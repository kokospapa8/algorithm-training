t = int(input())
for i in range(t):
  num, s = input().split()
  ret = ""
  for c in s:
    ret+=c*int(num)
  print(ret)
