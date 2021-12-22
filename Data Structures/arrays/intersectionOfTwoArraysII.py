# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element 
# in the result must appear as many times as it shows in both arrays and you may return the result 
# in any order.

array = []
array=input(" ").split(" ")

for i in range(len(array)):
    max_index = i
    for j in range(i+1, len(array)):
        if int(array[j]) > int(array[max_index]):
            max_index = j
    
    array[i],array[max_index] = int(array[max_index]),int(array[i])
    
    print(array)