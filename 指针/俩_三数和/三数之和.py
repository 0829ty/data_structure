
def three_sum(nums):
    nums.sort()
    res=[]
    for i in range(len( nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            temp=nums[i]+nums[left]+nums[right]
            if temp>0:
                right-=1
            elif temp<0:
                left+=1
            else:
                # res+=[[nums[i],nums[left],nums[right]]]
                res.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right - 1]:
                    right-=1
                left += 1
                right -= 1
    return  res


print(three_sum([-1,0,1,3,4,5,-2]))
