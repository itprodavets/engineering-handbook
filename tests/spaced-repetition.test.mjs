import test from 'node:test';
import assert from 'node:assert/strict';
import {gradeCard, selectCardQueue, nextIntervalDays, linkedUnitForQuestion, moduleOutline, unitView, cardsView} from '../site/assets/learning.js';

const questions = Array.from({length:35}, (_,i)=>({
  id:'Q-'+String(i+1).padStart(3,'0'),
  lesson:i<8?'async-lifecycle':'threadpool-scheduling',
  question:'Question '+(i+1), answer:'Reference '+(i+1), code:''
}));

test('new cards are capped at ten per local calendar day',()=>{
  const initial=selectCardQueue(questions,{},Date.UTC(2026,9,31,10));
  assert.equal(initial.newCount,10);
  assert.equal(initial.current.id,'Q-001');
  let history={};
  for(let i=0;i<10;i++)history=gradeCard(history,questions[i].id,true,Date.UTC(2026,9,31,10));
  const after=selectCardQueue(questions,history,Date.UTC(2026,9,31,10,1));
  assert.equal(after.newCount,0);
  assert.equal(after.current,null);
  assert.equal(after.remainingNew,25);
});

test('unknown answer comes back after exactly ten minutes',()=>{
 const now=Date.UTC(2026,9,31,10);
 const history=gradeCard({},'Q-001',false,now);
 assert.equal(history['Q-001'].dueAt-now,10*60*1000);
 assert.equal(history['Q-001'].streak,0);
 assert.equal(history['Q-001'].lapses,1);
 assert.equal(selectCardQueue([questions[0]],history,now+9*60*1000).dueCount,0);
 assert.equal(selectCardQueue([questions[0]],history,now+10*60*1000).dueCount,1);
});

test('consecutive known answers follow spaced intervals 1, 3, 7, 14, 30 days',()=>{
 let history={};
 let now=Date.UTC(2026,9,31,10);
 for(const days of [1,3,7,14,30]){
  assert.equal(nextIntervalDays(history['Q-001']),days);
  history=gradeCard(history,'Q-001',true,now);
  assert.equal(history['Q-001'].dueAt-now,days*24*60*60*1000);
  now=history['Q-001'].dueAt;
 }
});

test('a failed answer resets learning streak and counts a lapse',()=>{
 let h=gradeCard({},'Q-001',true,Date.UTC(2026,9,31));
 h=gradeCard(h,'Q-001',false,Date.UTC(2026,10,1));
 assert.equal(h['Q-001'].streak,0);
 assert.equal(h['Q-001'].lapses,1);
 assert.equal(nextIntervalDays(h['Q-001']),1);
});

test('due cards take precedence over new cards',()=>{
 const now=Date.UTC(2026,9,31,10);
 let h=gradeCard({},'Q-002',false,now-11*60*1000);
 const queue=selectCardQueue(questions,h,now);
 assert.equal(queue.current.id,'Q-002');
});

test('question belongs to one deep learning unit',()=>{
 const units=[{id:'example',lesson:'async-lifecycle',questions:[1,2],title:{ru:'Пример',en:'Example'}}];
 assert.equal(linkedUnitForQuestion(units,'Q-002')?.id,'example');
 assert.equal(linkedUnitForQuestion(units,'Q-020'),null);
});

test('rendered cards escape user content and show grades only after flip',()=>{
 const qs=[{id:'Q-001',question:'Can <script> run?',answer:'No, & escaped',code:'',lesson:'async-lifecycle'}];
 const ctx={lang:'en',questions:qs,units:[],history:{},href:(p,id)=>'#/'+p+'/'+id,now:Date.UTC(2026,9,31)};
 const hidden=cardsView({...ctx,flipped:false});
 assert.ok(!hidden.includes('No, & escaped'));
 assert.ok(hidden.includes('&lt;script&gt;'));
 assert.ok(!hidden.includes('data-action="card-grade"'));
 const revealed=cardsView({...ctx,flipped:true});
 assert.ok(revealed.includes('No, &amp; escaped'));
 assert.ok(revealed.includes('data-action="card-grade"'));
});

test('module and unit rendering preserve bilingual navigation',()=>{
 const unit={
 id:'one',lesson:'l1',level:'fundamentals',
 title:{ru:'Потоки',en:'Threads'},
 goal:{ru:'Понять',en:'Understand'},definition:{ru:'Текст',en:'Text'},
 steps:[{ru:'Шаг',en:'Step'}],
 resources:{ru:'Стек',en:'Stack'},pitfalls:{ru:'Гонка',en:'Race'},
 code:'Console.Write("Hi");',questions:[1],refs:[]
 };
 const href=(section,id)=>'#/'+section+'/'+id;
 const outline=moduleOutline({id:'l1'},[unit],'en',{},href);
 assert.ok(outline.includes('Threads'));
 assert.ok(outline.includes('#/unit/one'));
 const page=unitView(unit,{lang:'ru',units:[unit],questions:[questions[0]],unitProgress:{},href});
 assert.ok(page.includes('Потоки'));
 assert.ok(!page.includes('Threads'));
});
