length = int(input())
start = "".join(" " for x in range(length))
star = ""
for i in range(1,length+1):
  star=f"{star}*"
  print(f"{start[:-1*i]+star}"[:length])
