#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        countList = []
        for sentence in sentences:
            count = 0
            for i in sentence:
                if i == ' ':
                    count += 1
            countList.append(count)
        return max(countList)+1     
# @lc code=end

