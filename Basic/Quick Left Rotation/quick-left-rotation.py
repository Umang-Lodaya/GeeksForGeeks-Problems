class Solution:
    def leftRotate(self, arr, k, n):
        # Your code goes here
        k=k%n
        temp = []
        # Storing in temp array till kth index
        for i in range(k):
            temp.append(arr[i])
        # Storing the remaining elements in order
        for i in range(k,n):
            arr[i-k]=arr[i]
        # appending the elements from temp to original array
        for i in range(n-k,n):
            arr[i]=temp[i-(n-k)]
        return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends