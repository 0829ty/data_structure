#数组去重:
from typing import List


def removeDuplicated(nums: List):
    slow=0
    fast=1
    while fast<len(nums):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]
            fast+=1
    return nums
print(removeDuplicated([1,1,3,4]))


#数组移动0

def removeZero(nums: List):
    fast=0
    slow=0
    while fast<len(nums):
        if nums[fast]==0:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1

    for i in range(slow,len(nums)):
        nums[i]=0
    return nums

print(removeZero([1,0,0,7,0,3,5]))

# 删除指定元素:
def remove(nums: List,target):
    slow=0
    fast=0
    while fast<len(nums):
        if nums[fast]==target:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    return nums
print(remove([1,2,0,3,4,0],0))

