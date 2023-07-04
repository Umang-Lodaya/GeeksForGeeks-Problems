#User function Template for python3
class Solution:
    def find(self, arr, n, x):
        if x < arr[0] or arr[-1] < x: return -1, -1
        
        first = n
        
        low = 0; high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                first = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                
        if first == n: return -1, -1
        
        last = 0
        low = 0; high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                last = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return first, last
        
	def count(self,arr, n, x):
		l, r = self.find(arr, n, x)
		if l == -1: return 0
		return r - l + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends