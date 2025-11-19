# Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array.

# Examples : 

# Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
# Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

# Input: arr[] = [0, 0, 1, 0, 1, 0]
# Output: 2
# Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.

# Input: arr[] = [0, 0, 0, 0]
# Output: 4
# Explanation: The maximum number of consecutive 0’s in the array is 4.



if __name__ == "__main__":
    
    def longestSequence(arr):
        print(f"Given binary Array : {arr} ")
        maxCount=1
        repeatCount=1
        if len(arr) < 2:
            return  1
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1]):
                repeatCount+=1
            else:
                repeatCount=1
            maxCount = max(repeatCount,maxCount)
        return maxCount
            
    print(longestSequence([0]))
    
    print(longestSequence([1]))
    
    print(longestSequence([0,1]))
    
    print(longestSequence([0,0]))
    
    print(longestSequence([1,1]))
    
    print(longestSequence([0, 1, 0, 1, 1, 1, 1]))
    
    print(longestSequence([0, 0, 1, 0, 1, 0]))
    
    print(longestSequence([0, 0, 0, 0]))
