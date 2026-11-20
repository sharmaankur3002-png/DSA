# You are given an integer n. You need to find out the number of prime numbers in the 
# range [1, n] (inclusive). Return the number of prime numbers in the range.

# A prime number is a number which has no divisors except, 1 and itself.

class Solution:
    def count_prime(self,n):
        
        count = 0
        
        for num in range (2,n+1):
            for i in range(2,num):
                 
                if num % i == 0:
                    break
            else :
                count+=1

        return count

result = Solution()
num = int(input("Enter number: "))
total = result.count_prime(num) 
print(f'{num} have {total} prime number.') 