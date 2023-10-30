# Given an array of integers and an integer target, return indices of the two numbers such that they add up to target

# ---------------------------------------------------------------------------
import random

n = int(input("Enter length of array : "))
a = random.sample(range(-n, n), n)
t = int(input("Enter the target : "))
print("Array is :", a)
flag = 0
if t not in a :
    for i in range(n - 1) :
        for j in range(i+1, n) :
            if (a[i] + a[j] == t) :
                print("The components of", t, "are", a[i], "and", a[j])
                flag = flag + 1
                break
    if (flag == 0) :
        print(t, "is not present also does not have its components in the array")
else :
    print(t, "is present whole in array but no break-down components")