# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times

# ---------------------------------------------------------------------------------

import random

s = input("Enter a word : ")
k = int(input("Enter number of changes : "))
ls = list(s)
if (k > len(s)) :
    print("Proper change is not possible")
    print("You should have given a number not more than", len(s))
else :
    key = random.sample(range(0, len(s)), k)
    # print(key)
    for i in key :
        ls[i] = ls[i].upper()
    print(''.join(ls))