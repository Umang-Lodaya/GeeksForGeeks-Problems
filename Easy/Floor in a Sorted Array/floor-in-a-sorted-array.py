class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, N, X):
        if arr[0] >= X: return -1
        if arr[-1] <= X: return N - 1
        
        l = 0; r = N - 1
        ans = N - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] <= X:
                ans = mid
                l = mid + 1 
            else:
                r = mid - 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends