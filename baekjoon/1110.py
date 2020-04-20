x = int(input())
i=0
y = x
while(1):
  if y < 10:
    y = y*10 + y
  else:
    z = int(y/10) + y%10
    y = (y%10)* 10 + z % 10
  i+=1
  if x == y:
    break
print(i)
