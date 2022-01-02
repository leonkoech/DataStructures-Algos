# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if  len(s)<1 or len(s)>2*10**5 or not s.isascii():
            return 
#         TO:DO check if i is printable. i.isprintable()
#         remove non alphanumeric characters
        newStr= re.sub(r'[^a-zA-Z0-9]','',s).lower()
        if newStr == newStr[::-1]:
            return True
        else: 
            return False