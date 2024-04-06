#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n):
            dp[i] += dp[i - 1]
        
        dp[1] += 1
        
        for i in range(2, n):
            dp[i] += dp[i - 2]
            
        return dp[n-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        ob = Solution()
        print(ob.countWays(n))

# } Driver Code Ends