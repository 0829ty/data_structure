from typing import List
# 插入排序比如扑克牌插入最右边的往左边排好序的牌里插
# 左侧拍好序,右侧无序,每次
# 起手从第一张牌开始插入
def insertort(nums: List)->List:
    if len(nums)<=1:
        return nums
    for right in range(1,len(nums)):#遍历扑克牌从下标为1到结尾
        target=nums[right]#要插入的扑克牌:遍历到的那张牌
        for left in range(0,right):#遍历目标牌左边排好序的牌从0到目标牌
            if nums[left]>target:#如果拍好序的左边牌大于目标牌
                nums[left+1 : right+1]=nums[left : right]#将左边牌大于目标牌的位置到目标牌这一段整体切片后移一位
                nums[left]=target#将目标牌赋值给新位置,插队排好序
                break
    return nums




print(insertort([3,5,7,2,1,8]))

