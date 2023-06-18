#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digit_sum = 0
        for num in nums:
            for n in str(num):
                digit_sum += int(n)
        return abs(sum(nums) - digit_sum)       
# @lc code=end

