t = int(input())

sum = 1
i = 1 
if t ==1:
  print("1/1")
else:

  while sum < t:
    i+=1
    sum+=i
    
  diff = sum - t # 1
  if i % 2 == 0:
    print(f"{i-diff}/{1+diff}")
  else:
    print(f"{1+diff}/{i-diff}")
