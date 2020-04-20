n = int(input())
even = (n % 2 == 0)
for _ in range(n):

  for i in (0,1):    
    a =""
    for j in range(n):
      if j % 2 == i:
        a+="*"
      elif j != n-1:
        a+=" "
    print(a)
