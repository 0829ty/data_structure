from typing import List
def triangle(nums: List):
    nums.sort(reverse=True)
    # nums.remove(0)
    res=[]
    count=0
    for  i in range(len(nums)-2):
        right=len(nums)-1
        left=i+1
        while left<right:
            # if nums[right] == 0:
            #     right-=1
            sum=nums[left]+nums[right]
            if sum>nums[i]:
                count+=1
                res.append([nums[i],nums[left],nums[right]])
                right-=1
            else:
                left+=1
    return res,count

print(triangle([9,8,5,4,3]))


# 正确的
def trianglenumber(nums: List[int]):
    nums.sort()
    count=0
    for i in range(2,len(nums)):
        left=0
        right=i-1
        while left<right:
            if nums[left]+nums[right]>nums[i]:
                count+=right-left
                right-=1
            else:
                left+=1
    return count

# print(trianglenumber([1,1,1,0]))