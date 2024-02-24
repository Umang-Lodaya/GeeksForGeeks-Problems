#User function Template for python3

class Solution:
    def maxSum(self, n): 
        dp = [-1 for i in range(n+1)]
        
        dp[0] = 0
        
        def recursiveMaxSum(n):
            if dp[n] != -1:
                return dp[n]
            else:
                if n < n//2 + n//3 + n//4:
                    dp[n] = recursiveMaxSum(n//2) + recursiveMaxSum(n//3) + recursiveMaxSum(n//4)
                    return dp[n]
                else:
                    dp[n] = n
                    return dp[n]
        
        res = recursiveMaxSum(n)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends