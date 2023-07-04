#User function Template for python3

class Solution:
	def NthRoot(self, n, x):
	    if x == 1: return 1
        low = 1; high = x
        ans = 1
        while low <= high:
            mid = low + (high - low) // 2
            temp = 1
            for _ in range(n):
                temp *= mid
            if temp == x:
                return mid
            elif temp > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        
        temp = 1
        for _ in range(n):
            temp *= ans
        
        return ans if temp == x else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends