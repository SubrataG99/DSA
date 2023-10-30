# You are given an integer array height of length 'n'. There are n-vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store

# -------------------------------------------------------------------------------------------
import random

n = int(input("Enter the length of array : "))
a = random.sample(range(1, 2*n), n)
area = 0
for i in range(n - 1) :
    for j in range(i + 1, n) :
        area = max(area, min(a[i], a[j]) * (j - i))
print("List :", a)
print("Maximum area of container is :", area, "sq units")