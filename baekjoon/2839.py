total = int(input())
big = 5
small = 3 

# ret = -1

# if total % big == 0:
#   ret = total // big
# else:
#   if total % small == 0:
#     ret = total // big + (total % big) // small

# if ret > -1:
#   if total % small == 0:
#     ret = total // small
#   else:
#     if total % small == 0:
#       ret = total // small + (total % small) // big

ret = []

for b in range(total//big, 0, -1):

  r = total - (big *b) 
  if r == 0:
    ret.append(b)
    break
  for s in range(r//small, 0, -1):
    if total > b*5+s*3:
      break
    if r % small == 0:
      ret.append(s+b)
      
for s in range(total//small, 0, -1):
  
  r = total - (small *s) 
  if r == 0:
    ret.append(s)
    break
  for b in range(r//big, 0, -1):
    if total > b*5+s*3:
      break
    if r % big == 0:
      ret.append(s+b)

if len(ret) > 0:
  print(min(ret))
else:
  print(-1)
