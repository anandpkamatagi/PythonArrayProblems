# Given an array arr[] of size n, the task is to rearrange it in alternate positive and negative manner without changing the relative order of positive and negative numbers. In case of extra positive/negative numbers, they appear at the end of the array.

# Note: The rearranged array should start with a positive number and 0 (zero) should be considered as a positive number.

# Examples: 

# Input:  arr[] = [1, 2, 3, -4, -1, 4]
# Output: arr[] = [1, -4, 2, -1, 3, 4]

# Input:  arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output: arr[] = [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]

if __name__ == "__main__":
     def rearrange(array):
        pos = []
        neg = []
        newArray = []
        for a in array:
            if a < 0:
                neg.append(a)
            else:
                pos.append(a)
                
        print(pos)
        print(pos)
              
        i = 0
        while  i< len(pos)  and i< len(neg):
             newArray.append(pos[i])
             newArray.append(neg[i])
             i+=1
             print(newArray)
             
        while  i< len(pos):
             newArray.append(pos[i])
             i+=1
        
        while  i< len(neg):
             newArray.append(neg[i])
             i+=1
        print(newArray)
    
     rearrange([1,2,3,-4,-2,-1,-10,-13,-14])
        
         
