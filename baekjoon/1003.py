turns = int(input())
fib_mem={0:(1,0), 1:(0,1)}

def fib(n):
    if n in fib_mem:
      return fib_mem[n]
    else:
      fib_mem[n] = (fib(n-2)[0] + fib(n-1)[0] , fib(n-2)[1]+ fib(n-1)[1])
      return fib_mem[n]

for _ in range(turns):
    x = int(input())
    ret = fib(x)
    print(fib(x)[0], fib(x)[1])
