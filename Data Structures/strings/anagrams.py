from collections import Counter

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#       constraints cases
        if len(s)<1 or len(s)<5&10**4 or len(t)<1 or len(t)<5&10**4:
            return
        if s.isupper() or t.isupper():
            return
        
#       main fun
        if Counter(s) == Counter(t):
            return True
        else:
            return False