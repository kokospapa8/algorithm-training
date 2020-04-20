i = 1
maxi = 0
max = 0
for _ in range(9):
  j = int(input())
  if j > max:
    max = j
    maxi = i
  i+=1

print(max)
print(maxi)
