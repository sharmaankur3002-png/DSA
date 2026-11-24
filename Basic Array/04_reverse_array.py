# Given an array arr of n elements. The task is to reverse the given array. The reversal of array 
# should be inplace.


class Solution :
    def reverseArray(self,arr):
        left = 0
        right = len(arr)-1
        
        while right > left :
            arr[left],arr[right] = arr[right],arr[left]
            
            left+=1
            right-=1
        
        return arr
            
def main():
    
    arr = list(map(int,input("Enter elements of Array :").split()))
    
    result = Solution()
    
    check = result.reverseArray(arr)
    
    print(check)
    
   
if __name__ == "__main__":
    main()