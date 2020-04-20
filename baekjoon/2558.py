a = int(input())
b = int(input())

b1 = b % 10
b2 = b % 100 - b1
b3 = int(b/100)
print(a*b1)
print(int(a*b2/10))
print(a*b3)
print(a*b)
