#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = []
        ssum = 0
        for i in range(len(nums)):
            ssum += nums[i]
            running_sum.append(ssum)
        return running_sum
# @lc code=end

