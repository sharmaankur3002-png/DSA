# You are given an integer n. Return the integer formed by placing the digits of n in
# reverse order.

class solution():
    def reverse(self,n):
        
        if n < 0:
            sign = -1
        else :
            sign = 1
            
        n = abs(n)
        
        rev = 0
        while(n>0):
            
            last_digit = n % 10
        
            rev = rev*10 + last_digit
            
            n = n//10
        
        return rev * sign
        
result = solution()
num = int(input("Enter number: "))
print(result.reverse(num))       