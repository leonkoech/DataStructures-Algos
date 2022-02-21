class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#             find the compliment of the target and current number
#               [2,2,7,11,15]
#                4
        
        # hashmap={}
#         ans=[]
#         for i in range(len(nums)):
#             compliment = target-nums[i]
#             if compliment in hashmap:
#                 ans=[nums.index(compliment),i]
#             else:
#                 hashmap[nums[i]] = nums[i]
#         return ans
        hashmap=set()
        arr=[]
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                arr=[nums.index(compliment),i]
            else:
                hashmap.add(nums[i])
        return arr
        
#         two pointer 