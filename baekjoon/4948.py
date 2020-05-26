import math

max = 123456 *2
mem = set(range(2,max+1))

for i in range(2,int(math.sqrt(max+1))+1):
  if not i in mem:
    continue
  for j in range(i+i, max+2, i):
    if j in mem:
      mem.remove(j)

n = int(input())
while n != 0:
  result = list(filter(lambda x: x >n and x <=2*n, mem))
  print(len(result))
  n = int(input())
