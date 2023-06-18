#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        front = [nums[i] for i in range(0, n)]
        back = [nums[i] for i in range(n, 2*n)]
        shuffled = []
        for i, j in zip(front, back):
            shuffled.append(i)
            shuffled.append(j)
        return shuffled       
# @lc code=end

