# remove elements
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        list_length = len(nums)
        cnt =0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt+=1
        
        return cnt