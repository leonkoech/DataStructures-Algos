# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
class solution():
    def function(self,mylist):
        # [0,2,3,4,0,3,1]
        # [2,3,4,0,3,1,0]
        # [2,3,4,3,1,0,0]

        num=mylist.count(0)
        # O(n)
        for i in range(num):
            # O(k)
            mylist.remove(0)
            mylist.append(0)
        return mylist
        
print(solution().function([0,2,3,4,0,3,1,]))

# time complexity O(n)