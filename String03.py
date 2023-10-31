# Given two strings s and p, return an array of all the start indices of p's anagrams in s

# ----------------------------------------------------------------------------------------------------------

s = input("Enter main string : ")
p = input("Enter anagrams : ").split(' ')
print("Main string :", s)
print("Anagrams are : ", p)
for i in range(len(p)) :
    if (p[i] in s) :
        print(p[i], "is present from position", s.index(p[i]) + 1)