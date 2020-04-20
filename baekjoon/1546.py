num = int(input())
l = list(map(int, input().split()))
m = max(l)

print(sum(l) * 100 / m / num)
