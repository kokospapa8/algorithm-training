l, x = map(int, input().split())
arr = list(map(int, input().split()))
b = []
for a in arr:
  if a < x:
    b.append(a)

print(*b)
