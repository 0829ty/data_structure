#buttle
from typing import List


def buttle(l):
    if len(l)<=1:
        return l
    for i in range(1,len(l)):
        flag=False
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+i]=l[j+1],l[j]
                flag=True
        if flag==False:
            break
        print("第%s轮"%(i))
        print(l)
# buttle([1,4,2,7,5])


def select(l):
    if len(l)<=1:
        return l
    for i in range (len(l)-1):
        min_index=i
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]
        print("第%s轮循环" % (i + 1))
        print(l)


def binarySearch(nums: List, val: int): #
    left = 0
    right = len(nums) - 1
    if val==nums[len(nums)-1]:
        return len(nums)-1
    while left <right:
        mid =  (right + left)//2
        if val < nums[mid]:
            right = mid
        elif val > nums[mid]:
            left = mid
        else:
            return mid
# print(binarySearch([1,2,3,4,5,6,7],7))








def binarySearch8(nums: List, val: int,left: int, right: int):
    if right > 0:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            return binarySearch8(nums, val, left, mid-1)
        else:
            return binarySearch8(nums,val,mid+1,right)
    else:
        return -1

def search( nums, target):
    left=-1
    right=len(nums)
    while left<=right:
        mid=(left+right)//2
        if target<nums[mid]:
            right=mid
        elif target>nums[mid]:
            left=mid
        else:
            return mid
# print(search([1,2,3,4,5],5))


