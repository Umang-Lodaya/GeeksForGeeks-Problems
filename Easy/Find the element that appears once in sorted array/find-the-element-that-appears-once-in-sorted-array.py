#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        ans = -1
        low = 0; high = n - 1
        if len(arr) == 1: return arr[0]
        if arr[0] != arr[1]: return arr[0]
        if arr[-2] != arr[-1]: return arr[-1]
        
        while low <= high:
            mid = low + (high - low) // 2
            if mid % 2 == 0:
                if mid < n - 1 and arr[mid] == arr[mid + 1]:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if mid >= 0 and arr[mid] == arr[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return arr[low]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends