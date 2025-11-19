
# Given an integer array, find a maximum product of a triplet in the array.

# Examples: 

# Input:  arr[ ] = [10, 3, 5, 6, 20]
# Output: 1200
# Explanation: Multiplication of 10, 6 and 20

# Input:  arr[ ] =  [-10, -3, -5, -6, -20]
# Output: -90

# Input: arr[ ] =  [1, -4, 3, -6, 7, 0]
# Output: 168


if __name__ == "__main__":
    
    def findMaxTriplet(arr):
        if 0 in arr:
            return 0
        if (len(arr) <3):
            return -1
        arr.sort()
        return arr[-1] * arr[-2] * arr[-3] 
        
    print(findMaxTriplet([0,3]))
    
    print(findMaxTriplet([2,3,1,5]))
    
    print(findMaxTriplet([7,6,4,9,10]))
    
    print(findMaxTriplet([0,3]))
    
        
 
        
       
                
                
        
    
