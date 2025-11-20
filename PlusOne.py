# Given a non-negative number represented as an array of digits. The task is to add 1 to the number (increment the number represented by the digits by 1). The digits are stored such that the most significant digit is the first element of the array.

# Examples :

# Input : [1, 2, 4]
# Output : 125
# Explanation: 124 + 1 = 125 

# Input : [9, 9, 9]
# Output: 1000
# Explanation: 999 + 1 = 1000 



if __name__ == "__main__":
    def plusone(arr):
        
        
        print(f"Given array {arr}")
        if(len(arr) == 0):
            return None
        if(len(arr) == 1):
            if(arr[0] < 9):
                arr[0] +=1
                return arr
            if(arr[0] == 9):
                return [1,0]
        i = -1
        
        while (i > -(len(arr)+1) and arr[i] == 9):
               arr[i] = 0
               i -=1
        if (i == -(len(arr)+1)):
            return [1]+arr
        else:
            arr[i] += 1
            return arr
        
    print(plusone([]))
    print(plusone([4]))
    print(plusone([9]))
    print(plusone([1,2,3,4,5]))
    print(plusone([1,2,3,4,9]))
    print(plusone([9,9,9]))    
    
    
            
