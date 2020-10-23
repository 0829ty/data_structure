from typing import List

from rand import rand1

list1=rand1(10)
# def xuanze(a):
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     print(a)
# # xuanze(ran())
# xuanze([1,2,4,5,7,6])
def active_sort(n: List):
    if len(n)<=1:
        return n
    for i in range(len(n)-1):
        minindex=i
        for j in range(i+1,len(n)):
            if n[j]<n[minindex]:
                minindex=j
        n[i],n[minindex]=n[minindex],n[i]
        print("第%s轮循环"%(i+1))
        print(n)
if __name__ == '__main__':
    # active_sort(list1)
    active_sort([7,82,78,97,49,12,84,14,59,13])

