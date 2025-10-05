# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif(len(nums)==1):
            if nums[0]>target:
                return 0
            else:
                return 1 
        else:
            i = 1
            while(i<len(nums)):
                if target > nums[i-1] and target <nums[i]:
                    return i
                elif( target < nums[i]):
                    return i-1
                i+=1
            return len(nums)