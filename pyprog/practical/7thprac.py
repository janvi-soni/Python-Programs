def chkPalindrome(s):
    a=(s[::-1])
    if(s==a):
        print("palindrome")
    else:
        print("not a palindrome")
    
    
b=input("enter the string")
chkPalindrome(b)
    
