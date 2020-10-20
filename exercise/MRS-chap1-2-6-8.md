Chap 1 exercise
=======================================
Part 1
------------------
- (1.1)<br/>
  new, [1, 4]<br/>
  home, [1, 2, 3, 4]<br/>
  sales, [1, 2, 3, 4]<br/>
  top, [1]<br/>
  rise, [2, 4]<br/>
  in, [2, 3]<br/>
  july, [2, 3, 4]<br/>
  increase, [3]<br/>
  
- (1.2)<br/>
  (a)<br/>
  
|               | 1 | 2 | 3 | 4 |
|---------------|---|---|---|---|
| breakthrough  | 1 | 0 | 0 | 0 |
| drug          | 1 | 1 | 0 | 0 |
| for           | 1 | 0 | 1 | 1 |
| schizophrenia | 1 | 1 | 1 | 1 |
| new           | 0 | 1 | 1 | 1 |
| approach      | 0 | 0 | 1 | 0 |
| treatment     | 0 | 0 | 1 | 0 |
| of            | 0 | 0 | 1 | 0 |
| hopes         | 0 | 0 | 0 | 1 |
| patients      | 0 | 0 | 0 | 1 |

  (b)<br/>
  breakthrough, [1]<br/>
  drug, [1, 2]<br/>
  for, [1, 3, 4]<br/>
  schizophrenia, [1, 2, 3, 4]<br/>
  new, [2, 3, 4]<br/>
  approach, [3]<br/>
  treatment, [3]<br/>
  of, [3]<br/>
  hopes, [4]<br/>
  patients, [4]<br/>

- (1.3)<br/>
  (a)<br/>
  [1, 1, 0, 0]<br/>
  (b)<br/>
  [0, 0, 0, 1]<br/>

Part 2
------------------
- (1.4)<br/>
  (a)<br/>
  O(x+N-y)<br/>
  N, the number of documents<br/>
  (b)<br/>
  O(x+N-y)<br/>
  
- (1.5)<br/>
  Yes, O(max(Brutus_posting, Ceasar_posting)+N-max(Antony_posting Cleopatra_posting))<br/>
  Use The Distributive Law first, first process the one with smaller posting length<br/>
  
- (1.6)<br/>
  (a)<br/>
  Brutus OR Ceasar AND NOT Antony AND NOT Cleopatra<br/>
  (b)<br/>
  NO?<br/>
  (c)<br/>
  It depends on the words and contents of he document collection<br/>
- (1.7)<br/>
  (kaleidoscope OR eyes) AND (tangerine OR trees) AND (marmalade OR skies)<br/>
- (1.8)??<br/>
  N-x<br/>
  N, the number of documents<br/>
- (1.9)??<br/>
  Yes<br/>
- (1.10)<br/>
  add at 8th line after then, ADD(answer, docID(p1))<br/>
  add at 9th line after else, ADD(answer, docID(p2))<br/>
- (1.11)<br/>
  ??<br/>


Chap 2 exercise
=======================================
Part 2
------------------
- (2.8)<br/>
something is happening in New York. University president Dr. Blabla studied ...
- (2.9)<br/>
(a)<br/>
2, 4, 7<br/>
(b)<br/>
4<br/>
- (2.10)<br/>



Chap 6 exercise
=======================================
Part 1
------------------

  
Part 2
------------------
  - (6.8)<br/>
  0<=df<sub>t</sub><=N<br/>
  1<=N/df<sub>t</sub><=N<br/>
  0<=idf<sub>t</sub><=logN<br/>
  so finite<br/>
  - (6.9)<br/>
  0
  - (6.10)<br/>
  tf-idf<sub>car, d1</sub>=tf<sub>car, d1</sub>*idf<sub>car</sub>=27*log(3/3) = 0 = tf-idf<sub>car, d2</sub> = tf-idf<sub>car, d3</sub><br/>
  - (6.11)<br/>
  Yes
  - (6.12)<br/>
  base increases, score decreases
  - (6.13)<br/>
  idf<sub>t</sub> = log<sub>2</sub>N - log<sub>2</sub>df<sub>t</sub>
  