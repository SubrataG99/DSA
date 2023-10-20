# Find the kth smallest element in an array in linear time complexity

n = int(input("Enter number of elements : "))
arr = []
for i in range(n) :
    arr.append(input("Enter element : "))
print("\nOriginal Array : ", arr)
res = arr[0]
pos = 1
for i in range(n) :
    if (arr[i] < res) :
        res = arr[i]
        pos = i+1
print("Smallest element is :", res, "located at position", pos)