n = int(input())

arr = []
count= 0

def _calc(n):
  if n < 100:
    return True
  s=list(map(int,str(n)))
  d=s[1]-s[0]
  for i in range(len(s)-1,0,-1):
      if not s[i]-s[i-1]==d:
          return False
  return True

for i in range(1, n+1):
  if _calc(i):
    count+=1
print(count)

