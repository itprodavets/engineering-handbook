import test from 'node:test';
import assert from 'node:assert/strict';
import {gradeMastery,masterySummary,masteryReviewCards,activeReviewQuestions,assessmentPanel,unitView} from '../site/assets/learning.js';

const unit={
 id:'async-state-machine',lesson:'async-lifecycle',level:'internals',
 title:{ru:'Машина состояний',en:'State machine'},
 goal:{ru:'Понять',en:'Understand'},
 definition:{ru:'Определение',en:'Definition'},
 steps:[{ru:'Шаг 1',en:'Step 1'}],
 resources:{ru:'Память',en:'Memory'},pitfalls:{ru:'Риск',en:'Risk'},
 chapters:[{id:'move',title:{ru:'MoveNext',en:'MoveNext'},body:{ru:'Шаг и IL',en:'Step and IL'},code:'await Task.CompletedTask;'}],
 checks:['recall','explain','predict','diagnose','design'].map(level=>({
  level,prompt:{ru:'Вопрос '+level,en:'Question '+level},
  rubric:{ru:'Ответ '+level,en:'Answer '+level}
 })),
 questions:[12],refs:[],labFiles:['labs/dotnet/Q-024.cs']
};
const question={id:'Q-012',lesson:'async-lifecycle',question:'Why?',answer:'Because',code:''};
const href=(s,id='')=>'#/'+s+'/'+id;

test('five-level mastery records self-ratings without mutating input',()=>{
 const original={};
 const newer=gradeMastery(original,unit.id,'recall',2,111);
 assert.deepEqual(original,{});
 assert.equal(newer[unit.id].recall.grade,2);
 assert.equal(newer[unit.id].recall.at,111);
 assert.deepEqual(masterySummary(newer,unit.id),{answered:1,confident:1,partial:0,weak:0});
 const later=gradeMastery(newer,unit.id,'explain',0,222);
 assert.deepEqual(masterySummary(later,unit.id),{answered:2,confident:1,partial:0,weak:1});
 assert.throws(()=>gradeMastery({},unit.id,'invalid',1));
 assert.throws(()=>gradeMastery({},unit.id,'recall',3));
});

test('rubrics remain hidden before the reveal action',()=>{
 const hidden=assessmentPanel(unit,{lang:'ru'});
 assert.ok(hidden.includes('Вопрос recall'));
 assert.ok(!hidden.includes('Ответ recall'));
 assert.ok(!hidden.includes('data-action="mastery-grade"'));
 const shown=assessmentPanel(unit,{lang:'ru',revealed:{'async-state-machine:recall':true}});
 assert.ok(shown.includes('Ответ recall'));
 assert.ok(shown.includes('data-action="mastery-grade"'));
});

test('unit deep sections and labs are visible and localized',()=>{
 const html=unitView(unit,{lang:'en',units:[unit],questions:[question],unitProgress:{},href});
 assert.ok(html.includes('Question recall'));
 assert.ok(html.includes('Step and IL'));
 assert.ok(html.includes('labs/dotnet/Q-024.cs'));
 assert.ok(!html.includes('Вопрос recall'));
 assert.ok(html.includes('Answer criteria')===false); // remains hidden
});

test('weak mastery check enters spaced review as a synthetic card',()=>{
 const srs={'M:async-state-machine:explain':{dueAt:123,streak:0}};
 const cards=masteryReviewCards([unit],srs,'en');
 assert.equal(cards.length,1);
 assert.equal(cards[0].id,'M:async-state-machine:explain');
 assert.equal(cards[0].question,'Question explain');
 assert.equal(cards[0].answer,'Answer explain');
});

test('new cards only unlock after studying, old reviews remain accessible',()=>{
 let pool=activeReviewQuestions([question],[unit],{}, {},'en');
 assert.equal(pool.length,0);
 pool=activeReviewQuestions([question],[unit],{[unit.id]:{at:'now'}}, {},'en');
 assert.deepEqual(pool.map(x=>x.id),['Q-012']);
 pool=activeReviewQuestions([question],[unit],{}, {'Q-012':{dueAt:123}},'en');
 assert.deepEqual(pool.map(x=>x.id),['Q-012']);
});

test('synthetic review cards render correctly without duplicating theory',()=>{
 const srs={'M:async-state-machine:recall':{dueAt:12,streak:0}};
 const cards=activeReviewQuestions([],[unit],{},srs,'ru');
 assert.equal(cards.length,1);
 assert.equal(cards[0].answer,'Ответ recall');
});
