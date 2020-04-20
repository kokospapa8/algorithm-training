import sys
iter = int(sys.stdin.readline().rstrip())
for _ in range(iter):
  x = sys.stdin.readline()
  a, b = map(int, x.rstrip().split())
  print(a+b)
