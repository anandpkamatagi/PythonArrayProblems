if __name__ == "__main__":
    def second_largest(arr):
        print(f"given Array: {arr}" )
        if(len(arr) < 2):
            return  -1
        arr.sort()
        return arr[-2]
            
    print(f"second Larget:{second_largest([1])}")
    
    print(f"second Larget:{second_largest([3,2])}")
    
    print(f"second Larget:{second_largest([3,2,5,7,6,8])}")