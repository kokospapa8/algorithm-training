[solution](https://leetcode.com/problems/subarray-sum-equals-k/solution/)

# nested loop
- O(n**2), space(1)
```
    for i in range(0,len(array)-1):
      sum = 0
      for j in range(i, len(array)):
         sum+=array[j]
         if sum == k:
             count+=1
        
```

# Hashmap
- O(n), space(n)
Use difference between two cumulative sum 
hashmap of (sum, number of occurences)
```
k = <target>
count, sum = 0, 0
        
map = {0:1}
for i in range(0, len(array)):
  sum += array[i]
  if sum - k in map:
      count += map(sum-k)
  map[sum] = map.get(sum,0) + 1
            
```
