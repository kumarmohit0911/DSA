# 912. Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums,low,mid,high):
            temp=[]
            while(left<=mid and right<=high):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while(left<len(nums)):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
            while(right<len(nums)):
                if nums[left]<=nums[right]:
                    temp.append(nums[right])
                    right+=1
            for i in range(low,high):
                nums[i]= temp[i - low] 

            return nums      
        
        
    low = 0
    high = len(nums)-1    
        
    def mergeS(nums,low,high):
        if low==high:
            return

        mid = low+high//2
        mergeS(nums,low,mid)
        mergeS(nums,mid+1,high)
        merge(nums,low,mid,high)


        