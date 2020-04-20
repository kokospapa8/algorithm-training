x= []
for _ in range(5):
  x.append(int(input()))
def fail(score):
  return score if x > 40 else 40
x = [40 if i<40 else i for i in x]
print(int(sum(x)/len(x)))
