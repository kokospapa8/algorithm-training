t = int(input())



if t == 1:
  print(1)
else:
  sum = 1
  incr = 6
  i = 2
  
  while True:
    sum += incr
    if sum >= t:
      break
    incr+=6
    i+=1

  print(i)
