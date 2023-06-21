#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        bracket = []
        stack = []
        max_number = []
        for str in s:
            if str == '(' or str == ')':
                bracket.append(str)
        if len(bracket) == 0:
            return 0
        for i in range(len(bracket)):
            if bracket[i] == '(':
                stack.append(bracket[i])
                max_number.append(len(stack))
            elif bracket[i] == ')':
                stack.pop()
        return max(max_number)
    

class BetterSolution:
    def maxDepth(self, s: str) -> int:
        bracket = []
        stack = []
        max_number = 0
        for str in s:
            if str == '(' or str == ')':
                bracket.append(str)
        if len(bracket) == 0:
            return 0
        for i in range(len(bracket)):
            if bracket[i] == '(':
                stack.append(bracket[i])
                max_number = max(max_number, len(stack))
            elif bracket[i] == ')':
                stack.pop()
        return max_number       


class MuchBetterSolution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_number = 0
        if len(s) == 0:
            return 0
        for str in s:
            if str == '(':
                stack.append(str)
                max_number = max(max_number, len(stack))
            elif str == ')':
                stack.pop()
        return max_number
    

class SolutionwithabitlessprocessingtimeANDmuchlessmemoryusage:
    def maxDepth(self, s: str) -> int:
        ans = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                ans = max(ans, cur)
            elif c == ')':
                cur -= 1
        return ans 
# @lc code=end

