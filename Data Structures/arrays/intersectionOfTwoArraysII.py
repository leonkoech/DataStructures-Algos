# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element 
# in the result must appear as many times as it shows in both arrays and you may return the result 
# in any order.


from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count={}
        ans=[]
        
        for i in nums1:
            count[i]=count.get(i,0) + 1
        
        for b in nums2:
            if b in count and count[b] > 0:
                ans.append(b)
                count[b] -= 1
        return ans
  

