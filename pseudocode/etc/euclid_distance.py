import math 
t1 = (0,0,0)
t2 = (3,4,5)
euclid_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(t1, t2)]))
