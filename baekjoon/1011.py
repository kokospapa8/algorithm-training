T = int(input())
for _ in range(T):
  start, end = map(int, input().split())

  diff = end - start

  i = 0
  if diff == 1:
    print(1)
  else:
    while diff > 0 :
      i += 1
      diff -= 2*i
      if diff <= 0:
          print(2 * i)
          break
      elif diff <= i+1:
          print(i*2+1)
          break
