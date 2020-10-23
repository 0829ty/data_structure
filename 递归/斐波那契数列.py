import time
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2  )+fib(n-1)
# for i in range(6):
#     print(fib(i))
# start=time.time()
# print(fib(5))
# end=time.time()
# t=end-start
# print(t)
# diguish

# 阶乘
def aaa(n):
    if n<=2:
        return n
    return n*aaa(n-1)
# print(aaa(5))

# 青蛙跳台阶问题
def bb(n):
    if n<=3:
        return n
    # bb(n)=bb(n-1)
    return bb(n - 2) + bb(n - 1)
print(bb(5))