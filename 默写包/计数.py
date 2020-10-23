from typing import List


def countSort(nums: List):
    max_data=max(nums)
    count_array=[0]*(max_data+1)
    for i in range(len(nums)):
        count_array[nums[i]]+=1
    sotr_array=[]
    for i in range(len(count_array)):
        for j in range(count_array[i]):
            sotr_array.append(i)
    return sotr_array

print(countSort([4,2,1,8,9,4,6]))