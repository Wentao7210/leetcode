#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j_s = 0
        while len(jewels) > count:
            for i in range(len(stones)):
                if stones[i] == jewels[count]:
                    j_s += 1
            count += 1
        return j_s       
# @lc code=end
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dictj = {}
        for j in jewels:
            if j in dictj:
                dictj[j] += 1
            else:
                dictj[j] = 1
        sum = 0
        for s in stones:
            if s in dictj:
                sum += dictj[s]
        return sum
s2 = Solution2()
s2.numJewelsInStones("aA","aAAbbbb" )