class Solution: 
    def reverse(self, x: int) -> int:
#         meet base cases
        if x ==0:
            return 0
        if x>=-2**31 and x<= 2**31 - 1:
            result=0
#             make sure that the result is within the constraints
#             check if number is negative
#             loop from the back forming a string with the value
#             if negative, multiply by -
#              123, -123
#               [2],[1],[0] : [3],[2],[1]
            y=''
            for i in range(len(str(x))-1,-1 if x>0 else 0,-1):
                    y+= str(x)[i]
                
            result = int(y)*-1 if x<0 else int(y)
            
            if result>=-2**31 and result<= 2**31 - 1:
                return result
#           if the answer is greater or smaller that the 32bits return 0
            else:
                return 0
                
        else:
            return
       