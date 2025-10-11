# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        m =len(word1)-1
        n=len(word2)-1
        concat=""

        while(left<=m and right<=n):
            concat+=word1[left]+word2[right]
            left+=1
            right+=1
        while(right<=n):
            concat+=word2[right]
            right+=1
        while(left<=m):
            concat+=word1[left]
            left+=1
        return concat             
            
