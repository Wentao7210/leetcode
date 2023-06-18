#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums
        return ans
# @lc code=end

nums_1 = [1,2,1]
nums_2 = [1,3,2,1]
ans_1 = Solution().getConcatenation(nums_1)
ans_2 = Solution().getConcatenation(nums_2)
print(ans_1, ans_2)

### Reflection
# first I used append funtion -> exceed the time limit
# if want to concatente, just use + for lists or arrays