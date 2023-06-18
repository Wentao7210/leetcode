#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    
    # search for duplicate numbers
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        # number of good pairs
        repeat = {}
        num = 0
        
        # for every element in nums
        for v in nums:
            
            # number of repeated digits
            if v in repeat:
                
                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                
                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num       
# @lc code=end

