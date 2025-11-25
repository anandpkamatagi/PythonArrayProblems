# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

# Examples: 

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.

# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.


if __name__ == "__main__": 
    def removeDuplicateUsingHashSet(arr):
        print(f"Given Array: {arr}")
        hs  = set(arr)
        return list(hs)
    # print(removeDuplicateUsingHashSet([1,2,2]))
    
    def removeDuplicateWithoutExtraMemory(arr):
        print(f"Given Array: {arr}")
        for i in range(len(arr)-1):
            if(arr[i] == arr[i+1]):
                del arr[i]
        print(f"after removing deplucates: {arr}")
        
    print(removeDuplicateUsingHashSet([1,2,2,1,3,4,5,4]))
