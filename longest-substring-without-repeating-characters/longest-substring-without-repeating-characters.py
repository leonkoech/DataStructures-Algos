class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        
        
        
        
        
        
        
        
#         use a sliding window technique
    # '''
    # create a hashmap and store the position as well as the index of the item
    # loop through the string trying to check if the item is in the hashmap
    #     if the item is in the hashmap move the start to where the maximum index 
    #     is of the i. So start=max(start,hashmap[i])
    # total so far should be [0,0,0,p1,7,7,7,p2] find the diference between p2 and p1
    # and because p2 is 0 indexed add 1
    # '''
    
#     start and end can be considered as the reader and writer sliding window
        start=0

        total=0
        hashmap={}
        for reader in range(len(s)):
            if s[reader] in hashmap:
                start=max(start,hashmap[s[reader]])
            
            total=max(total,reader-start+1)
            hashmap[s[reader]]=reader+1
        return total