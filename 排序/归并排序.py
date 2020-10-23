from typing import List

from rand import rand1

list1=rand1(9)
# print(list1)
# 拆分数组,只剩一个元素
def merge(left,right):
    arr=[]#接收结果
    while left and right:#当左右列表都存在
        if left[0]>right[0]:#判断俩个列表那个小
            arr.append(right.pop(0))#添加较小的到结果列表中并且弹出首位
        else:
            arr.append(left.pop(0))
    # 当其中一个遍历完后,剩下的在添加到结果列表里
    if left:
        arr.extend(left)
    if right:
        arr.extend(right)
    return arr

def mergeSort(iList: List):
    if len(iList)<=1:
        return iList
    mid=len(iList)>>1#位运算得出中点
    left,right=iList[0:mid],iList[mid:]#分为左右俩个数组
    return merge1(mergeSort(left),mergeSort(right))#递归调用,拆分为单个元素


def merge1(left,right):
    # 传统归并参考俩数组合并代码
#利用分离指针在俩个列表判断
    arr=[]
    l1=0
    r1=0
    # 指针前进直到遍历完俩个列表
    while l1<len(left) and r1<len(right):
        #如果左边的列表值小于右边,添加到新列表里
        if left[l1]<=right[r1]:
            arr.append(left[l1])
            l1+=1
        else:
            arr.append(right[r1])
            r1+=1

    arr.extend(left[l1:])
    arr.extend(right[r1:])
    return arr
print(mergeSort(list1))





