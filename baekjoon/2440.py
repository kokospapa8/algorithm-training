length =int(input())
start = "".join("*" for x in range(length+1))
for i in range(1,length+1):
    print(f"{start[:-1*i]}"[:length])
