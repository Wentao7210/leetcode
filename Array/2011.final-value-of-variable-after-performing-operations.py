#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for str in operations:
            if str[1] == '+':
                x += 1
            else:
                x -= 1
        return x       
# @lc code=end

