def partion(arr,start,end):
    pivot=arr[start]
    mark=start
    for i in range(start+1,end+1):
        if arr[i]<pivot:
            mark+=1
            arr[mark],arr[i]=arr[i],arr[mark]
    arr[start]=arr[mark]
    arr[mark]=pivot
    return mark
def quickSort(iList,start,end):
    if start>=end:
        return
    mid=partion(iList,start,end)#分区
    quickSort(iList,start,mid-1)
    quickSort(iList,mid+1,end)
    return iList
print(quickSort([4,3,2,1],0,3))