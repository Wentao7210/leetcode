#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffling_dic = {}
        list_str = list(s)
        for i in range(len(indices)):
            shuffling_dic[indices[i]] = list_str[i]
        shuffling_dic = dict(sorted(shuffling_dic.items()))
        shuffled_list = list(shuffling_dic.values())
        shuffled_str = ''.join(shuffled_list)
        return shuffled_str
# @lc code=end

