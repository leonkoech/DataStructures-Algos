class Solution:
    
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # strs = ["eat","tea","tan","ate","nat","bat"]
#             iterate over strs creating subarrays in a big array
#             for every element, check if the anagram is contained in subarrays
#             get total value of word ord
        hashmap={}
    
        
        # {eat:[tea,eat,ate],atn:[]}
        for j in strs:
            k= "".join(j for j in sorted(j))
            if k in hashmap:
                hashmap[k].append(j)
            else:
                hashmap[k] = [j]
       # print(hashmap)
        
        return list(hashmap.values())