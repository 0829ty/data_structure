# 合并有序数组
import sys
from typing import List

nums1=[1, 5, 6,3,0,0,0]
def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1  # 控制输出的数组大小
    # 倒着遍历
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        elif nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


# 翻转
def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


print(reverse([1, 2, 3, 4, 5]))


def binarySearch(nums: List, val: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if val == nums[left]:
            return left
        elif val == nums[right]:
            return right
        else:
            mid = (left + right) // 2
            if val < nums[mid]:
                right = mid
            elif val > nums[mid]:
                left = mid
            else:
                return mid


def binarySearch2(nums: List, val: int):
    left = -1
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if val < nums[mid]:
            right = mid
        elif val > nums[mid]:
            left = mid
        else:
            return mid


def binarySearch3(nums: List, val: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 适用于其他编程语言
        if val < nums[mid]:
            right = mid
        elif val > nums[mid]:
            left = mid
        else:
            return mid


print(binarySearch3([1, 2, 3, 4, 5, 6], 4,))
# 递归版


def binarySearch4(nums: List, val: int, left: int, right: int):
    if right > 0:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            return binarySearch4(nums, val, left, mid - 1)
        else:
            return binarySearch4(nums, val, mid + 1, right)
    else:
        return -1

# arr = list(range(30))
# target = 10
# print(binarySearch4(arr,target,0,len(arr)))
