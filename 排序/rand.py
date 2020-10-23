import random
# 不去重随机数
def rand1(n):
    list=[]
    for i in range (n):
        a=random.randint(0,10)
        list.append(a)
    return list
# print(rand1(5))

# 去重随机数

def ran(n):
    a=[]
    while len(a)<10:
        b=random.randint(0,10)
        if b not in a:
            a.append(b)
    print(a)
