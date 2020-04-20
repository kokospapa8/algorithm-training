mul = 1
for _ in range(3):
  mul*= int(input())

mul_str = str(mul)

count_arr=[0] * 10

for i in range(len(mul_str)):
  c = int(mul_str[i])
  count_arr[c]+=1

for x in count_arr:
  print(x)
