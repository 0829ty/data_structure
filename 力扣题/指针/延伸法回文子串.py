def longestPalindrome(s: str) -> str:
    if not s:  # 当字符串为空时
        return "empty"
    length = len(s)  # 字符串长度
    if length == 1 or s == s[::-1]:  # 当字符串长度为1 或者字符串正反都一样返回字符串
        return s
    max_len, start = 1, 0  # 设置回文字符串最长长度为1,从0开始计算
    for i in range(1, length):
        even = s[i - max_len:i + 1]  # 偶数位回文/记录遍历下标减去最大长度,到下标值
        odd = s[i - max_len - 1:i + 1]  # 奇数位回文/记录下标减去最大长度减一 到下标值
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            # 当odd找到一个时,包头包尾部回文开始为坐标值减去最大的回文长度在向前一步
            start = i - max_len - 1
            max_len += 2  # 最大长度加二
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len  # 当用even找到时,开始位置减去最大长度
            max_len += 1  # 最大长度加一就是完整的回文长度
            continue
    return s[start:start + max_len]
# print(longestPalindrome(s="asdacagb"))


# 延伸法:分离指针
def centerSpread(s: str, left: int, right: int):  # 中心扩展
    i = left
    j = right
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    return s[i + 1:j]


def longestPalindrome1(s: str) -> str:
    length = len(s)
    if length <= 1:
        return s
    maxlen = 1  # 最大长度
    res = s[0]  # 结果
    for i in range(length - 1):  # 遍历字符串
        odd = centerSpread(s, i, i)  # 计算奇数
        even = centerSpread(s, i, i + 1)  # 计算偶数中心点为i 和i+1
        maxstr = odd if len(odd) > len(even) else even  # 最长字符串
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


# def longestPalindrome3(s: str ):
#     length=len(s)
#     if length<=1:
#         return s
#     maxlen=1
#     res=[0]


if __name__ == '__main__':
    atrs = "001002033304"
    print(longestPalindrome1(atrs))
