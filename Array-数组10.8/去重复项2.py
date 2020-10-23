# 80. 删除排序数组中的重复项 II
def remove(nums):
    slow=0
    fast=1
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

    print(slow+1,nums)

remove([1,1,1,2,2,3])

