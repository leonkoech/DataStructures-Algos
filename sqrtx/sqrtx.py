class Solution:
    def mySqrt(self, x: int) -> int:
        begin, end = 0, x
#         8
#          two pointers 0 and 8
#          increse 0 by mid which is 8+0//2
#           if (8+0//2)**2 == target return min
#           if ^^^^^^^^^^^ < target: 0= min + 1
#             else 8=min-1


        while begin<=end:
            mid=(begin+end)//2
            temp=mid*mid
            if temp==x:
                return mid
            if x>temp:
                begin = mid+1
            else:
                end = mid -1
        return end

        
        
        # Use binary search to find the largest
        # integer i such that, i * i <= x
        # while begin <= end:
        #     mid = (begin + end) // 2
        #     temp = mid * mid
        #     if temp == x:   
        #         return mid
        #     elif temp < x:  
        #         begin = mid + 1
        #     else:           
        #         end = mid - 1
        # return end
        