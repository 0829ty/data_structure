def removeDuplicated(nums):
    slow = 0
    fast = 0

    while fast < len(nums):

        if nums[fast] == 0:
            fast += 1
        else:# slow占位置,调换fast不同的值,会发生覆盖.快指针发现不同的值后慢指针前进.
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    print(nums, slow + 1)
removeDuplicated([2,0,2,1,3,0,7,1])
