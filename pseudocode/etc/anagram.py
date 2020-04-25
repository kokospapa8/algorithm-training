def hash_func(astring):
  s=0
  for one in astring:
    if one in string.whitestapce:
      continue
    s = s + ord(one)
  return s

def is_anagram(w1, w2):
  return hash_func(w1) == hash_func(w2)
  
-----------------------------
from collections import Counter
def is_anagram(s1,s2):
  counter = Counter()
  for c in s1:
     counter[c]+=1
  for c in s2:
     counter[c]-=1
  
  for i in counter.values():
     if i : 
        return False
  return True
