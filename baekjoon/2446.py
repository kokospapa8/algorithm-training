n = int(input())

x = []
for i in range(n):
  a=""
  for j in range(n*2-1):
    if j > (n*2-2-i):
      continue
    if j < i:
      a+=" "       
    else:
      a+="*"
  print(a)

x = list(range(n))[:-1]
x.reverse()

for i in x:
  a=""
  for j in range(n*2-1):
    if j > (n*2-2-i):
      continue
    if j < i:
      a+=" "       
    else:
      a+="*"
  print(a)  
