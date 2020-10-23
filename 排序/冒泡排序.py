from typing import List
from rand import rand1
list1=rand1(10)

def bubblesort(l:List[int]):
    # 冒泡排序,从小到大
    if len(l)<=1:
        return l
    for i in range(1,len(l)):#外层控制了循环次数
        flag=False
        for  j in range(len(l)-i):#内层负责交换的数据
            if l[j] > l[j + 1]:  # 判断是否大于下一个
                l[j],l[j+1]=l[j+1],l[j]
                flag=True
        if flag==False:
            break
        print("第%s轮排序结果为"%(i))
        print(l)
    # return l

if __name__ == '__main__':
    bubblesort(list1)

