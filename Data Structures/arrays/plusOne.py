from typing import List

name = "leon"
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         add one to the array
#             [1,2,3]
            finalCount=''
            finalArr=[]
            for i in digits:
                finalCount += str(i)
            finalCount = str(int(finalCount)+1)
            for item in finalCount:
                finalArr.append(int(item))
            return finalArr
