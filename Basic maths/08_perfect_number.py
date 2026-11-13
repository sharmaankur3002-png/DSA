# You are given an integer n. You need to check if the number is a perfect number or not. 
# Return true if it is a perfect number, otherwise, return false.

# A perfect number is a number whose proper divisors (excluding the number itself) add up to 
# the number itself.


class Solution:
    def isperfect(self,n):
        
        if n <= 1:
            return False
        
        divisor_sum = 1
        
        i = 2 
        
        while i*i <= n :
            if n % i == 0 :
                divisor_sum += i
                
                pair = n // i
                
                if pair != i :
                    divisor_sum += pair 
                
            i += 1
            
        return n == divisor_sum
    
result = Solution()
num = int(input("Enter number: "))
if result.isperfect(num) :
    print(f'{num} is a perfect number.') 
else:
    print(f'{num} is not a perfect number.') 