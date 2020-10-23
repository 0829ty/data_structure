# 1.归并排序
from typing import List


def mergeSort(nums: List):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left,right=nums[0:mid],nums[mid:]
    return merge1(mergeSort(left),mergeSort(right))

def merge(left,right):
    res=[]
    while left and right:
        if left[0]<right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res
def merge1(left,right):
    res=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
# def merge1(left,right):
#     # 传统归并参考俩数组合并代码
#
#     arr=[]
#     l1=0
#     r1=0
#     while l1<len(left) and r1<len(right):
#         if left[l1]<=right[r1]:
#             arr.append(left[l1])
#             l1+=1
#         else:
#             arr.append(right[r1])
#             r1+=1
#
#     arr.extend(left[l1:])
#     arr.extend(right[r1:])
#     return arr



# 快速排序
def swap(nums: List ,p,q):
    nums[q],nums[p]=nums[p],nums[q]
def quickSort(nums:List,start,end):
    if start>=end:
        return
    mid=partion(nums,start,end)
    quickSort(nums,start,mid-1)
    quickSort(nums,mid+1,end)
    return nums
def partion(nums,start,end):
    privo=nums[start]
    p=start+1
    q=end
    while p<=q:
        while p<=q and nums[p]<privo:
            p+=1
        while p<=q and nums[q]>privo:
            q-=1
        if p<q:
            swap(nums,p,q)
    swap(nums,start,q)
    return q

if __name__ == '__main__':
    # print(mergeSort([2,4,1,7,4,5]))
    print(quickSort([4,7,3,5,6,2,3,1],0,7))