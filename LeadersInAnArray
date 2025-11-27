if __name__ == "__main__":
    def findLeader_Bruetforce(arr):
        print(f"given array {arr}")
        print("finding leader by brute force")
      
        leader = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[i] < arr[j]):
                    break
                if(j == len(arr)-1):
                    leader.append(arr[i])
        leader.append(arr[i])
        return  leader
        
    def findLeaders_reverse_traverse(arr):
        print(f"given array {arr}")
        print("finding leader by reverse traversing")
        maxRight = arr[-1]
        leader = []
        leader.append(arr[-1])
        
        for i in range (len(arr)-2,-1,-1):
            if(arr[i] > maxRight):
                leader.append(arr[i])
                maxRight =arr[i]
                
        # Reverse the Array since we added elements from right to left
        leader.reverse()
        return  leader
                
        
    print(findLeader_Bruetforce([16, 17, 4, 3, 5, 2]))
    print(findLeaders_reverse_traverse([16, 17, 4, 3, 5, 2]))
    
    
    
    print(findLeader_Bruetforce([1, 2, 3, 4, 5, 2]))
    print(findLeaders_reverse_traverse([1, 2, 3, 4, 5, 2]))
    
