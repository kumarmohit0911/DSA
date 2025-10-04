# Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        cnt = 1
        for i in range(k - 2):
            
            if nums[i] == nums[i+1]:
                cnt+=1
                if cnt>2:
                    nums.remove(nums[i])
                    k-=1
            else:
                cnt = 1
        return k,nums
        