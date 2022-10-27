# Python Selection sort algorithm

arr = [90,43,5,7,2]
  
# tranversing loop in array
for i in range(len(arr)):
      
    # min_index is minimum index set as first element
    
    min_index = i
    # Loop to iterate over un-sorted sub-array
    for j in range(i+1, len(arr)):
    
    #Finding the minimum element in the unsorted sub-array
        if arr[min_index] > arr[j]:
            min_index = j
              
    # swapping the minimum element with the element at min_index to place it at its correct position    
    arr[i], arr[min_index] = arr[min_index], arr[i]
  
# Print the sorted array obtained

print("Sorted Array is " , arr)
