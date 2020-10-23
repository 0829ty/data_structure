from typing import List


def bucketSort(arr: List):
    max_data=max(arr)
    min_data=min(arr)
    d=max_data-min_data#间距
    #1,初始化桶
    bucket_num=len(arr)#桶的个数为数组元素个数
    count_array=[]#空桶[]
    for i in range(bucket_num):
        count_array.append([])#造桶[[],[],[],[],[]]

    # 2.* 定位元素在哪个桶
    for i in range (len(arr)):
        num=int((arr[i]-min_data)/d*(bucket_num-1))
        bucket=count_array[num]
        bucket.append(arr[i])
    #桶内部排序
    for i in range (len(count_array)):
        count_array[i].sort()
    # print(count_array)
    #按照顺序输出
    sort_array=[]
    for sub in count_array:
        for item in sub:
            sort_array.append(item)
    return sort_array
if __name__ == '__main__':
    print(bucketSort([4.5,0.5,0.8,2.7,3.5]))