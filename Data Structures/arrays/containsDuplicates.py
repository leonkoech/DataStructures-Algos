# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution():
    def containsDuplicate(self,mylist):
        # using set solution
        myset=set()
        # {1,2,3,4,5,5}
        for i in mylist:
            if i in myset:
                return True
            else:
                myset.add(i)
        return False
    def containsDuplicatehash(self,mylist):
        # using set solution
        hashmap={}
        for i in mylist:
            if i not in hashmap:
                hashmap[i] =i
            else:
                # meaning the number is alreadyu in the hashmap
                return True
        # if the return true doesn't run then this should run because no duplicate was found
        return False


# using set
print(Solution().containsDuplicate([2,2,1]))
# using hashmaps
print(Solution().containsDuplicatehash([2,2,1]))