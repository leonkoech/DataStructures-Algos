
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
#         0(1) extra memory
#         handle constraints
        for i in s:
            if not i.isprintable():
                return
        
        if len(s)>=1 and len(s)<=10**5:
            
            return s.reverse()
        else:
            return
        