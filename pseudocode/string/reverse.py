# recursive
# s is array of string
def reverse_recurse(s):
  if s:
    s = s[-1]+reverse(s[:-1])
  return s
  
# pythonic
def reverse(s):
  return s[::-1]
