# You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of 
# the two given numbers. Return the LCM of the two numbers.

class Solution:
    def lcm(self,n1,n2):
        
        if n1 ==0 or n2 == 0 :
            return 0
        
        n1 = abs(n1)
        n2 = abs(n2)
               
        big = n1*n2
        lcm = 1
        
        for i in range(max(n1,n2),big+1):
            if i % n1 == 0 and i % n2 == 0 :
                lcm = i
                break
    
        return lcm
    
result = Solution()
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
lcm = result.lcm(num1,num2) 
print(f'{num1} and {num2} lcm = {lcm} ') 