#User function Template for python3

class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
            
        same, diff, mod = 0, k, 10**9 + 7
        
        for i in range(2, n + 1):
            same, diff = diff, ((same + diff) * (k - 1)) % mod
        
        return (same + diff) % mod



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends