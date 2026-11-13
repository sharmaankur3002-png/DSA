# You are given an integer n. You need to check whether it is an armstrong number or not. 
# Return true if it is an armstrong number, otherwise return false.

# An armstrong number is a number which is equal to the sum of the digits of the number, 
# raised to the power of the number of digits

class Solution:
    def armstrong(self,n):
        if n < 0:
            return False
        
        if n == 0 :
            return True 
        
        arm = n
        arm_sum = 0
        
        digit_count = 0
  
        while arm > 0 :

            digit_count+=1
            arm = arm//10
           
        arm = n 
        while arm > 0 :                       
            last_digit =  arm %10
            arm_sum += last_digit**digit_count
            arm = arm // 10
            
    
        return arm_sum == n 
    
result = Solution()
num = int(input("Enter number: "))
if result.armstrong(num) :
    print(f'{num} is an armstrong') 
else:
    print(f'{num} is not an armstrong') 