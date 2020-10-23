from typing import List


def partion(nums: List, start, end):
    pivot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < pivot:
            p += 1
        while p <= q and nums[q] >= pivot:
            q -= 1
        if p < q:
            swap(nums, p, q)
    swap(nums, start, q)
    return q


def quick_dan(nums: List, start, end):
    pivot = nums[start]
    mark = start
    for i in range(start + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[i], nums[mark] = nums[mark], nums[i]
    nums[start] = nums[mark]
    nums[mark] = pivot


def quickSort(nums: List, start, end):
    if start >= end:
        return
    mid = partion(nums, start, end)
    quickSort(nums, start, mid - 1)
    quickSort(nums, mid + 1, end)
    return nums


def swap(nums: List, p, q):
    nums[p], nums[q] = nums[q], nums[p]


if __name__ == '__main__':
    iList = []
    # for i in range(7):
    #     iList.append(random.randint(1,7))
    # print(iList)
    # print(quickSort(iList,0,len(iList)-1))
    print(quickSort([3, 6, 7, 2, 1], 0, 4))

