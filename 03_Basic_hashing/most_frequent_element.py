# Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum
# number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.


class Solution :
    def most_frequent_element(self,arr):
        
        if not arr :
            return None
        
        max_count = {}
        
        
        #found the frequence of all element
        
        for num in arr :
            max_count[num] = max_count.get(num, 0) + 1
            
        
        maximum = max(max_count.values()) 
        
        #found the smallest number with highest frequency
        
        minimum_number = min(num for num,count in max_count.items() 
                             if count == maximum )
        
        return minimum_number
                                     
def main():
    
    arr =[]
    n = int(input("Enter size of array : "))
    
    for i in range (n) :
        num = int(input("Enter number :"))
        
        if num < 0 :
            print("Please give positive number!")
            return
        
        arr.append(num)
    
    result = Solution()
    max_occur = result.most_frequent_element(arr)
    print("Most Frequent Element:",max_occur)
    
    
if __name__ == "__main__" :
    main()