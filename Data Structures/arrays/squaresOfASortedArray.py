# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

nums = [-4,-1,0,3,10]
#          p1   p2
newarr=[0]*len(nums)
# [0,1,9,16,100]
# [0,0,0,0,100]
# two pointer technique
p1,p2=0,len(nums)-1
for i in range(len(newarr)-1,-1,-1):
        if abs(nums[p1])>abs(nums[p2]):
                val=nums[p1]
                p1+=1
        else:
            val=nums[p2]
            p2-=1
        newarr[i]=val*val
print(newarr)