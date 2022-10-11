def bubbleSort(ar):
    n = len(ar)
    swapped = False
    for i in range( n - 1 ):
        for j in range( 0, n - i - 1 ):
            if ar[j] > ar[j + 1]:
                swapped = True
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
         
        if not swapped:
            return
 
 
ar = [19, 14, 72, 8, 97, 1, 63, 54, 31]
 
bubbleSort(ar)
 
print("Sorted array is:")
for i in range(len(ar)):
    print("% d" % ar[i], end=" ")

print("\n")