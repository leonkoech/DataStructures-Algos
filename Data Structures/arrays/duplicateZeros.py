# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


arr = [1,0,2,3,0,4,5,0]
newArr=[0]*len(arr)
# [1,0, ,2,3,0,4,5,0]
# [1,0,0,2,3,0,4,5]
# Output: [1,0,0,2,3,0,0,4]
for i in range(len(arr)):
    if arr[i] == 0:
        newArr[i] = 0
        newArr[i+1]=0