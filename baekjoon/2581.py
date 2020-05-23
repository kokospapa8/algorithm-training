min = int(input())
max = int(input())


mem = list(range(2,max+1))

def check_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in range(2,max+1):
  if not i in mem:
    continue
  #find prime
  if check_prime(i):
    #remove all multiple of prime
    for j in range(i+i,max+1, i):
      if j in mem:
        mem.remove(j)

result = list(filter(lambda x: x in mem, range(min, max+1)))
if len(result) > 0:
  print(sum(result))
  print(result[0])
else:
  print(-1)
