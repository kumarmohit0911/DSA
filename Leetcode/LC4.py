# 4. Median of Two sorted array

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)-1
        n = len(nums2)-1
        temp = []
        left =0
        right =0
        while(left <=m and right <= n):
            if nums1[left]<=nums2[right]:
                temp.append(nums1[left])
                left+=1
            else:
                temp.append(nums2[right])
                right += 1
        while(left<=m):
            temp.append(nums1[left])
            left+=1
        while(right<=n):
            temp.append(nums2[right])
            right+=1

        if len(temp)%2==0:
            mid = int(len(temp)/2)-1
            mean=(temp[mid] + temp[mid+1])/2
            return mean
        else:
            mid = int(len(temp)/2)
            return temp[mid]

            
        
