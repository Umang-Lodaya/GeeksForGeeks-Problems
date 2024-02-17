
class Solution:
    def isMaxHeap(self, arr, n):
        for i in range(n // 2):
            if (2 * i + 1 < n and arr[i] < arr[2 * i + 1]) or (2 * i + 2 < n and arr[i] < arr[2 * i + 2]):
                return False
        
        return True



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends