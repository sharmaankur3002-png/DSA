# You are given an integer n. You need to return the number of odd digits present in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

class solution:
    def odd(self,n):
        
        if n == 0 :
            return 0
        
        n = abs(n)
        count = 0
        
        while(n>0):
            
            digit = n % 10
            
            if digit % 2 != 0:
                count+=1

            n = n//10
        return count    
        
result = solution()
num = int(input("Enter number: "))
print(result.odd(num))            