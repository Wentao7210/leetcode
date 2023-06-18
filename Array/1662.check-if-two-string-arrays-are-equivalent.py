#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        concat_word1 = ''.join(word1)
        concat_word2 = ''.join(word2)
        return concat_word1 == concat_word2       
# @lc code=end

