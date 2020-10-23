# 数组面试题:删除指定元素.移动0.删除重复项.删除重复项2
from typing import List

# 删除指定元素
def remove_point(nums,data):
    fast=0
    slow=0
    while fast < len (nums):
        if nums[fast]==data:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    print(nums)

# remove_point([0,1,2,3,3,5],1)
# 移动零
def move_zero(nums):
    fast=0
    slow=0
    while fast < len (nums):
        if nums[fast]==0:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    for i in range(slow,len(nums)):
        nums[i]=0
    print(nums)

# move_zero([1,0,0,6,7,0])

# 去重

def remove_duplicates(nums):
    slow=0
    fast=1
    while fast<len(nums):
        if nums[fast]==nums[slow]:
            fast+=1
        else:
         slow+=1
         nums[slow]=nums[fast]
         fast+=1
    print(nums)
# remove([1,1,1,2,3,3,5])
def remove_duplicated(nums:List):
    slow=0
    fast=1
    # 计数器,
    count=1
    while fast<len(nums):
        if nums[fast]==nums[slow]:
            count+=1
            if count==2:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]
            fast+=1
            count=1
    print(nums)
    return nums
# print(remove_twonum([1,1,1,2,2,3,3,3,4]))
