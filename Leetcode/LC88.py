# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        temp = []
        left =0
        right =0
        while left<=m-1 and right<=n-1:
            if nums1[left]<=nums2[right]:
                #if nums1[left]!=0:
                temp.append(nums1[left])
                left+=1
            elif(nums1[left]>=nums2[right]):
                #if nums2[right]!=0:
                temp.append(nums2[right])
                right+=1                
        while left<=m-1:
            # if nums1[left]!=0:
            temp.append(nums1[left])
            left+=1
        while right<=n-1:
            # if nums2[right]!=0:
            temp.append(nums2[right])
            right+=1 


        for i in range(len(temp)):
            nums1[i]=temp[i]
        return nums1
                



        