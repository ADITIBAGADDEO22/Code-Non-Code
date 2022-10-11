# python script to check prime number 

num = int(input("Enter a number: "))


#boolean variable condition 
S1 = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set s1 to True
            S1 = True
            # break out of loop
            break

# check if flag is True
if S1:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
