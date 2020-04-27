s = input()

from collections import Counter
c = Counter(s.lower())


ret = "?"
max = 0


for k, v in dict(c).items():
  if v > max:
    max = v
    ret = k
  elif v == max:
    ret = "?"

print(ret.upper() if ret != "?" else "?")
