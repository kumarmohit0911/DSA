class Solution:

    def merge(self,nums,low,mid,high):
        temp=[]
        left = low
        right=mid+1
        while(left<=mid and right<=high):
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=mid):
            # if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        while(right<=high):
            # if nums[left]<=nums[right]:
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i]= temp[i - low] 
            
    def mergeS(self,nums,low,high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeS(nums,low,mid)
        self.mergeS(nums,mid+1,high)
        self.merge(nums,low,mid,high)  
        # return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        self.mergeS(nums,low,high)
        return nums         