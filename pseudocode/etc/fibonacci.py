# generator

def fib_generator(a):
   a, b = 0, 1
   while True:
       yield b 
       a, b = b, a+b 
      
fib = fib_generator()
print(next(fib))


# recusive

def fib(a)
  if a in [0,1]:
      return 1
  return fib(a-1) + fib(a-2)
  
