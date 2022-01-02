# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
#         index of first occurence of needle in haystack
#         if needle is not part of the hastack
           # isFound = False
#         index if needle in haystack else -1
#         if needle is an empty string 0 +
#         constraint 1 +
#         constraint 2 +
          if len(haystack)<0 or len(needle)>5*10**4:
            return
          if needle == '':
            return 0
          if haystack.isupper() or needle.isupper():
            return       
          if needle in haystack:
            return haystack.index(needle)
          return -1 