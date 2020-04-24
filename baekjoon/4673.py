def _sequence_calc(n):
  num_array = [int(x) for x in str(n)]
  return n + sum(num_array)

numbers = []
max = 10000
i = 1
while i < max:
  numbers.append(_sequence_calc(i))
  i+=1  
l = list(set(range(1, max))-set(numbers))
l.sort()
for i in l:
  print(i)
