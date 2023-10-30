# Given an unsorted array of size 'n'. Array elements are in the range of 1 to n. One number from set (1, 2, 3,..., n) is missing and one number occurs twice in the array. Find these two number.

# ------------------------------------------------------------------------
import random

n = int(input("Enter length of array : "))
a = random.sample(range(1, n), n-1)
a.append(random.randint(1, n))
print("Array is :", a)
flag = 0
for i in range(1, n + 1) :
    if (i not in a) :
        print("Missing number is :", i)
        for j in range(n) :
            if ((a[j] == a[i-1]) and (j != i - 1)) :
                flag = flag + 1
            if (flag == 1) :
                print("Repeating number is", a[i-1], "at position", j+1, "and", i)
                break
            else :
                flag = 0
if (not flag) :
    print("All are distinct")