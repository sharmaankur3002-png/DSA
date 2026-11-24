# Given an array of n elements. The task is to return the count of the number of odd numbers in the array.


class Solution :
    def countOdd(self,n):
        
        arr = []
        for i in range(n):
            arrelement = int(input(f"Enter number {i+1} :"))
            arr.append(arrelement)
        print("array :",arr)
            
        count = 0
            
        for num in arr  :
            if num % 2 != 0 :
                count += 1
            
        return count
            
        
        
def main():
    n = int(input("Enter array size:"))
    result = Solution()
    totalodd  = result.countOdd(n)
    print("Total Odd number in array :",totalodd)
    
    
    
if __name__ == "__main__":
    main()