import string
s = input()

result={}
i = 0 

for c in list(s):
  if not c in result:
    result[c] = i
  i+=1

ret = ""
for c in list(string.ascii_lowercase):
  if c in result:
    ret+=f"{result[c]} "
  else:
    ret+="-1 "

print(ret)
