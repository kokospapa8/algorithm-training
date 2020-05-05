a, b, c = map(int, input().split())
z = c-b
if z < 1:
  print(-1)
else: 
  print((a // z)  + 1)
