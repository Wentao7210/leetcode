#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [None for ans in range(len(nums))]
        for i in nums:
            ans[i] = nums[nums[i]]
        return ans 
# @lc code=end


nums_1 = [0,2,1,5,3,4]
ans_1 = Solution().buildArray(nums_1)
print(ans_1)
nums_2 = [5,0,1,2,3,4]
ans_2 = Solution().buildArray(nums_2)
print(ans_2)

### Refelctions
# create an array and loop each value in the array to transform it
# knowing the time complexity: O(1)
### What is the solution of faster runtime and using less memory?
# hint: straight loop in an array as a return result in an function