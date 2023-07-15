#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {}
        for char in sentence:
            if char in alphabet:
                alphabet[char] += 1
            else:
                alphabet[char] = 0
        return len(alphabet) == 26
# @lc code=end

