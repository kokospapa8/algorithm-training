n = int(input())

star = ""
#expensive append
for _ in range(n):
    star+="*"

for i in range(1,n+1):
    print(star[:i])

for i in range(1,n):
    print(star[:-1*i])
