s = int(input())

def fact(n):
  if n in [0,1]:
    return 1
  return n * fact(n-1)

print(fact(s))
