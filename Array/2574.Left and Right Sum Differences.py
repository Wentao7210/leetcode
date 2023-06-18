class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        return [abs(sum(nums[:i])-sum(nums[(i+1):])) for i in range(len(nums))]