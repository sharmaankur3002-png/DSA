# You are given an integer n. Return the largest digit present in the number.


class solution :
    def largest(self,n):
        large = 0
        
        n = abs(n)
        
        while(n>0):
            last = n%10
            
            if last > large :
                large = last
            
            n = n//10
        return large
    
result = solution()
num = int(input("Enter number: "))
print( f"largest number = {result.largest(num)}" )      