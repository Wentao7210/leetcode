#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]
        for i in range(len(encoded)):
            arr.append(int(encoded[i] ^ arr[i]))
        return arr       
# @lc code=end

