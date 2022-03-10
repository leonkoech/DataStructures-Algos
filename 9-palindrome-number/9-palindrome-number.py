class Solution:
    def isPalindrome(self, x: int) -> bool:
            # two pointer technique
            
            # 12233221
            # p1     p2
            
            listo=str(x)
            p1=0
            p2=len(listo)-1
            while p1<=p2:
                if listo[p1]!=listo[p2]:
                    return False
                p1+=1
                p2-=1
            return True