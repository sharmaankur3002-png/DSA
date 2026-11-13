# You are given an integer n. Return the value of n! or n factorial.

# Factorial of a number is the product of all positive integers less than or 
# equal to that number.

class Solution :
    def factorial(self,n):
        
        if n < 0 :
            raise ValueError("number must be positive!")
        
        fact = 1
        
        while n>0:
            
            fact *= n 
            
            n= n-1
        return fact 
    
result = Solution()
num = int(input("Enter number: "))
print( f"{num} Factorial = {result.factorial(num)}" )    
