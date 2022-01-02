# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
#       ["flower","flow","flight"]
#       [f,l,o,w]
#       main=strs[0]
        if len(strs) < 1 or len(strs)>200 :
                return
        
        
               
        word = min(strs,key=len) if min(strs,key=len).islower() else ''
#         remove word from the position
        strs.remove(word)
        for wrd in range(len(strs)):
            if strs[wrd].isupper():
                return
            
            comparable = strs[wrd]
#             flower, flow
            for i in range(len(word)):
                if not word[i]  == comparable[i]:
                    word=  word[:i]
                    break
            
        return word