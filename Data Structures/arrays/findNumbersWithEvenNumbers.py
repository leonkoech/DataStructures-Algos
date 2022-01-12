# Given an array nums of integers, return how many of them contain an even number of digits.

# [12,3,4,5,,6,7,7]
# of digits, so its character count
nums=[12,3,4,5,6,7,7,8]
# ans 1
count=0
for i in nums:
    if len(str(i))%2==0:
        count+=1
print(count) 
