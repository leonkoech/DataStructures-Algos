# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
#           use set
#           add items based on their availability. 
#           If item is in stack remove it
#           take first value in stack
           
            if len(s)>=1 and len(s)<=10**5 and s.islower():
                myhash={}
                for i in range(len(s)):
                    if s[i] not in myhash:
                        myhash[s[i]]=i
                    else:
                        myhash[s[i]]=-1
#                 get the least value in the hash between 0 and len
# aaabbc
# {a:-1,b-1,c=5}

                miny = -1
                for y in myhash.values():
                    if y>-1:
                        if miny==-1:
                            miny=y
                        else:
                            miny  = min(miny,y)
                return miny                  
            else:
                return