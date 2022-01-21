from collections import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if  len(s)<1 or len(s)>2*10**5 or not s.isascii():
        #     return 
#         TO:DO check if i is printable. i.isprintable()
#         remove non alphanumeric characters
        newStr= re.sub(r'[^a-zA-Z0-9]','',s).lower()
        # two pointers, one starts at the end the other one starts at the begining
        start,end=0,len(newStr)-1
        while start<=end:
            if newStr[start] != newStr[end]:
                return False
            start+=1
            end-=1
        return True