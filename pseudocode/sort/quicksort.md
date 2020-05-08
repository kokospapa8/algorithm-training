```
def quicksort(list)
  if length(list) <2)
    return list

  x = pickPivot(list)
  list1 = [y in list where y < x]
  list2 = [x]
  list3 = [y in list where x < y]
  quicksort(list1)
  quicksort(list2)
  return list1 + list2 + list3 
```
 
# Complexity
- avg : O(n log(n))
- worst : O(n^2)

```
- left end or right end. 
  This could give O(n^2) performance depending on the input so this is a bad choice but easiest to implement.
- Best of 3. Left, middle and right. 
  This gives substantially better performance than simply choosing an end in the worst case.
- Random. 
  Choosing a random pivot is fairly easy to implement and guarantees n log n performance so it is a very good choice.
```
