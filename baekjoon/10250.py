t = int(input())
for _ in range(0,t):
  H, W, N = map(int, input().split())

  r = (N // H) +1
  f = N % H
  if f == 0:
    f = H
    r-=1
  if r < 10:
    print(f"{f}0{r}")
  else:
    print(f"{f}{r}")

