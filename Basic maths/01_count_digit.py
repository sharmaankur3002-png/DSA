# You are given an integer n. You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

class solution:
    def count_num(self,n):
        
        if n == 0 :
            return 1
        n= abs(n)
        
        count = 0
        while(n>0):
            n= n//10
            count += 1
        return count

result = solution()
num = int(input("Enter number: "))
print(result.count_num(num))

            
                