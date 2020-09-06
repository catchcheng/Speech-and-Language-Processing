Group Exercises on Naive Bayes and Sentiment
=======================================
Part 1
------------------
- (1)<br/>
  |V| = 20, n- = 14, n+ = 9<br/>
  prior: P(c=+) = 0.4, P(c=-) = 0.6<br/>
  likelihood: <br/>
  P(and|-) = (2+1)/(14+20) = 3/34
  P(the|+) = (2+1)/(9+20) = 3/29
- (2)<br/>
  P('predictable'|c=+) = 0<br/>
  P('with'|c=+) = 0<br/>
  P('no'|c=+) = 0<br/>
  P('originality'|c=+) = 0<br/>
  P('predictable with no originality'|c=+) = 0<br/>
  P('predictable'|c=-) = 1<br/>
  P('with'|c=+) = 0<br/>
  P('no'|c=+) = 1<br/>
  P('originality'|c=+) = 0<br/>
  P('predictable with no originality'|c=+) = 0<br/>



Chap 4 exercise
=======================================
Part 4.1
------------------
  P('I always like foreign films.'|c=pos)/P('I always like foreign films.'|c=neg) = 0.09*0.07*0.29*0.04*0.08/(0.16*0.06*0.06*0.15*0.11) = 0.615<br/>
  so neg class<br/>
  
Part 4.2
------------------
  |V|= 7, n_comedy = 9, n_action = 11<br/>
  prior: <br/>
  P(c=comedy) = 0.4, P(c=action) = 0.6<br/>
  P(c|'fast, couple, shoot, fly')∝P('fast, couple, shoot, fly'|c)*P(c)<br/>
  =P(fast|c)*P(couple|c)*P(shoot|c)*P(fly|c)*P(c)<br/>
  likelihood: <br/>
  P(fast|c=comedy) = (1+1)/(9+7) = 1/8<br/>
  P(couple|c=comedy) = (2+1)/(9+7) = 3/16<br/>
  P(shoot|c=comedy) = (0+1)/(9+7) = 1/16<br/>
  P(fly|c=comedy) = (1+1)/(9+7) = 1/8<br/>
  P(c=commedy|'fast, couple, shoot, fly')∝1/8*3/16*1/16*1/8*0.4 = 0.000073242<br/>
  P(fast|c=action) = (2+1)/(9+7) = 3/16<br/>
  P(couple|c=action) = (0+1)/(9+7) = 1/16<br/>
  P(shoot|c=action) = (4+1)/(9+7) = 5/16<br/>
  P(fly|c=action) = (1+1)/(9+7) = 1/8<br/>
  P(c=action|'fast, couple, shoot, fly')∝3/16*1/16*5/16*1/8*0.6 = 0.00027465<br/>
  so the 'fast, couple, shoot, fly' is classfied as action
    
Part 4.3
------------------
prior: <br/>
P(c=pos) = 0.4, P(c=neg) = 0.6<br/>
P(c|'A good, good plot and great characters, but poor acting')∝P('A good, good plot and great characters, but poor acting'|c)*P(c) = P(good|c)*P(good|c)*P(great|c)*P(poor|c)*P(c)<br/><br/>
multinomial naive Bayes<br/>
|V| = 3, n_pos = 9, n_neg = 14<br/>
P(good|c=pos) = (3+1)/(9+3) = 1/3<br/>
P(great|c=pos) = (5+1)/(9+3) = 1/2<br/>
P(poor|c=pos) = (1+1)/(9+3) = 1/6<br/>
P(c=pos|'A good, good plot and great characters, but poor acting')∝ 1/3*1/3*1/2*1/6*0.4 = 0.0037<br/>
P(good|c=neg) = (2+1)/(14+3) = 3/17<br/>
P(great|c=neg) = (2+1)/(14+3) = 3/17<br/>
P(poor|c=neg) = (10+1)/(14+3) = 11/17<br/>
P(c=pos|'A good, good plot and great characters, but poor acting')∝ 1/4*1/4*1/4*11/12*0.6 = 0.00213<br/>
so pos class<br/><br/>
binarized naive Bayes<br/>
|V| = 3, n_pos = 4, n_neg = 6<br/>
P(good|c=pos) = (1+1)/(4+3) = 2/7<br/>
P(great|c=pos) = (2+1)/(4+3) = 3/7<br/>
P(poor|c=pos) = (1+1)/(4+3) = 2/7<br/>
P(c=pos|'A good, good plot and great characters, but poor acting')∝ 2/7*2/7*3/7*2/7*0.4 = 0.00399<br/>
P(good|c=neg) = (2+1)/(6+3) = 1/3<br/>
P(great|c=pos) = (1+1)/(6+3) = 2/9<br/>
P(poor|c=pos) = (3+1)/(6+3) = 4/9<br/>
P(c=pos|'A good, good plot and great characters, but poor acting')∝ 1/3*1/3*2/9*4/9*0.6 = 0.00658<br/>
so neg class<br/>
Two models agree.<br/>
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  