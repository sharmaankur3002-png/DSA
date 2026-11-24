# Given an array arr of size n, the task is to find the sum of all the elements in the array.

class Solution :
    def sumarray(self,n):
        
        arr = []
        for i in range(n):
            arrelement = int(input(f"Enter number {i+1} :"))
            arr.append(arrelement)
        print("array :",arr)
            
        total = 0
            
        for j in range (len(arr)) :
            total+=arr[j]
            
        return total
            
        
        
def main():
    n = int(input("Enter array size:"))
    result = Solution()
    totalarr  = result.sumarray(n)
    print("Total sum of array :",totalarr)
    
    
    
if __name__ == "__main__":
    main()