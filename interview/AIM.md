# questions
Each question was given 5min

## Q1
```
Given : def rand_7 => random(1~7), create rand_5.
=> rand_7 mod 5 # This is not uniformly distributed
=> 
```
## Q2
``` find random_7 from random_5
=> random_5 + (2 mod random_5 ) # this is not uniformly distributed
=> ( 7 * random_5 ) mod 7 +1 # this is not uniformly distributed solution 

### use accept and reject 
i=0;
while(i > 21):
  i = 5 * (rand5() - 1) + rand5();  // i is now uniformly random between 1 and 25 
// i is now uniformly random between 1 and 21
return i % 7 + 1; 
```
## Q3
```
Given set of elements with following rules, elements are grouped in consecutive elements
[1,2,3] [7,8] [12,13,14]
if new set of elements are introduced, new array is formed 
for example 
introducing [3,4,6] will result 
[1,2,3,4] [6,7,8] [12,13,14]

=> append all together O(n)
=> make set to remove redundant elements (*this is not needed but at the time of the interview I thought this was needed)
=> sort all O(nlogn)
=> given two pointer, Head, head+1, traverse and append array, 
     if Head , Head+1 are not consecutive, create new array, 
     if Head, Head+1 are same, continue,



```
