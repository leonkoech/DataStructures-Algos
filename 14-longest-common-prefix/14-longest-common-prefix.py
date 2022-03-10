class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
#       ["flower","flow","flight"]
#       [f,l,o,w]
#       main=strs[0]        
               
        word = min(strs,key=len) if strs else ''
#         remove word from the position
        strs.remove(word)
        for wrd in range(len(strs)):
            
            
            comparable = strs[wrd]
#             flower, flow
            for i in range(len(word)):
                if not word[i]  == comparable[i]:
                    word=  word[:i]
                    break
            
        return word
            