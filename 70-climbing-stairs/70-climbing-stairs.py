class Solution:
    def climbStairs(self, n: int) -> int:
        temp=0
        cur=1
        pre=1
        for b in range(1,n):
            temp=cur
            cur=cur+pre
            pre=temp          
        return cur
        
        