# Largest Positive Integer That Exists With Its Negative
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxm= 0
        for i in nums:
            if i>maxm and -1*i in nums:
                maxm = i
        if maxm == 0:
            return -1
        else:
            return maxm
