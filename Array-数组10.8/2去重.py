# # a=[1,1,3,2,4,4,5]
# # a=set(a)
# # print(a)
# # [1,1,2,2,3,4,]-->[1,2,3,4,1,2]
# # [1,1,2,2,3,4,]-->[1,2,2,3,4,1]
# from typing import List
#
#
# class Solution:
#     def removeDuplicated(self, nums: List[int]) -> int:
#         n = len(set(nums))
#         i = 0
#         while i < n - 1:
#             if nums[i] == nums[i + 1]:
#                 temp = nums[i + 1]
#                 nums[i + 1:len(nums) - 1] = nums[i + 2:]
#                 nums[-1] = temp
#                 continue
#             else:
#                 i += 1
#         return i + 1
#
#
# a = Solution()
# a.removeDuplicated([1, 1, 2, 3, 5, 2])

class Solution:
    def removeDuplicated(self,nums ):
        slow=0#慢指针
        fast=1#快指针
        while fast<len(nums):
            if nums[fast] !=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
                fast+=1

            elif nums[fast] == nums[slow] :
                fast+=1
        print( nums)

a = Solution()
a.removeDuplicated([1, 1,1, 2, 2, 5, 26])
