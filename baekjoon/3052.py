count_dict = {}

for _ in range(10):
  index = int(input()) % 42
  count_dict[index]= 1
print(len(count_dict))
