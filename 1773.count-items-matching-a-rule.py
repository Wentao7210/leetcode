#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
### original solution
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # dict for index and rulekey
        rules = ['type', 'color', 'name']
        rules_dict = {n:rules[n] for n in range(len(rules))}
        # matching test
        matchlist = []
        for item in items:
            for key,value in rules_dict.items():
                if ruleKey == value and item[key] == ruleValue:
                    matchlist.append(item)
        return len(matchlist)
# @lc code=end


### better solution in two lines
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
    

### modified solution
#for line 12,13
rules = ['type', 'color', 'name']
rules_dict = {rules[i]:i for i in range(len(rules))} # or: rules_dict = {value:index for index, value in enumerate(rules)}
#for line 16~19
    #for item in items:
        #if item[rules_dict[ruleKey]] == ruleValue:
            #matchlist.append(item)  

s = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
s.countMatches(items,ruleKey,ruleValue)