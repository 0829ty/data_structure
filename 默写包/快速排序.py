from typing import List

def swap(iList,p,q):
    iList[p],iList[q]=iList[q],iList[p]

def partion(iList, start, end):
    prevot=iList[start]
    p=start+1
    q=end
    while p <=q:
        while p<=q and iList[p]<prevot:
            p+=1
        while p<=q and iList[q]>prevot:
            q-=1
        if p<q:
            swap(iList,p,q)
    swap(iList,start,q)
    return q


def quickSort(iList: List,start,end):
    if start>=end:
        return
    mid=partion(iList,start,end)
    quickSort(iList,start,mid-1)
    quickSort(iList,mid+1,end)
    return iList

print(quickSort([4,1,3,7,2,9],0,5))


