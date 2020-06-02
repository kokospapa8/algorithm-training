import math

max = 10000
mem = set(range(2,max+1))

for i in range(2,int(math.sqrt(max+1))+1):
  if not i in mem:
    continue
  for j in range(i+i, max+2, i):
    if j in mem:
      mem.remove(j)

t = int(input())
for _ in range(0,t):
  n = int(input())
  li = list(filter(lambda x: x < n - 1, mem))
  
  # find index where  n//2 
  m = len(li) - 1
  while m > -1:
    if li[m] <= n//2:
      break
    m-=1

  for i in range(m , len(li)+1):
    if n-li[i] in li:
      comp = n-li[i]
      if comp < li[i]:
        print(comp, li[i])
        break
      else:
        print(li[i], comp)
        break
