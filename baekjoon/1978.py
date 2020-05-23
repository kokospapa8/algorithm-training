T = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
mem = list(range(2,max_num+1))
iter_list = list(range(2,max_num+1))


def check_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in iter_list:
  if not i in mem:
    continue
  #find prime
  if check_prime(i):
    #remove all multiple of prime
    for j in range(i+i,max_num+1, i):
      if j in mem:
        mem.remove(j)
print(len(set(arr).intersection(set(mem))))
