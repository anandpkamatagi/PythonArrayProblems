if __name__ == "__main__":
    
    def rotateArray(arr, position):
        
        print(arr)
        new_array = arr[position:] + arr[:position] 
        print(new_array)
        
    rotateArray([1,2,3,4,5,6],2)
