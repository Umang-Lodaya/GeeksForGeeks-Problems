#User function Template for python3

class Solution:
    def nCr(self, n, r):
        if n < r: return 0
        
        def fact(m):
            res = 1
            while m > 0:
                res *= m
                m -= 1
            return res
        
        N = fact(n)
        R = fact(r)
        N_R = fact(n - r)
        
        ans = N // (R * N_R)
        return ans % ((10**9) + 7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends