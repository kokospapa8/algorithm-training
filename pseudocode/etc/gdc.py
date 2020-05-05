# x % y == 0 , return y
# x % y !=0 , x <=y, y<= (x%y) repeat

def gcd 
  if x > y:
    y,x =x,y

  while y > 0:
    r = x%y
    x = y
    y = r
  return y
