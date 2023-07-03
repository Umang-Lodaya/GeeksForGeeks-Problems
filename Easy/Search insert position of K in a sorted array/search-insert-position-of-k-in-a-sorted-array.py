#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, X):
        l = 0; r = N - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == X:
                return mid
            elif arr[mid] < X:
                l = mid + 1
            else:
                r = mid - 1
        
        return r + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends