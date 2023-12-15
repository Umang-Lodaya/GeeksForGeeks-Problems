#User function Template for python3

class Solution:
	def nthPoint(self, n):
	    MOD = 10**9 + 7
	    if n <= 2:
	        return n
	    c = 0
	    a = 1; b = 1
	    
	    for i in range(2, n + 1):
	        c = a % MOD + b % MOD
	        c %= MOD
	        a = b
	        b = c
	        
	    return c % MOD
	    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends