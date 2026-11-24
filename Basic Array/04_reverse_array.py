# Given an array arr of n elements. The task is to reverse the given array. The reversal of array 
# should be inplace.


class Solution :
    def reverseArray(self,arr):
        newarr=[]
        for i in range(len(arr)-1,-1,-1):
            newarr.append(arr[i])
            
        return newarr
            
def main():
    
    arr = list(map(int,input("Enter elements of Array :").split()))
    
    result = Solution()
    
    check = result.reverseArray(arr)
    
    print(check)
    
   
if __name__ == "__main__":
    main()