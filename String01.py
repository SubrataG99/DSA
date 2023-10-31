# Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory

# -----------------------------------------------------------------------------

s = input("Enter a string : ")
n = len(s)
l = list(s)
for i in range(len(s)//2) :
    l[i], l[n-i-1] = l[n-i-1], l[i]
print("Reversed string :", ''.join(l))