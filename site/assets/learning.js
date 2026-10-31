/* Engineering Handbook learning path and spaced-repetition layer.
   All learning data is public; personal review state is stored only in the browser. */
const DAY=86400000, MINUTE=60000, NEW_DAILY_LIMIT=10;
const intervals=[0,1,3,7,14,30,60,120,240];
const WORDS={
 ru:{level:{fundamentals:'Основы',internals:'Внутренние механизмы',production:'Production'},units:'Учебные разделы',unit:'Учебный раздел',unitProgress:'Пройдено разделов',learn:'Изучить',objectives:'Цель обучения',definition:'Точное определение',mechanics:'Механизм выполнения',resources:'Ресурсы',pitfalls:'Граничные случаи и ошибки',code:'Пример кода',practice:'Проверить себя',references:'Первоисточники',done:'Отметить как изученное',undone:'Снять отметку',next:'Следующий раздел',back:'К модулю',flashcards:'Карточки для повторения',reviewSubtitle:'Интервальное повторение с двумя оценками. Сначала ответь самостоятельно, затем открой эталон.',due:'К повторению',newCards:'Новые сегодня',learned:'Изучено карточек',today:'Сегодня',showAnswer:'Показать ответ',again:'Не знаю',know:'Знаю',againHint:'Повтор через 10 минут',knowHint:'Следующий интервал: ',noCards:'На сегодня карточек больше нет.',nextDue:'Следующее повторение',allDone:'Повторения запланированы автоматически. Возвращайся, когда появятся карточки.',sourceLesson:'Основная тема',unseen:'Новая карточка',dueNow:'Повторение',yourProgress:'Интервалы: 1 → 3 → 7 → 14 → 30 дней при правильных ответах.',codeReminder:'Сначала предскажи результат. Выполнение кода доступно через Codespaces/Actions.',min:'мин',day:'д.',linkedQuestions:'Связанные задания',unitNo:'Раздел',studyUnits:'Продолжить изучение'},
 en:{level:{fundamentals:'Fundamentals',internals:'Internals',production:'Production'},units:'Learning units',unit:'Learning unit',unitProgress:'Units completed',learn:'Study',objectives:'Learning objective',definition:'Precise definition',mechanics:'Execution mechanics',resources:'Resources',pitfalls:'Boundary cases and failure modes',code:'Code example',practice:'Check your knowledge',references:'Primary references',done:'Mark as studied',undone:'Undo completion',next:'Next unit',back:'Back to module',flashcards:'Spaced-repetition cards',reviewSubtitle:'Two-button spaced repetition. Answer from memory, then reveal the reference.',due:'Due for review',newCards:'New today',learned:'Cards practiced',today:'Today',showAnswer:'Reveal answer',again:'Don’t know',know:'Know',againHint:'Review in 10 minutes',knowHint:'Next interval: ',noCards:'No more cards for today.',nextDue:'Next review',allDone:'Reviews are scheduled automatically. Return when cards are due.',sourceLesson:'Canonical module',unseen:'New card',dueNow:'Due review',yourProgress:'Intervals: 1 → 3 → 7 → 14 → 30 days after successive correct answers.',codeReminder:'Predict the outcome first. Use Codespaces or Actions for real execution.',min:'min',day:'d',linkedQuestions:'Related exercises',unitNo:'Unit',studyUnits:'Continue learning'}
};
const asDay=date=>{const d=new Date(date);return [d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-');};
const safe=(value)=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function nextIntervalDays(previous){return intervals[Math.min((previous?.streak||0)+1,intervals.length-1)];}
export function gradeCard(existing,questionId,known,now=Date.now()){
  const old=existing?.[questionId]||{};
  const streak=known?Math.min((old.streak||0)+1,intervals.length-1):0;
  const intervalMs=known?intervals[streak]*DAY:10*MINUTE;
  return {...existing,[questionId]:{
    createdDay:old.createdDay||asDay(now),
    firstAt:old.firstAt||now,
    lastAt:now, dueAt:now+intervalMs,
    streak, reviews:(old.reviews||0)+1,
    lapses:(old.lapses||0)+(known?0:1),
    lastKnown:!!known
  }};
}
export function selectCardQueue(questions,history,now=Date.now(),limit=NEW_DAILY_LIMIT){
  const all=questions||[];const today=asDay(now);const entries=Object.entries(history||{});
  const newToday=entries.filter(([,v])=>v.createdDay===today).length;
  const due=all.filter(q=>history?.[q.id]&&Number(history[q.id].dueAt)<=now)
    .sort((a,b)=>history[a.id].dueAt-history[b.id].dueAt);
  const remain=Math.max(0,limit-newToday);
  const newCards=all.filter(q=>!history?.[q.id]).slice(0,remain);
  const future=all.filter(q=>history?.[q.id]&&Number(history[q.id].dueAt)>now)
    .sort((a,b)=>history[a.id].dueAt-history[b.id].dueAt);
  return {current:due[0]||newCards[0]||null,dueCount:due.length,newCount:newCards.length,
    startedToday:newToday,completed:entries.length,remainingNew:all.length-entries.length,
    nextDue:future[0]?history[future[0].id].dueAt:null};
}
export function linkedUnitForQuestion(units,questionId){
  const number=Number(String(questionId).replace(/^Q-/,''));
  return units?.find(u=>u.questions.includes(number))||null;
}
export function moduleOutline(lesson,units,locale,progress,href){
  const t=WORDS[locale]||WORDS.ru;
  const list=(units||[]).filter(u=>u.lesson===lesson.id);
  return '<section class="unit-outline"><div class="section-title"><span class="section-index">01</span><h2>'+safe(t.units)+'</h2></div>'+
   '<p class="unit-subtitle">'+safe(t.unitProgress)+': '+list.filter(x=>progress?.[x.id]).length+' / '+list.length+'</p>'+
   '<div class="unit-list">'+list.map((u,i)=>
     '<a class="unit-list-item" href="'+href('unit',u.id)+'"><span class="unit-order">'+String(i+1).padStart(2,'0')+'</span>'+
     '<span class="unit-item-main"><span class="unit-level">'+safe(t.level[u.level]||u.level)+'</span><strong>'+safe(u.title[locale])+'</strong><small>'+safe(u.goal[locale])+'</small></span>'+
     '<span class="unit-completed">'+(progress?.[u.id]?'✓':'↗')+'</span></a>').join('')+'</div></section>';
}
export function unitView(unit,ctx){
 const {lang,units,questions,unitProgress,href}=ctx;
 const t=WORDS[lang]||WORDS.ru;
 const sequence=units.filter(u=>u.lesson===unit.lesson);
 const index=sequence.findIndex(u=>u.id===unit.id);
 const next=sequence[index+1];
 const refs=unit.refs||[];
 const qs=unit.questions.map(n=>questions.find(q=>q.id==='Q-'+String(n).padStart(3,'0'))).filter(Boolean);
 return '<nav class="unit-breadcrumb"><a href="'+href('lessons')+'">'+safe(t.units)+'</a> › <a href="'+href('lesson',unit.lesson)+'">'+safe(t.back)+'</a> › '+safe(t.unitNo)+' '+(index+1)+'</nav>'+
 '<header class="unit-heading"><span class="unit-level">'+safe(t.level[unit.level]||unit.level)+' · '+(index+1)+'/'+sequence.length+'</span><h1>'+safe(unit.title[lang])+'</h1><p class="lead">'+safe(unit.goal[lang])+'</p></header>'+
 '<article class="unit-article">'+
 '<section><h2>'+safe(t.definition)+'</h2><p>'+safe(unit.definition[lang])+'</p></section>'+
 '<section><h2>'+safe(t.mechanics)+'</h2><ol class="unit-steps">'+unit.steps.map((s,i)=>'<li><span>'+String(i+1).padStart(2,'0')+'</span><p>'+safe(s[lang])+'</p></li>').join('')+'</ol></section>'+
 '<section><h2>'+safe(t.resources)+'</h2><p>'+safe(unit.resources[lang])+'</p></section>'+
 '<section><h2>'+safe(t.pitfalls)+'</h2><p>'+safe(unit.pitfalls[lang])+'</p></section>'+
 (unit.code?'<section><h2>'+safe(t.code)+'</h2><pre class="unit-code"><code>'+safe(unit.code)+'</code></pre><p class="unit-small">'+safe(t.codeReminder)+'</p></section>':'')+
 '<section><h2>'+safe(t.linkedQuestions)+'</h2><div class="question-list">'+qs.map(q=>'<a class="question-link" href="'+href('question',q.id)+'"><span class="qid">'+safe(q.id)+'</span><span class="qtext">'+safe(q.question)+'</span><span class="qicon">↗</span></a>').join('')+'</div></section>'+
 '<section><h2>'+safe(t.references)+'</h2><ul>'+refs.map(r=>'<li><a class="inline-link" target="_blank" rel="noopener noreferrer" href="'+safe(r)+'">'+safe(r)+'</a></li>').join('')+'</ul></section></article>'+
 '<div class="unit-footer-actions"><a class="btn btn-secondary" href="'+href('lesson',unit.lesson)+'">← '+safe(t.back)+'</a>'+
 '<button class="btn '+(unitProgress?.[unit.id]?'btn-secondary':'btn-primary')+'" data-action="unit-completed" data-id="'+safe(unit.id)+'">'+safe(unitProgress?.[unit.id]?t.undone:t.done)+'</button>'+
 (next?'<a class="btn btn-secondary" href="'+href('unit',next.id)+'">'+safe(t.next)+' →</a>':'')+'</div>';
}
function timeLabel(ts,lang){return new Intl.DateTimeFormat(lang==='ru'?'ru-RU':'en-US',{dateStyle:'medium',timeStyle:'short'}).format(new Date(ts));}
export function cardsView(ctx){
 const {lang,questions,units,history,flipped,href,now,lessonId}=ctx;
 const t=WORDS[lang]||WORDS.ru;
 const scoped=lessonId?questions.filter(q=>q.lesson===lessonId):questions;
 const queue=selectCardQueue(scoped,history,now);
 const q=queue.current; const linked=q?linkedUnitForQuestion(units,q.id):null;
 const nextDays=q?nextIntervalDays(history?.[q.id]):1;
 const stats='<div class="card-stats"><div><b>'+queue.dueCount+'</b><small>'+safe(t.due)+'</small></div><div><b>'+queue.newCount+'</b><small>'+safe(t.newCards)+'</small></div><div><b>'+queue.completed+'</b><small>'+safe(t.learned)+'</small></div></div>';
 if(!q)return '<div class="unit-heading"><span class="unit-level">SRS</span><h1>'+safe(t.flashcards)+'</h1><p>'+safe(t.reviewSubtitle)+'</p></div>'+stats+
 '<div class="review-empty"><span>✓</span><h2>'+safe(t.noCards)+'</h2><p>'+safe(t.allDone)+'</p>'+
 (queue.nextDue?'<p><b>'+safe(t.nextDue)+':</b> '+safe(timeLabel(queue.nextDue,lang))+'</p>':'')+
 '<p>'+safe(t.yourProgress)+'</p></div>';
 const lines=q.code?'<pre class="unit-code"><code>'+safe(q.code)+'</code></pre>':'';
 return '<div class="unit-heading"><span class="unit-level">SRS · '+safe(t.today)+'</span><h1>'+safe(t.flashcards)+'</h1><p class="lead">'+safe(t.reviewSubtitle)+'</p></div>'+stats+
 '<article class="flashcard"><div class="flashcard-top"><span>'+safe(q.id)+'</span><span>'+safe(history?.[q.id]?t.dueNow:t.unseen)+'</span></div>'+
 '<div class="flashcard-question"><h2>'+safe(q.question)+'</h2>'+lines+'</div>'+
 (flipped?'<div class="flashcard-answer"><span class="answer-label">'+safe(t.showAnswer)+'</span><p>'+safe(q.answer)+'</p></div>'+
 '<div class="flashcard-grades"><button class="btn btn-again" data-action="card-grade" data-id="'+safe(q.id)+'" data-grade="again"><strong>'+safe(t.again)+'</strong><small>'+safe(t.againHint)+'</small></button>'+
 '<button class="btn btn-good" data-action="card-grade" data-id="'+safe(q.id)+'" data-grade="know"><strong>'+safe(t.know)+'</strong><small>'+safe(t.knowHint)+' '+nextDays+' '+safe(t.day)+'</small></button></div>':
 '<button class="btn btn-primary flashcard-flip" data-action="card-flip">'+safe(t.showAnswer)+'</button>')+
 (linked?'<div class="flashcard-reference">'+safe(t.sourceLesson)+': <a href="'+href('unit',linked.id)+'">'+safe(linked.title[lang])+' ↗</a></div>':'')+
 '</article><p class="unit-small">'+safe(t.yourProgress)+'</p>';
}
