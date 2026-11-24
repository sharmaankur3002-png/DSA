# Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing 
# / Non-decreasing) order. If the array is sorted then return True, else return False.


class Solution :
    def checkSort(self,arr):
        
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
                
        return True

def main():
    
    arr = list(map(int,input("Enter elements of Array :").split()))
    
    result = Solution()
    
    check = result.checkSort(arr)
    
    if check :
        print("Array is sorted!")
    else:
        print("Array is not sorted!")
    
    
    
if __name__ == "__main__":
    main()