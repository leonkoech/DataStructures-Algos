class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i]=nums2[i]
        # nums1.sort()
         
#         [1,2,2,2,3,5,6]
#          p2  p
#         [1,2,5,6]
#           p3
#         nums1.extend(nums2)
#         nums1.sort()
            
    
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()