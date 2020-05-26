'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all
unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

input: [-1,0,1,2,-1,-4]
output: [
  [-1,0,1], [-1,-1,2]
]

test set
[0,0,0,0,0,0]
[0,1,-1]
[0]
[]
[-8,-1,0,0,0,0,0,1,2,-1,-4]
'''


result = set()

#input - input number with space inbetween
input_array = list(map(int,input().split()))
# input_array =[-1,0,1,2,-1,-4]
len_array = len(input_array)
input_array.sort() 

# print(input_array)


for i in range(0, len_array-2):
  left = i + 1
  right = len_array-1

  while(left < right):
    sum = input_array[i]+input_array[left]+input_array[right]

    if sum < 0:
      left+=1
    elif sum > 0: 
      right-=1
    else:
      result.add((input_array[i],input_array[left],input_array[right]))
      break;

#convert result to set
ret = []
for s in result:
  ret.append(list(s))
print(ret)
