#User function Template for python3
class Solution:
	def setBits(self, N):
		ans = 0
		while N != 0:
		    ans += N & 1
		    N = N >> 1
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends