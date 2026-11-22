# You are given an integer n. You need to find all the divisors of n. Return all the divisors
# of n as an array or list in a sorted order.

class Solution:
    def divisor(self,n):
        divisior_list = []
        
        for i in range(1,n+1):
            if n % i == 0 :
                divisior_list.append(i)
                
        return divisior_list
    

result = Solution()
num = int(input("Enter number: "))
divisor = result.divisor(num) 
print(f'{num} divisors list = {divisor} ') 
