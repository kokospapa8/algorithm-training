import math 
no_case = int(input())
T = []

for _ in range(no_case):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())
  t1 = (x1,y1)
  t2 = (x2,y2)

  euclid_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(t1, t2)]))

  if r2 > r1:
    r1, r2 = r2, r1

  if r1 > euclid_distance or r2 > euclid_distance:
    if t1 == t2 and r1 == r2:
      print(-1)
    else:   
      if euclid_distance + r2 < r1:
        print(0)
      elif euclid_distance + r2 == r1:
        print(1)
      elif euclid_distance + r2 > r1:
        print(2)

  else:
    if euclid_distance - r1 > r2:
      print(0)
    elif euclid_distance - r1 == r2:
      print(1)
    elif euclid_distance - r1 < r2:
      print(2)
