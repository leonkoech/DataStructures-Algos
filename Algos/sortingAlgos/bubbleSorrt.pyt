# Write a function rotate(ar[], n) that rotates arr[] of size n by d elements. 
def leftRotate(arr,n):
    # create a temp arr of the first n
    # pop the first n arrays from arr
    # join temp to the popped arr
    if n!=len(arr) and n<len(arr):
        temp=arr[:n]
        for x in temp:
            arr.pop(arr.index(x))
            arr.append(x)
    return arr
def sortSummary():
    # find distinct values 
    # iterate through the arr and count the number of times each items appears
    # if the item appears at least one time add it to another list as a 2d array with the number of times it appears
    # sort by the second value of the 2d array
    n=[3,3,1,2,1]
    newArr=[]
    
    for val in n:
       if [val,n.count(val)] not in newArr:
           newArr.append([val,n.count(val)])
    newArr.sort(key=lambda x:x[1], reverse=True)
    newArr.sort(key=lambda y:y[1],reverse=False)
           
  
    print(newArr)
def insertion_sort():
#     The worst case time complexity of Insertion sort is O(N^2)
# The average case time complexity of Insertion sort is O(N^2)
# The time complexity of the best case is O(N).
# The space complexity is O(1)
    arr=[9,3,4,5,5,6,6,3,3,2,43,2,5,46,4,5,65,6,5742,1,23,23,6,3,45,56,4,234,2,32,2,32,3,5,7,5,5,6,2,7,78,5]
    n = len(arr)
    for x in range(1,n):
        while arr[x-1] > arr[x] and x>0:
            arr[x],arr[x-1]=arr[x-1],arr[x]
            # print(x)
            x=x-1
            # print(x)
        # x=x-1
    print(arr)
# def merge_sort():
# insertion_sort()
def selection_sort():
        arr=[9,3,4,5,5,6,6,3,3,2,342,65,32,5,5,22,3,56,4,5,4,67,5,65,6,67,7,45,5,5,43,5,2,23,4,34,34,1,31,4,2,424,234]
        # take the value on the left and compare it to the values on the right
        # then look for the minimum value
        # shift that value to the left or add it to a new list

        # create an empty list, take value at index and compare it to all the values in the arr, if the value is smallest add it to the new list and pop it from the existing list
        for n in range(0,len(arr)-1):
            minv = n
            for k in range(n+1,len(arr)):
                if arr[k] < arr[minv]:
                    minv = k
            if minv != n:
                arr[minv],arr[n] = arr[n], arr[minv] 
        print(arr)
def binary_search(data, target, low, high):
     
    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
    if target == data[mid]: # found a match
        return True
    elif target < data[mid]:
     # recur on the portion left of the middle
        return binary_search(data, target, low, mid - 1)
    else:
     # recur on the portion right of the middle
        return binary_search(data, target, mid + 1, high) 
def main():
   selection_sort()

if __name__=="__main__":
    main()





