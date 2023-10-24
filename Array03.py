# Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum and print the subarray

# Principle used : Kadane Algorithm

from sys import maxsize

n = int(input("Enter number of elements : "))
start = 0
end = 0
s = 0
a = []
till = -maxsize - 1
maxend = 0
for i in range(n) :
    a.append(int(input("Enter element : ")))
print("The list is : ", a)
for i in range(n) :
    maxend = maxend + a[i]
    if (till < maxend) :
        till = maxend
        start = s
        end = i
    if (maxend < 0) :
        maxend = 0
        s = i+1
print("\nThe subcontiguous array is : ", a[start : end+1])
print("Sum : ", till)