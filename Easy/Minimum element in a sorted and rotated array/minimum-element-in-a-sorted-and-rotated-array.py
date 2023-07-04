#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        mn = float('inf')
        low = 0; high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if arr[low] <= arr[mid]:
                mn = min(mn, arr[low])
                low = mid + 1
            else:
                mn = min(mn, arr[mid])
                high = mid - 1
        
        return mn


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends