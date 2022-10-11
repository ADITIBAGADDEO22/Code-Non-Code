#program for bubble sort
a=eval(input("enter a list with [] sep by ,"))
for i in range(1,len(a)):
    j=i-1
    temp=a[i]
    while temp<a[j] and j>=0:
        a[j+1]=a[j]
        a[j]=temp
        j=j-1
    
print(a)