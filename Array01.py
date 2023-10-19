# Write a program to reverse an array

n = int(input("Enter number of elements you want to enter : "))
arr = []
for i in range(n) :
    temp = int(input("Enter element : "))
    arr.append(temp)
print("Original array : ", arr)

# ------------------------------------------------------------------Using pre-defined Function
arr.reverse()
print("\nReversing using predefined function : ", arr)

# ------------------------------------------------------------------Using Slicing
arr[::-1]
print("\nReversing using Slicing : ", arr)

# ------------------------------------------------------------------Using basic method
print("\nBefore : ", arr)
for i in range(n//2) :
    temp = arr[i]
    arr[i] = arr[n-1-i]
    arr[n-i-1] = temp
print("Reversing using basic idea/logic : ", arr)