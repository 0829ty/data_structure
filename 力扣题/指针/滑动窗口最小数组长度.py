from typing import List


def min_list(num: List[int],s : int):
    num.sort()#排序从小到大
    left=0
    left=0
    minlen=1
    cursom=0
    for right in range (len(num)):
        cursom+=right
        while cursom>=s:
            minlen=min(minlen,right-left+1)
            cursom=cursom-num[left]
            left+=1



"""在一个坐标上存在俩个指针,left 和right
left是窗口的左边框,right是窗口的有边框俩个都分别向右移动.前者使窗口的和减少.后者使窗口的
和增大.开始俩个指针重合
开始时right向右滑动,使和变大]
当恰好>=s时,记录"""
def minSubArrayLenl(s: int ,nums: List[int])->int:
#     初始化
    left, sum , res=0,0,float("inf")
#     有指针右移动
    for right in range(len(nums)):
        sum+=nums[right]
        while sum>res:
            if right- left+1<res:
                res=right-left+1

            sum-=nums[left]
            left+=1
    return 0 if res==float("inf") else res

