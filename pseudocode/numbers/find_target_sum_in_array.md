# 2 numbers
## brute force
n**2
## use hash
## walk inside 


# 3 numbers


# triplet
## bruteforce
time - n***3
```
for i in range(i, len-2):
    for j in range(i+1, len-1):
        for k in range(j+1, len)
           if sum == 0:
              print(val[i,j,k])
              
```
## use hash
time - n**2
space - n 
```
for i in range(n - 1): 
  for j in range(i + 1, n): 
    x = -(val_i + val_j) 
      if x in dict: 
        print(x, val_i, val_j) 
      else: 
        s.add(arr[j]) 
    
```
## walk inside
time - n**2
space - 1
```
arr.sort()
for i in range(0, n-1): 
    l = i + 1
    r = n - 1
    x = arr[i] 
    while (l < r): 
      if (x + arr[l] + arr[r] == 0): 
            # print elements if it's sum is zero 
            print(x, arr[l], arr[r]) 
             l+=1
             r-=1
       elif (x + arr[l] + arr[r] < 0): 
           l+=1
  
       else: 
           r-=1
 ```
