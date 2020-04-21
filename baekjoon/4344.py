num = int(input())

for _ in range(num):
  score = list(map(int, input().split()))
  count = score[0]
  total = sum(score[1:])
  avg = int(total/count)
  above = list(filter(lambda x: x > avg, score[1:]))

  print("%.3f" % (len(above)/count* 100)+"%")

