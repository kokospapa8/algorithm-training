x = []
for _ in range(5):
  x.append(int(input()))
h = x[:3]
d = x[3:5]

h.sort()
d.sort()
print(h[0]+d[0]-50)
