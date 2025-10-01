def is_palindrome(s):
    return s==s[::-1]
s=input("enter a string :   ")
if is_palindrome(s):
    print("palindrome")
else:
    print("not a palindrome")