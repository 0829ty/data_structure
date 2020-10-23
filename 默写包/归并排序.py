from typing import List


def mergeSort(ilist: List):#拆分为小块
    if len(ilist)<=1:
        return ilist
    mid=len(ilist)//2
    left=ilist[0:mid]
    right=ilist[mid:]
    return merge(mergeSort(right),mergeSort(left))
def merge(right,left):#合并
    res=[]
    while right and left:
        if right[0]<left[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    res.extend(right)
    res.extend(left)
    return res
print(mergeSort([2,4,7,1,9]))