#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#

# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_list_k = s.split()[0:k]
        return ' '.join(s_list_k)                 
# @lc code=end