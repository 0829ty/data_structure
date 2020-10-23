def aaa(n):
    i=0

    while n!=0:
        n=n&(n-1)
        i+=1
    print(i)

# aaa(9)

# 异或[1,1,2,3,3]利用异或,俩个相同的数异或后则为0,0和一个数异或后得到那个数
# 则可得到只要出现一次得到数
def lis(nums):

    res=0
    for i in range(len(nums)):
        res=res ^ nums[i]
    return res
# print(lis([1,4,1,2,3,2,3,]))

#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。

# 计算异或后1 的个数
def ggg1(x,y):
    # return  bin(x^y).count("1")
    count=0
    s=x^y
    while s:
        count+=1
        s=s&(s-1)
    print(count)

# ggg1(1,4)

# 欧几里得方法 俩个数较大时取余慢,不适合
  # 俩个数的最大公约数: 一个数的约数最大也是它的一半
def ggg1(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        temp=a%b
        a=b
        b=temp#余数
    return a
# print(ggg1(16,18))

# 涨转相除法
def get_max(a,b):
    big=max(a,b)
    small=min(a,b)
    if big%small==0:
        return small
    return get_max(small,big%small)
#

# 暴力法:
def get_greatest_common_divisorl(a,b):
    big=max(a,b)
    small=min(a,b)
    if big%small==0:
        return small
    for i in range(small//2 , 0 ,-1):#公约数最大为这个数一半.倒着遍历,遇到的i就是最大公约数
        if big%i==0 and small%i==0:
            return i


# print(get_greatest_common_divisorl(3,2))


# 更相减损术法:俩个正整数的最大公约数等于a-b的差 c 和b  之间的最大公约数.
# 在减时次数多
def get_greatest_common_divisor2(a,b):
    big = max(a, b)
    small = min(a, b)
    if a-b==0:
        return a
    return get_greatest_common_divisorl(big-small,small)

# print(get_greatest_common_divisor2(12,22))

def get_greatest_common_divisor3(a,b):
    if a<b:
        a,b=b,a
    cha=a-b
    small=min(cha,b)
    big=max(cha,b)
    if big%small==0:
        return small
    return get_greatest_common_divisor3(cha,small)

# print(get_greatest_common_divisor3(24,6))





def greatest5(a,b):
    if a==b:#当俩数相同返回本身
        return a
    if a<b:#确定a为最大值
        a,b=b,a
    else:#出口为a
        if a%2==0 and b%2==0:#当a,b都为偶数
            return greatest5(a>>1,b>>1)<<1
        elif a%2==0 and b%2!=0:
            return greatest5(a>>1,b)
        elif a % 2 != 0 and b % 2 == 0:
            return greatest5(a,b>>1)
        else:
            return greatest5(b,a-b)

print(greatest5(24,8))
# print(12>>1)