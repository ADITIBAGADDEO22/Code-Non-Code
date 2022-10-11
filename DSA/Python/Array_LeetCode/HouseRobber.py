# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         elif n == 2:
#             return max(nums[0], nums[1])
#         elif n == 3:
#             return max(nums[1], nums[0] + nums[2])
#         dp = [0] * n
#         dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
#         for i in range(3, n):
#             dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
#         return max(dp[-1], dp[-2])
def rob(self, nums: List[int]) -> int:
        prev=0
        curr=0
        for x in nums:
            temp=prev
            prev=curr
            curr=max(x+temp,prev)
        return curr