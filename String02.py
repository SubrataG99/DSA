# Given a string of length 'N', you have to find the number of palindrome subsequences (need not necessarily be disitnct) present in string

# ----------------------------------------------------------------------------

def isPalindrome(w) :
    new = w
    w = w[::-1]
    if (new == w) :
        return True
    else :
        return False

s = input("Enter a word : ")
temp = ''
cnt = 0
for i in range(len(s) - 1) :
    temp = temp + s[i]
    for j in range(i+1, len(s)) :
        temp = temp + s[j]
        if (isPalindrome(temp)) :
            cnt = cnt + 1
            print(temp)
    temp = ''
print("There are total", cnt, "palindrome substrings")