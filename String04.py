# Given two strings s1 and s2, write a function to check whether s2 is a rotation of s1 or not

# -----------------------------------------------------------------

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
unit = 0
if (len(s1) != len(s2)) :
    print("Rotation is not possible")
else :
    for i in range(len(s1)) :
        if (s1[i] == s2[0]) :
            unit = i+1
            flag = 0
            for j in range(len(s2)) :
                if (s2[j] != s1[(i+j) % len(s1)]) :
                    flag = flag + 1
            if (flag == 0) :
                print(s2, "is a rotation of", s1, "by", unit, "characters from right and", len(s1) - unit, "from left")
                break