# 快速查找
import random
from typing import List
from rand import rand1


def swap(iList, p, q):#数字的交换
    iList[p],iList[q]=iList[q],iList[p]


def partion(iList: List,start, end):
    pivot=iList[start]
    p=start+1
    q=end
    while p<=q:#当俩个指针对撞时,等于后在走一步出来

        while p<=q and iList[p]<pivot:#p指针寻找比start值大的元素
            p+=1
        while p<=q and iList[q]>=pivot:#q指针从尾部到中间寻找比start大的元素
            q-=1
        if p<q:#找到后交换p和q的值
            swap(iList,p,q)
    swap(iList,start,q)#最后交换开始值与q的值因为q比start小
    return q# 返回q为mid


def quickSort(iList,start,end):
    if start>=end:
        return
    mid=partion(iList,start,end)#分区
    quickSort(iList,start,mid-1)
    quickSort(iList,mid+1,end)
    return iList
if __name__ == '__main__':
    iList=[]
    for i in range(7):
        iList.append(random.randint(1,7))
    print(iList)
    print(quickSort(iList,0,len(iList)-1))
    print(quickSort([3,6,7,2,1],0,4))