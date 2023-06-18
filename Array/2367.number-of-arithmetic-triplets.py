#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        #if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        number_tri = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff and k < len(nums) and j < k and i < j:
                        number_tri += 1
        return number_tri     
# @lc code=end

