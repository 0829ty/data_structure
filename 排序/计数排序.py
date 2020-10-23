from typing import List
from rand import rand1

# print(rand1(16))

def countSort(nums: List):
    max_data=max(nums)
    count_arr=[0]*(max_data+1)
    for i in range (len(nums)):
        count_arr[nums[i]]+=1
    sort_arr=[]
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sort_arr.append(i)
    return sort_arr
print(countSort([2,1,4,7,9,0,3,5]))

