import math
min, max = map(int,input().split())

mem = set(range(2,max+1))

for i in range(2,int(math.sqrt(max+1))+1):
  if not i in mem:
    continue
  for j in range(i+i, max+2, i):
    if j in mem:
      mem.remove(j)

result = list(filter(lambda x: x >= min, mem))
for i in result:
  print(i)
