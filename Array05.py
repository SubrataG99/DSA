# Given an array consisting of only 0s, 1s and 2s. Write a program to in-place sort the array without using inbuilt sort functions, in linear time complexity and constant space

# ---------------------------------------------------------------------------------------

n = int(input("Enter the size of array : "))
a = []
for i in range(n) :
    a.append(int(input("Enter element : ")))
l = 0
m = 0
h = n-1

while m < h :
    if (a[m] == 0) :                # to check for 0
        a[l], a[m] = a[m], a[l]
        l = l + 1
        m = m + 1
    elif (a[m] == 1) :              # to check for 1
        m = m + 1
    else :                          # for presence of 2
        a[m], a[h] = a[h], a[m]
        h = h - 1

print(a)