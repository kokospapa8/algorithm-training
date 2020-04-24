
n = int(input())

arr = []
count= 99

def _calc(n):
  s=list(map(int,str(n)))
  d=s[1]-s[0]
  for i in range(len(s)-1,0,-1):
      if not s[i]-s[i-1]==d:
          return False
  return True

for i in range(111, n+1):
  if _calc(i):
    count+=1
print(count)

