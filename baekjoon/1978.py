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

'''
list remove is O(n) ops

'''
import math
min, max = map(int,input().split())

mem = set(range(2,max+1))

for i in range(2,int(math.sqrt(max+1))+1):
  if not i in mem:
    continue
  for j in range(i+i, max+2, i):
    if j in mem:
      mem.remove(j)
