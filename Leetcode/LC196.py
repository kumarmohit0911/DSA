# 196 find peak element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxm = max(nums)
        for i in nums:
            if i ==maxm:
                return nums.index(maxm)
























#         class Solution:
# #     def merge(nums,low, mid,high):
# #         left = low
# #         right = mid +
# #     def mergeSort(nums,low,high):
# #         if low == high:
# #             return
# #         mid = low+high//2
# #         mergeSort(nums,low,mid)
# #         mergeSort(nums,mid+1,high)
# #         merge(nums,low,mid,high)

#     def findPeakElement(self, nums: List[int]) -> int:
# #         low=0
# #         high=len(nums)-1
# #         mergeSort(nums,low,high)
# #         return nums  
      
