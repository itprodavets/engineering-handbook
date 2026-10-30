/* Engineering Handbook — dependency-free, static bilingual learning interface.
   Answers and progress stay in the browser; C# execution uses Codespaces/Actions. */
const REPO = 'https://github.com/itprodavets/engineering-handbook';
const CODESPACES = 'https://codespaces.new/itprodavets/engineering-handbook';
const UI = {
  ru: {
    overview:'Обзор',curriculum:'Темы',practice:'Практика',glossary:'Термины',search:'Поиск по темам и вопросам',
    modules:'Направления',progress:'Прогресс обучения',studied:'Изучено',forReview:'Повторить',questions:'Вопросов',
    introKicker:'ENGINEERING • LEARN BY UNDERSTANDING',introStart:'Разбирай устройство систем.',introEnd:'Не заучивай ответы.',
    intro:'Языки, базы данных, AI/LLM/RAG, Kafka, архитектура, ОС и инфраструктура. Одна тема — одно объяснение; вопросы и лаборатории закрепляют механизм.',
    start:'Начать с async/await',browse:'Каталог тем',lesson:'Основная тема',review:'Проверка знаний',reinforcement:'Закрепление',
    allModules:'Карта знаний',moduleIntro:'Все основные механизмы изложены один раз. Упражнения привязаны к конкретным темам.',
    active:'Доступно',planned:'В планах',comingTitle:'Следующие направления',comingText:'После .NET будем добавлять Go, Kafka, PostgreSQL и другие технологии в тот же структурированный каталог.',
    go:'Открыть тему',openQuestion:'Открыть вопрос',questionsShort:'вопросов',mastered:'освоено',
    definition:'Определение',mechanism:'Внутренний механизм',resources:'Ресурсы и ограничения',pitfalls:'Типичные ошибки',
    check:'Проверить понимание',train:'Примеры для закрепления',sources:'Первоисточники',
    questionPrefix:'Вопрос',challenge:'Задача с подвохом',related:'Теория изучается здесь',predict:'Сначала сформулируй свой ответ',
    writeAnswer:'Твой ответ или предсказание',answerPlaceholder:'Напиши, что произойдёт и почему…',outputPlaceholder:'Например: ABC',
    checkPrediction:'Проверить вывод',showAnswer:'Показать эталонный ответ',hideAnswer:'Скрыть ответ',
    clear:'Сбросить код',copy:'Копировать код',copied:'Скопировано',
    actualRun:'Запустить код',runActions:'Запустить через Actions',runCodespaces:'Открыть Codespaces',
    runHint:'Проверка сравнивает предсказание с эталоном, но не выполняет код. Для изменённого примера используй Codespaces. Actions запускает только сохранённый код .NET.',
    checkCorrect:'Предсказание совпало с эталонным выводом. Теперь объясни механизм.',
    checkWrong:'Вывод отличается от эталона. Перепроверь порядок выполнения и попробуй ещё раз.',
    checkNotSupported:'У этого задания нет одного гарантированного вывода. Оцени механизм и сравни с разбором.',
    noPrediction:'Сначала введи предполагаемый вывод.',modifiedCode:'Ты изменил код. Эталонный вывод относится к исходному варианту; запусти изменённый код в Codespaces.',
    yourProgress:'Как оцениваешь понимание?',markMastered:'✓ Изучено',markReview:'↺ Повторить',resetMark:'Сбросить отметку',
    next:'Следующий вопрос',backLesson:'К основной теме',previous:'Предыдущий',
    sourceMarkdown:'Открыть Markdown',safeNote:'Прогресс сохраняется только в этом браузере. Без аккаунта, без отправки личных ответов на сервер.',
    filter:'Фильтр по теме',all:'Все темы',filterReview:'Требуют повторения',practiceCount:'Задач с кодом',
    noResults:'Ничего не найдено. Попробуй другой запрос.',codeEditor:'Редактируемый пример',
    challengeLabel:'ПРЕДСКАЖИ РЕЗУЛЬТАТ',theoryLabel:'ОБЪЯСНИ МЕХАНИЗМ',
    references:'Полезные источники',footer:'Точные определения • RU / EN • Код с проверяемым поведением',
    searchResult:'Результаты поиска',searchNo:'Совпадений нет',searchTopics:'Темы',searchQuestions:'Вопросы',
    hintSpace:'Введите текст для поиска',stages:{execution:'Выполнение и async',concurrency:'Потоки и синхронизация',reliability:'Ошибки и надёжность'},
    glossaryIntro:'Термины отдельно от вопросов, без повторения учебных объяснений.',
    noLab:'Для этого вопроса отдельной запускаемой лаборатории нет. Можно изучить механизм в основной теме.',
    categoryQuiz:'Теоретические вопросы',categoryCode:'Примеры с кодом',clearFilter:'Сбросить фильтр',
    themeLight:'Светлая тема',themeDark:'Тёмная тема',openSidebar:'Открыть меню',closeSidebar:'Закрыть меню',
    notExecution:'Это проверка предсказания, не запуск компилятора.',
    verifyBefore:'Эталонный ответ скрыт до твоей попытки.',
    notices:'Публичный учебник не содержит личных оценок из Google Таблицы.',
    area:'Направление',browseArea:'Открыть раздел',lessonCount:'Готовых уроков',tracksCount:'Технологий',noLesson:'Уроки появятся после проверки материалов.',
  },
  en: {
    overview:'Overview',curriculum:'Curriculum',practice:'Practice',glossary:'Glossary',search:'Search topics and questions',
    modules:'Knowledge areas',progress:'Learning progress',studied:'Mastered',forReview:'Review',questions:'Questions',
    introKicker:'ENGINEERING • LEARN BY UNDERSTANDING',introStart:'Understand how systems work.',introEnd:'Go beyond memorized answers.',
    intro:'Languages, databases, AI/LLM/RAG, Kafka, architecture, OS internals and infrastructure. One canonical lesson per concept, reinforced by questions and labs.',
    start:'Start with async/await',browse:'Explore lessons',lesson:'Canonical lesson',review:'Knowledge check',reinforcement:'Reinforcement',
    allModules:'Knowledge map',moduleIntro:'Each core mechanism has one lesson. Exercises are linked to that canonical explanation.',
    active:'Available',planned:'Planned',comingTitle:'Next learning tracks',comingText:'Go, Kafka, PostgreSQL, and other topics will grow within the same organized curriculum.',
    go:'Open lesson',openQuestion:'Open question',questionsShort:'questions',mastered:'mastered',
    definition:'Definition',mechanism:'Under the hood',resources:'Resources and constraints',pitfalls:'Failure modes',
    check:'Check your understanding',train:'Reinforcement challenges',sources:'Primary references',
    questionPrefix:'Question',challenge:'Tricky code challenge',related:'Canonical explanation',predict:'Write your reasoning first',
    writeAnswer:'Your answer or prediction',answerPlaceholder:'Explain what happens and why…',outputPlaceholder:'For example: ABC',
    checkPrediction:'Check predicted output',showAnswer:'Reveal model answer',hideAnswer:'Hide answer',
    clear:'Reset code',copy:'Copy code',copied:'Copied',
    actualRun:'Run code',runActions:'Run with Actions',runCodespaces:'Open Codespaces',
    runHint:'The checker compares a prediction with a reference, but does not execute code. Use Codespaces to run edited snippets; Actions runs committed .NET examples only.',
    checkCorrect:'Your prediction matches the reference output. Now explain why it happens.',
    checkWrong:'The output does not match the reference. Recheck execution order and try again.',
    checkNotSupported:'This challenge has no single guaranteed output. Compare the mechanism with the explanation.',
    noPrediction:'Enter your predicted output first.',modifiedCode:'You modified the code. The expected output applies to the original version; run your edited code in Codespaces.',
    yourProgress:'How well do you understand it?',markMastered:'✓ Mastered',markReview:'↺ Review again',resetMark:'Clear status',
    next:'Next question',backLesson:'Back to lesson',previous:'Previous',
    sourceMarkdown:'View Markdown',safeNote:'Progress is saved only in this browser. No account required; personal answers are never sent to a server.',
    filter:'Filter by lesson',all:'All lessons',filterReview:'Needs review',practiceCount:'Code challenges',
    noResults:'No matching material. Try a different search.',codeEditor:'Editable example',
    challengeLabel:'PREDICT THE OUTCOME',theoryLabel:'EXPLAIN THE MECHANISM',
    references:'Further reading',footer:'Precise definitions • RU / EN • Verifiable code examples',
    searchResult:'Search results',searchNo:'Nothing found',searchTopics:'Lessons',searchQuestions:'Questions',
    hintSpace:'Type to search',stages:{execution:'Runtime and async',concurrency:'Threads and synchronization',reliability:'Reliability and failure'},
    glossaryIntro:'Terminology has a dedicated reference, rather than duplicating lessons.',
    noLab:'This question has no runnable standalone lab. Explore the underlying mechanism in its canonical lesson.',
    categoryQuiz:'Concept questions',categoryCode:'Code challenges',clearFilter:'Clear filter',
    themeLight:'Light theme',themeDark:'Dark theme',openSidebar:'Open menu',closeSidebar:'Close menu',
    notExecution:'This checks a prediction; it does not execute the source code.',
    verifyBefore:'The model answer is hidden until you attempt the question.',
    notices:'The public handbook does not contain private learner scores.',
    area:'Knowledge area',browseArea:'Open area',lessonCount:'Available lessons',tracksCount:'Technologies',noLesson:'Lessons will appear after verification.',
  },
};
const PREDICTABLE = {'Q-024':'ABC','Q-025':'ACB','Q-026':'True','Q-027':'2','Q-030':'DONE','Q-031':'X','Q-032':'True','Q-034':'False'};
const UPCOMING = ['Go','Kafka','PostgreSQL','Kubernetes'];
 const TRACK_LABELS = {dotnet:'.NET / C#', go:'Go', kafka:'Kafka', postgresql:'PostgreSQL', kubernetes:'Kubernetes', linux:'Linux', 'system-design':'System Design'};
 const trackLabel = track => TRACK_LABELS[track] || track;
const stageOrder=['execution','concurrency','reliability'];
const root=document.getElementById('app');
const state={lang:'ru',data:null,renderToken:0,route:['home'],mobile:false,query:'',filter:'all',drafts:{},edits:{},revealed:{},checks:{},theme:'light',progress:{},cache:{}};
function getStored(key,fallback){try{const value=localStorage.getItem(key);return value?JSON.parse(value):fallback;}catch{return fallback;}}
function persist(key,value){try{localStorage.setItem(key,JSON.stringify(value));}catch{}}
state.progress=getStored('eh:progress:v1',{});
state.theme=getStored('eh:theme:v1','light');
document.documentElement.dataset.theme=state.theme;
function escapeHTML(v){return String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function strip(v){return String(v??'').replace(/\s+/g,' ').trim();}
function routePath(lang,section='home',id=''){return `#/${lang}/${section}${id?'/'+encodeURIComponent(id):''}`;}
function currentPath(){const parts=decodeURIComponent(location.hash.replace(/^#\/?/,'')).split('/').filter(Boolean);return {lang:['ru','en'].includes(parts[0])?parts[0]:'ru',section:parts[1]||'home',id:parts[2]||''};}
const t=()=>UI[state.lang];
const qById=id=>state.data.questions.find(q=>q.id===id);
const lById=id=>state.data.lessons.find(l=>l.id===id);
const completed=()=>state.data?.questions?.filter(q=>statusOf(q.id)==='mastered').length||0;
const needsReview=()=>state.data?.questions?.filter(q=>statusOf(q.id)==='review').length||0;
const statusOf=id=>state.progress[id]?.status||'';
const href=(section,id='')=>routePath(state.lang,section,id);
function icon(name){return {home:'▣',lessons:'▤',practice:'⌘',glossary:'≡'}[name]||'◈';}
async function load(lang){if(!state.cache[lang]){state.cache[lang]=fetch(`./data/${lang}.json`).then(async r=>{if(!r.ok)throw Error(`Content ${lang}: ${r.status}`);return r.json();});}return state.cache[lang];}
function progressBar(){const total=Math.max(1,state.data?.questions?.length||0);const pct=Math.round(completed()/total*100);return `<div class="progress-track" role="progressbar" aria-label="${escapeHTML(t().progress)}" aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100"><div class="progress-fill" style="width:${pct}%"></div></div>`;}
function activeNav(section){if(['lesson','lessons'].includes(section))return 'lessons';if(section==='question')return 'practice';return section;}
function header(r){const u=t();const langTwin=state.lang==='ru'?'en':'ru';const section=r.section==='home'?'home':r.section;return `<header class="header">
  <button class="icon-btn mobile-toggle" type="button" data-action="toggle-menu" aria-label="${escapeHTML(u.openSidebar)}">☰</button>
  <a class="brand" href="${href('home')}" aria-label="Engineering Handbook"><span class="brand-mark">&gt;_</span><span class="brand-name">Engineering Handbook<small>software engineering • fundamentals to internals</small></span></a>
  <div class="header-search"><span class="search-ico" aria-hidden="true">⌕</span><input id="search" type="search" placeholder="${escapeHTML(u.search)}" autocomplete="off" aria-label="${escapeHTML(u.search)}"><span class="shortcut">/</span><div id="search-results"></div></div>
  <div class="header-actions"><div class="lang-switch" role="group" aria-label="Language"><a href="${routePath('ru',section,r.id)}" class="${state.lang==='ru'?'active':''}" lang="ru" aria-current="${state.lang==='ru'?'true':'false'}">RU</a><a href="${routePath('en',section,r.id)}" class="${state.lang==='en'?'active':''}" lang="en" aria-current="${state.lang==='en'?'true':'false'}">EN</a></div><button class="icon-btn" data-action="toggle-theme" type="button" title="${escapeHTML(state.theme==='light'?u.themeDark:u.themeLight)}">${state.theme==='light'?'☾':'☼'}</button></div>
</header>`;}
function sidebar(r){const u=t();const active=activeNav(r.section);const routes=[['home',u.overview],['lessons',u.curriculum],['practice',u.practice],['glossary',u.glossary]];
return `<aside id="sidebar" class="sidebar ${state.mobile?'open':''}"><div class="side-label">${u.overview}</div>${routes.map(([route,label])=>`<a class="side-link ${route===active?'active':''}" href="${href(route)}"><span class="glyph">${icon(route)}</span>${escapeHTML(label)}${route==='practice'?'<span class="side-count">${state.data.questions.length}</span>':''}</a>`).join('')}<div class="side-section"><div class="side-label">${escapeHTML(u.modules)}</div>${catalog().map((l,i)=>`<a class="side-topic ${r.section==='category'&&r.id===l.id?'active':''}" href="${href('category',l.id)}"><span class="topic-dot"></span><span>${escapeHTML(l.title)}</span></a>`).join('')}</div><div class="sidebar-footer"><strong>${escapeHTML(u.progress)}</strong><div class="small-text">${completed()}/${state.data.questions.length} ${escapeHTML(u.mastered)}</div>${progressBar()}<div class="small-text">${needsReview()} ${escapeHTML(u.forReview.toLowerCase())}</div></div></aside>`;}
function breadcrumb(links){return `<div class="breadcrumb">${links.map((x,i)=>`${i?'<span class="chevron">›</span>':''}${x.href?`<a href="${x.href}">${escapeHTML(x.label)}</a>`:`<span>${escapeHTML(x.label)}</span>`}`).join('')}</div>`;}
function panelLink(lesson){return `<a href="${href('lesson',lesson.id)}" class="inline-link">${escapeHTML(t().go)} ↗</a>`;}
function moduleCard(lesson,i){const qs=lesson.questions.map(n=>qById('Q-'+String(n).padStart(3,'0'))).filter(Boolean);const core=qs.filter(q=>q.kind==='review').length,pract=qs.filter(q=>q.kind==='reinforcement').length;return `<a class="module-card" href="${href('lesson',lesson.id)}"><span class="mod-num">${String(i+1).padStart(2,'0')} / ${escapeHTML(t().active)}</span><h3>${escapeHTML(lesson.title)}</h3><p>${escapeHTML(lesson.desc)}</p><div class="card-foot"><span>${core} ${escapeHTML(t().questionsShort)} · ${pract} ${escapeHTML(t().practice.toLowerCase())}</span><span class="more">${escapeHTML(t().go)} ↗</span></div></a>`;}
const catalog=()=>state.data?.catalog||[];
const category=id=>catalog().find(c=>c.id===id);
function categorySections(){return `<div class="module-grid">${catalog().map((cat,i)=>{const count=state.data.lessons.filter(l=>cat.tracks.some(t=>t.id===(l.track||"dotnet"))).length;return `<a class="module-card" href="${href("category",cat.id)}"><span class="mod-num">${String(i+1).padStart(2,"0")} / ${escapeHTML(count?t().active:t().planned)}</span><h3>${escapeHTML(cat.title)}</h3><p>${escapeHTML(cat.description)}</p><div class="card-foot"><span>${count} ${escapeHTML(t().lessonCount.toLowerCase())} · ${cat.tracks.length} ${escapeHTML(t().tracksCount.toLowerCase())}</span><span class="more">${escapeHTML(t().browseArea)} ↗</span></div></a>`;}).join("")}</div>`;}
function categoryPage(id){const cat=category(id);if(!cat)return notFound();const u=t();const groups=cat.tracks.map(track=>{const lessons=state.data.lessons.filter(l=>(l.track||"dotnet")===track.id);return `<div class="section-head"><h2>${escapeHTML(track.title)}</h2></div>${lessons.length?`<div class="module-grid">${lessons.map(l=>moduleCard(l,state.data.lessons.indexOf(l))).join("")}</div>`:`<p class="small-text">${escapeHTML(u.planned)} — ${escapeHTML(u.noLesson)}</p>`}`;}).join("");return `${breadcrumb([{label:u.overview,href:href("home")},{label:u.curriculum,href:href("lessons")},{label:cat.title}])}<div class="lesson-hero"><div class="eyebrow">${escapeHTML(u.area)}</div><h1>${escapeHTML(cat.title)}</h1><p class="lead">${escapeHTML(cat.description)}</p></div>${groups}`;}
function stageSections(){const tracks=[...new Set(state.data.lessons.map(l=>l.track||'dotnet'))];return tracks.map(track=>{const lessons=state.data.lessons.filter(l=>(l.track||'dotnet')===track);const stages=[...new Set([...stageOrder,...lessons.map(l=>l.stage)])].filter(stage=>lessons.some(l=>l.stage===stage));return `<div class="section-head"><div><h2>${escapeHTML(trackLabel(track))}</h2></div></div>`+stages.map(stage=>{const group=lessons.filter(l=>l.stage===stage);return `<div class="section-head"><div><div class="eyebrow"><span class="dot-accent"></span>${escapeHTML(t().stages[stage]||stage)}</div></div></div><div class="module-grid">${group.map(l=>moduleCard(l,state.data.lessons.indexOf(l))).join('')}</div>`;}).join('');}).join('');}
function stageComing(){const present=new Set(state.data.lessons.map(l=>trackLabel(l.track||'dotnet')));const future=UPCOMING.filter(name=>!present.has(name));if(!future.length)return '';return `<div class="section-head"><div><h2>${escapeHTML(t().comingTitle)}</h2><p>${escapeHTML(t().comingText)}</p></div></div><div class="module-grid">${future.map(name=>`<div class="module-card upcoming"><span class="mod-num muted-num">${escapeHTML(t().planned)}</span><h3>${name}</h3><p>${escapeHTML(t().comingText)}</p></div>`).join('')}</div>`;}
function home(){const u=t();return `${breadcrumb([{label:u.overview}])}<div class="hero"><div class="eyebrow"><span class="dot-accent"></span>${u.introKicker}</div><h1>${escapeHTML(u.introStart)} <span>${escapeHTML(u.introEnd)}</span></h1><p class="lead">${escapeHTML(u.intro)}</p><div class="hero-actions"><a class="btn btn-primary" href="${href('lesson','async-lifecycle')}">${escapeHTML(u.start)} ↗</a><a class="btn btn-secondary" href="${href('lessons')}">${escapeHTML(u.browse)} →</a></div></div><div class="stat-row"><div class="stat"><b>${catalog().length}</b><span>${escapeHTML(u.modules)}</span></div><div class="stat"><b>${state.data.questions.length}</b><span>${escapeHTML(u.questions)}</span></div><div class="stat"><b>${completed()}/${state.data.questions.length}</b><span>${escapeHTML(u.studied)}</span></div></div><div class="section-head"><div><h2>${escapeHTML(u.allModules)}</h2><p>${escapeHTML(u.moduleIntro)}</p></div><a class="inline-link" href="${href('practice')}">${escapeHTML(u.practice)} ↗</a></div>${categorySections()}<div class="note"><span class="note-icon">◎</span><div><b>${escapeHTML(u.safeNote)}</b><div>${escapeHTML(u.notices)}</div></div></div>`;}
function lessonsPage(){return `${breadcrumb([{label:t().overview,href:href('home')},{label:t().curriculum}])}<div class="lesson-hero"><div class="eyebrow"><span class="dot-accent"></span>${escapeHTML(t().modules.toUpperCase())}</div><h1>${escapeHTML(t().allModules)}</h1><p class="lead">${escapeHTML(t().moduleIntro)}</p></div>${categorySections()}`;}
function sectionHeading(index,text){return `<div class="section-title"><span class="section-index">${index}</span><h2>${escapeHTML(text)}</h2></div>`;}
function questionRow(q){const flag=statusOf(q.id);return `<a href="${href('question',q.id)}" class="question-link"><span class="qid">${escapeHTML(q.id)}</span><span class="qtext">${escapeHTML(q.question)}${q.kind==='reinforcement'?` <span class="kind-tag practice">${escapeHTML(t().reinforcement)}</span>`:''}${flag?` <span class="badge-mini ${flag==='review'?'review':''}">${flag==='mastered'?'✓':'↺'}</span>`:''}</span><span class="qicon">↗</span></a>`;}
function lessonPage(id){const lesson=lById(id);if(!lesson)return notFound();const u=t(),core=lesson.questions.map(n=>qById('Q-'+String(n).padStart(3,'0'))).filter(q=>q?.kind==='review'),pract=lesson.questions.map(n=>qById('Q-'+String(n).padStart(3,'0'))).filter(q=>q?.kind==='reinforcement');
return `${breadcrumb([{label:u.overview,href:href('home')},{label:u.curriculum,href:href('lessons')},{label:lesson.title}])}<div class="lesson-hero"><div class="eyebrow"><span class="dot-accent"></span>${escapeHTML(u.lesson.toUpperCase())} · ${escapeHTML(u.stages[lesson.stage]||lesson.stage)}</div><h1>${escapeHTML(lesson.title)}</h1><p class="lead">${escapeHTML(lesson.desc)}</p></div>${sectionHeading('01',u.definition)}<p>${escapeHTML(lesson.overview)}</p>${sectionHeading('02',u.mechanism)}<div class="mechanism-list">${lesson.mechanism.map((s,i)=>`<div class="step"><i>${String(i+1).padStart(2,'0')}</i><p>${escapeHTML(s)}</p></div>`).join('')}</div>${sectionHeading('03',u.resources)}<div class="resources">${lesson.resources.map(r=>`<div class="resource"><h3>${escapeHTML(r.name)}</h3><p>${escapeHTML(r.detail)}</p></div>`).join('')}</div>${sectionHeading('04',u.pitfalls)}<ul class="pitfalls">${lesson.risks.map(x=>`<li>${escapeHTML(x)}</li>`).join('')}</ul>${sectionHeading('05',u.check)}<div class="question-list">${core.map(questionRow).join('')}</div>${pract.length?`${sectionHeading('06',u.train)}<div class="note"><span class="note-icon">◎</span><div>${escapeHTML(u.moduleIntro)}</div></div><div class="question-list">${pract.map(questionRow).join('')}</div>`:''}${sectionHeading('↗',u.sources)}<ul class="pitfalls">${lesson.refs.map(x=>`<li><a target="_blank" rel="noopener noreferrer" href="${escapeHTML(x)}" class="inline-link">${escapeHTML(x)}</a></li>`).join('')}</ul>`;}
function challengeEditor(q){const u=t();const code=state.edits[q.id]??q.code;const command=q.runCommand||'';const editorLabel=q.codeLanguage==='go'?'Go':q.codeLanguage==='csharp'?'C#':(q.codeLanguage||'Code');return `<div class="code-window"><div class="code-titlebar"><span class="dots"><i></i><i></i><i></i></span><span>${escapeHTML(u.codeEditor)}</span><span>${escapeHTML(editorLabel)}</span></div><textarea id="code-editor" class="code-editor" spellcheck="false" aria-label="${escapeHTML(u.codeEditor)}" style="height:${Math.min(420,Math.max(170,code.split('\n').length*22+45))}px">${escapeHTML(code)}</textarea></div><div class="code-controls"><button class="btn btn-secondary btn-small" data-action="copy-code" data-id="${q.id}">⧉ ${escapeHTML(u.copy)}</button><button class="btn btn-secondary btn-small" data-action="reset-code" data-id="${q.id}">↺ ${escapeHTML(u.clear)}</button>${q.lab?`<a class="btn btn-soft btn-small" href="${CODESPACES}" target="_blank" rel="noopener noreferrer">⌘ ${escapeHTML(u.runCodespaces)}</a>${q.track==='dotnet'?`<a class="btn btn-soft btn-small" href="${REPO}/actions/workflows/run-lab.yml" target="_blank" rel="noopener noreferrer">▶ ${escapeHTML(u.runActions)}</a>`:''}`:''}</div><div class="code-note">${escapeHTML(u.runHint)}${command?` <code>${escapeHTML(command)}</code>`:''}</div>`;}
function questionPage(id){const q=qById(id);if(!q)return notFound();const l=lById(q.lesson),u=t(),shown=!!state.revealed[id],answer=state.drafts[id]||'',check=state.checks[id],hasCode=!!q.code,prevNext=l.questions.map(n=>'Q-'+String(n).padStart(3,'0')),i=prevNext.indexOf(id),prev=prevNext[i-1]||null,next=prevNext[i+1]||null;
return `${breadcrumb([{label:u.overview,href:href('home')},{label:u.curriculum,href:href('lessons')},{label:l.title,href:href('lesson',l.id)},{label:id}])}<div class="qhead"><div class="eyebrow"><span class="dot-accent"></span>${hasCode?escapeHTML(u.challengeLabel):escapeHTML(u.theoryLabel)} · ${id}</div><h1>${escapeHTML(hasCode?u.challenge:u.questionPrefix+' '+id)}</h1><div class="qfoot"><span class="kind-tag ${hasCode?'practice':''}">${escapeHTML(hasCode?u.reinforcement:u.review)}</span><a class="inline-link" href="${REPO}/blob/main/${encodeURI(q.markdown)}" target="_blank" rel="noopener noreferrer">${escapeHTML(u.sourceMarkdown)} ↗</a></div></div><div class="lesson-ref">${escapeHTML(u.related)}: <a href="${href('lesson',l.id)}">${escapeHTML(l.title)} ↗</a></div><div class="challenge-card"><h2>${escapeHTML(u.predict)}</h2><p class="prompt">${escapeHTML(q.question)}</p>${hasCode?challengeEditor(q):''}<div class="answer-field"><label for="my-answer">${escapeHTML(u.writeAnswer)}</label><textarea id="my-answer" rows="3" placeholder="${escapeHTML(hasCode&&(q.checkOutput||PREDICTABLE[id])?u.outputPlaceholder:u.answerPlaceholder)}">${escapeHTML(answer)}</textarea></div><div class="answer-actions">${hasCode?`<button class="btn btn-secondary" data-action="check-prediction" data-id="${id}">${escapeHTML(u.checkPrediction)}</button>`:''}<button class="btn btn-primary" data-action="toggle-answer" data-id="${id}">${escapeHTML(shown?u.hideAnswer:u.showAnswer)}</button></div>${check?`<div class="feedback ${check==='correct'?'':'try'}" role="status">${escapeHTML(check==='correct'?u.checkCorrect:check==='wrong'?u.checkWrong:check==='empty'?u.noPrediction:check==='modified'?u.modifiedCode:u.checkNotSupported)}</div>`:''}${shown?`<div class="answer-box"><span class="answer-label">${escapeHTML(u.showAnswer)}</span><p>${escapeHTML(q.answer)}</p></div>`:`<div class="small-text" style="margin-top:12px">${escapeHTML(u.verifyBefore)}</div>`}</div><div class="statusbar"><div><span class="status-label">${escapeHTML(u.yourProgress)} </span>${statusOf(id)?`<span class="badge-mini ${statusOf(id)==='review'?'review':''}">${escapeHTML(statusOf(id)==='mastered'?u.studied:u.forReview)}</span>`:''}</div><div class="buttons"><button class="btn btn-soft btn-small" data-action="mark-mastered" data-id="${id}">${escapeHTML(u.markMastered)}</button><button class="btn btn-secondary btn-small" data-action="mark-review" data-id="${id}">${escapeHTML(u.markReview)}</button>${statusOf(id)?`<button class="btn btn-secondary btn-small" data-action="clear-progress" data-id="${id}">${escapeHTML(u.resetMark)}</button>`:''}</div></div><div class="statusbar"><div class="buttons">${prev?`<a class="btn btn-secondary" href="${href('question',prev)}">← ${escapeHTML(u.previous)}</a>`:''}<a class="btn btn-secondary" href="${href('lesson',l.id)}">${escapeHTML(u.backLesson)}</a></div>${next?`<a class="btn btn-primary" href="${href('question',next)}">${escapeHTML(u.next)} →</a>`:''}</div>`;}
function practicePage(){const u=t(),filter=state.filter;const qs=state.data.questions.filter(q=>filter==='all'||filter==='review'&&statusOf(q.id)==='review'||q.lesson===filter);const core=qs.filter(q=>q.kind==='review'),rein=qs.filter(q=>q.kind==='reinforcement');return `${breadcrumb([{label:u.overview,href:href('home')},{label:u.practice}])}<div class="lesson-hero"><div class="eyebrow"><span class="dot-accent"></span>${escapeHTML(u.practice.toUpperCase())}</div><h1>${escapeHTML(u.check)}</h1><p class="lead">${escapeHTML(u.moduleIntro)}</p></div><div class="filter-bar"><label for="topic-select" class="small-text">${escapeHTML(u.filter)}</label><select id="topic-select"><option value="all" ${filter==='all'?'selected':''}>${escapeHTML(u.all)}</option><option value="review" ${filter==='review'?'selected':''}>${escapeHTML(u.filterReview)}</option>${state.data.lessons.map(l=>`<option value="${escapeHTML(l.id)}" ${filter===l.id?'selected':''}>${escapeHTML(l.title)}</option>`).join('')}</select></div>${qs.length?`${core.length?`<div class="list-group"><h3>${escapeHTML(u.categoryQuiz)} · ${core.length}</h3><div class="question-list">${core.map(questionRow).join('')}</div></div>`:''}${rein.length?`<div class="list-group"><h3>${escapeHTML(u.categoryCode)} · ${rein.length}</h3><div class="question-list">${rein.map(questionRow).join('')}</div></div>`:''}`:`<div class="empty">${escapeHTML(u.noResults)}</div>`}`;}
function glossaryPage(){const u=t(),entries=state.data.glossary||[];return `${breadcrumb([{label:u.overview,href:href('home')},{label:u.glossary}])}<div class="lesson-hero"><div class="eyebrow"><span class="dot-accent"></span>REFERENCE</div><h1>${escapeHTML(u.glossary)}</h1><p class="lead">${escapeHTML(u.glossaryIntro)}</p></div><div class="glossary-grid">${entries.map(x=>`<div class="glossary-card"><h3>${escapeHTML(x.term)}</h3><p>${escapeHTML(x.definition)}</p><small>${escapeHTML(x.example)}</small></div>`).join('')}</div>`;}
function notFound(){return `<div class="empty">${escapeHTML(t().noResults)} <p><a class="inline-link" href="${href('home')}">${escapeHTML(t().overview)} ↗</a></p></div>`;}
function footer(){return `<footer class="footer"><span>${escapeHTML(t().footer)}</span><span><a href="${REPO}" target="_blank" rel="noopener noreferrer">GitHub ↗</a> · <a href="${REPO}/actions" target="_blank" rel="noopener noreferrer">Actions ↗</a> · <a href="${CODESPACES}" target="_blank" rel="noopener noreferrer">Codespaces ↗</a></span></footer>`;}
function searchResults(query){const u=t(),text=strip(query).toLowerCase();if(text.length<2)return '';const areas=catalog().filter(c=>(c.title+" "+c.description+" "+c.tracks.map(t=>t.title).join(" ")).toLowerCase().includes(text)).slice(0,5);const lessons=state.data.lessons.filter(x=>(x.title+' '+x.desc).toLowerCase().includes(text)).slice(0,5);const qs=state.data.questions.filter(q=>(q.id+' '+q.question+' '+q.title).toLowerCase().includes(text)).slice(0,7);const rows=[...areas.map(x=>`<a class="search-row" href="${href("category",x.id)}"><b>${escapeHTML(u.area)}</b>${escapeHTML(x.title)}</a>`),...lessons.map(x=>`<a class="search-row" href="${href('lesson',x.id)}"><b>${escapeHTML(u.lesson)}</b>${escapeHTML(x.title)}</a>`),...qs.map(x=>`<a class="search-row" href="${href('question',x.id)}"><b>${escapeHTML(x.id)}</b>${escapeHTML(x.question)}</a>`)];return `<div class="search-overlay">${rows.join('')||`<div class="small-text" style="padding:15px">${escapeHTML(u.searchNo)}</div>`}</div>`;}
function updateSearchDisplay(){const el=document.getElementById('search-results');if(el)el.innerHTML=state.query?searchResults(state.query):'';}
function mainPage(section,id){if(section==='home')return home();if(section==='lessons')return lessonsPage();if(section==='category')return categoryPage(id);if(section==='lesson')return lessonPage(id);if(section==='question')return questionPage(id);if(section==='practice')return practicePage();if(section==='glossary')return glossaryPage();return notFound();}
async function render(){const token=++state.renderToken;const r=currentPath();const was=state.lang;state.lang=r.lang;state.route=[r.section,r.id];document.documentElement.lang=state.lang;
 try{const loaded=await load(r.lang);if(token!==state.renderToken)return;state.data=loaded;}catch(err){root.innerHTML=`<div class="bootstrap"><h2>Content unavailable</h2><p>${escapeHTML(err.message)}</p></div>`;return;}
 document.title=`${r.id?(r.section==='lesson'?lById(r.id)?.title:r.section==='category'?category(r.id)?.title:qById(r.id)?.id)+' — ':''}Engineering Handbook`;
 root.innerHTML=`<div class="shell">${header(r)}<div class="body-grid">${sidebar(r)}<div class="sidebar-scrim ${state.mobile?'show':''}" data-action="close-menu"></div><main id="main" class="main"><div class="content">${mainPage(r.section,r.id)}${footer()}</div></main></div></div>`;
 const inp=document.getElementById('search');if(inp)inp.value=state.query;updateSearchDisplay();
 if(was!==r.lang||r.section!==state.lastSection||r.id!==state.lastId){window.scrollTo(0,0);state.mobile=false;state.query='';}
 state.lastSection=r.section;state.lastId=r.id;
}
function setProgress(id,status){if(status){state.progress[id]={status,at:new Date().toISOString()};}else delete state.progress[id];persist('eh:progress:v1',state.progress);render();}
function normalizeOutput(s){return strip(s).replace(/\s+/g,'').toLowerCase();}
function doAction(action,id){switch(action){
 case 'toggle-theme':state.theme=state.theme==='light'?'dark':'light';document.documentElement.dataset.theme=state.theme;persist('eh:theme:v1',state.theme);render();break;
 case 'toggle-menu':state.mobile=!state.mobile;render();break;
 case 'close-menu':state.mobile=false;render();break;
 case 'toggle-answer':state.revealed[id]=!state.revealed[id];render();break;
 case 'reset-code':delete state.edits[id];render();break;
 case 'copy-code':{const q=qById(id);const code=state.edits[id]??q?.code??'';navigator.clipboard?.writeText(code).then(()=>{const button=document.querySelector(`[data-action="copy-code"]`);if(button)button.textContent='✓ '+t().copied;}).catch(()=>{});break;}
 case 'check-prediction':{const guess=state.drafts[id]||'';state.checks[id]=state.edits[id]!==undefined&&state.edits[id]!==qById(id)?.code?'modified':!strip(guess)?'empty':!(qById(id)?.checkOutput||PREDICTABLE[id])?'unknown':normalizeOutput(guess)===normalizeOutput(qById(id)?.checkOutput||PREDICTABLE[id])?'correct':'wrong';render();break;}
 case 'mark-mastered':setProgress(id,'mastered');break;
 case 'mark-review':setProgress(id,'review');break;
 case 'clear-progress':setProgress(id,'');break;
}}
window.addEventListener('hashchange',()=>render());
document.addEventListener('click',e=>{
 const btn=e.target.closest('[data-action]');if(btn){if(btn.tagName==='BUTTON')e.preventDefault();doAction(btn.dataset.action,btn.dataset.id);}else if(e.target.closest('.sidebar a,.search-overlay a')){state.mobile=false;state.query='';}
});
document.addEventListener('input',e=>{
 if(e.target.id==='search'){state.query=e.target.value;updateSearchDisplay();}
 if(e.target.id==='my-answer'){const r=currentPath();state.drafts[r.id]=e.target.value;}
 if(e.target.id==='code-editor'){const r=currentPath();state.edits[r.id]=e.target.value;}
});
document.addEventListener('change',e=>{if(e.target.id==='topic-select'){state.filter=e.target.value;render();}});
document.addEventListener('keydown',e=>{if(e.key==='/' && !['INPUT','TEXTAREA'].includes(document.activeElement?.tagName)){e.preventDefault();document.getElementById('search')?.focus();}if(e.key==='Escape'){state.query='';updateSearchDisplay();document.getElementById('search')?.blur();if(state.mobile){state.mobile=false;render();}}});
if(!location.hash)location.hash='#/ru/home';else render();
