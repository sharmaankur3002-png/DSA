# You are given an integer n. You need to check if the number is prime or not. Return 
# true if it is a prime number, otherwise return false.

# A prime number is a number which has no divisors except 1 and itself.

class Solution:
    def is_prime(self,n):
 
        if n <= 1:
            return False
        
        i = 2
        
        while i*i <= n :
            
            if n % i == 0:
                return False
            
            i += 1
        
        return True
result = Solution()
num = int(input("Enter number: "))
if result.is_prime(num) :
    print(f'{num} is a prime number.') 
else:
    print(f'{num} is not a prime number.') 