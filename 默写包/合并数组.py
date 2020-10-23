# 其中一个数组无限长,将在这个数组上进行合并
def merge(list1, m, list2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if list1[i] >= list2[j]:
            list1[k] = list1[i]
            i -= 1
        else:
            list1[k] = list2[j]
            j -= 1
        k -= 1
    while i >= 0:
        list1[k] = list1[i]
        k -= 1
        i -= 1
    while j >= 0:
        list1[k] = list2[j]
        k -= 1
        j -= 1

    return list1


print(merge([1, 3, 5, 6, 0, 0, 0], 4, [2, 7, 8], 3))
