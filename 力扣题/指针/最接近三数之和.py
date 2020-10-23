from typing import List


def threenumCloest(num: List,target):
    num.sort()
    # 排序后的三数和最大差值
    min=abs(num[0]+num[1]+num[2]-target)
    res=num[0]+num[1]+num[2]
    for i in range(len(num)-2):
        left=i+1
        right=len(num)-1
        while left<right:
            sum=num[i]+num[left]+num[right]
            if abs(sum-target)<min:
                min=abs(sum-target)
                res=sum
            if sum>target:
                right-=1
            if sum<target:
                left+=1
            else:
                return sum,
    return res,
print(threenumCloest([-1,2,1,-4],1))