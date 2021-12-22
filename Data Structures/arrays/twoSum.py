# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#             find the compliment of the target and current number
#               [2,2,7,11,15]
#                4
        
        hashmap={}
        ans=[]
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in hashmap:
                ans=[nums.index(compliment),i]
            else:
                hashmap[nums[i]] = nums[i]
        return ans
        