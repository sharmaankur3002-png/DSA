# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of 
# the two given numbers. Return the GCD of the two numbers.

class Solution:
    def gcd(self,n1,n2):
        
        small = min(n1,n2)
        gcd = 1
        
        for i in range(2,small+1):
            if n1 % i == 0 and n2 % i == 0 :
                gcd = i
    
        return gcd
    
result = Solution()
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
gcd = result.gcd(num1,num2) 
print(f'{num1} and {num2} gcd = {gcd} ')