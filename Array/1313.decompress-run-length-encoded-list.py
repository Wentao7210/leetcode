#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        concat_arr = []
        for i in range(int(len(nums)/2)):
            arr = int(nums[2*i])*[nums[2*i+1]]
            concat_arr += arr
        return concat_arr
# @lc code=end

