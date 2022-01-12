# Given a binary array nums, return the maximum number of consecutive 1's in the array.
nums=[1,1,0,0,0,0,1,1,1,1,0,0,0,1]
count=0
ans=0
for i in range(len(nums)):
    if nums[i] != 1:
        
        count=0
    else:
        count+=1
    ans=max(count,ans)
print(ans)