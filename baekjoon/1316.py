from collections import Counter
import re
t = int(input())

count = 0

for _ in range(t):
  s = input()
  sub = re.sub(r"(.)\1{1,}", r"\1", s)
  l_sub = Counter(list(sub))

  is_conseq = True
  for k, v in l_sub.items():
    if v > 1: 
      is_conseq = False
      
  count += 1 if is_conseq else 0

print(count)
