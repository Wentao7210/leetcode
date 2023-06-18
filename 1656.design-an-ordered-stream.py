#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.newlist = n*[None]
        self.startnumber = 0


    def insert(self, idKey: int, value: str) -> list[str]:
        self.newlist[idKey-1] = value
        ans = []
        while self.startnumber < len(self.newlist) and self.newlist[self.startnumber] is not None:
            ans.append(self.newlist[self.startnumber])
            self.startnumber += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

