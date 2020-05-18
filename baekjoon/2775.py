'''
# recusion too long 

t = int(input())
for _ in range(0,t):
  k = int(input())
  n = int(input()) 

  def low_sum(k,n):
    # if zero no need to recurse
    if k == 0:
      return n
    # first unit is always 1
    if n == 1: 
      return 1 
    return low_sum(k-1, n) + low_sum(k, n-1)

  print(low_sum(k,n))
'''

# memoization
global mem

mem = {}

for k in range(0,14):
  mem[(k,1)] = 1

for n in range(1,15):
  mem[(0,n)] = n

t = int(input())

for _ in range(0,t):
  k = int(input())
  n = int(input()) 

  def low_sum(k,n):
    # if zero no need to recurse
    if (k,n) in mem:
      return mem[(k,n)]

    if k == 0:
      mem[(0,1)] = n
      return n

    if n == 1: 
      mem[(k,1)] = 1
      return 1 

    sum=low_sum(k-1, n) + low_sum(k, n-1)
    mem[(k,n)]=sum
    return sum
  print(low_sum(k,n))
