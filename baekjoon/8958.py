num = int(input())

for _ in range(num):
  quiz = input()

  incr = 0
  score = 0
  
  for i in quiz:
    if i == "O":
      incr+=1
      score+=incr
    else:
      incr = 0
  print(score)

