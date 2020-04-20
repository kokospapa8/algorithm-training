length = int(input())
l = list(map(int, input().split(" ")))

l.sort()
print(int(l[0]), int(l[-1]))
