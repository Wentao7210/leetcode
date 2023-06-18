#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        small = []
        for i in range(len(nums)):
            count = 0
            for number in nums:
                if nums[i] > number:
                    count += 1
            small.append(count)
        return small      
# @lc code=end

