def two_sum(nums: list ,target):#对撞指针(O(nlogn),返回值而不是下标
    right=len(nums)-1
    left=0
    while left<right:
        sum_two=nums[right]+nums[left]
        if sum_two==target:
            print(nums[left],nums[right])
            left+=1
            right-=1
        elif sum_two<target:
            left+=1
        else:
            right-=1


def two1_sum(nums : list,target):
    # 借用空间,时间复杂度On,空间复杂度大,时间最短
#     字典收集遍历的值和下标
    dic={}
#     遍历数组下标
    for i in range(len(nums)):
#         差值
        cha=target-nums[i]
        # 判断差值是否在字典里
        if cha not in dic:
            # 不存在则把遍历 的值和下标存在字典里
            dic[nums[i]]=i
        else:
            # 打印
            print(i,dic[cha])


def two2_sum(nums,target):#(O(n2)
    # 外层循环下标到倒数第二位
    for i in range(len(nums)-1):
        # 内层循环下标从i+1到末尾
        for j in range(i+1,len(nums)):
            # 判断和是否等于目标
            if nums[i]+nums[j]==target:
                return [i,j]

print(two2_sum([1,2,3,4,5],6))
