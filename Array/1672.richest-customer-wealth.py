#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for row in accounts:
            wealth = sum(row)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth       
# @lc code=end

