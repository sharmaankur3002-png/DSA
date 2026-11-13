# You are given an integer n. You need to check whether the number is a palindrome number 
# or not. Return true if it's a palindrome number, otherwise return false.

# A palindrome number is a number which reads the same both left to right and 
# right to left.


class solution :
    def palindrome(self,n):
        if n < 0:
            return False
        num = n 
        revrse = 0
        while (num>0):
            
            last_digit = num % 10
            
            revrse = revrse*10 + last_digit
            
            num = num // 10
            
        return revrse == n 
            
           
result = solution()
num = int(input("Enter number: "))
if result.palindrome(num) :
    print(f'{num} is a palindrom') 
else:
    print(f'{num} is not a palindrom')         