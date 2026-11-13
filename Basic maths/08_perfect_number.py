# You are given an integer n. You need to check if the number is a perfect number or not. 
# Return true if it is a perfect number, otherwise, return false.

# A perfect number is a number whose proper divisors (excluding the number itself) add up to 
# the number itself.


class Solution:
    def isperfect(self,n):
        
        if n <= 1:
            return False
        
        divisor_sum = 1
        
        for i in range(2,n):
            if n % i == 0 :
                divisor_sum +=i 
                
        return n == divisor_sum
    
result = Solution()
num = int(input("Enter number: "))
if result.isperfect(num) :
    print(f'{num} is a perfect number.') 
else:
    print(f'{num} is not a perfect number.') 