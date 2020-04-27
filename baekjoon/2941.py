s = input().lower()

arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in arr:
  s = s.replace(a,"*")

print(len(s))
