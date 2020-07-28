import math

def palindrome(x):
    reverse = 0
    demolisher = x
    while demolisher >= 1:
        reverse = reverse * 10 + (int(demolisher%10))
        demolisher /= 10
    return (x == reverse)


a = 10
print(palindrome(a))
b = 121
print(palindrome(b))
c = 1231
print(palindrome(c))
d = 12221
print(palindrome(d))