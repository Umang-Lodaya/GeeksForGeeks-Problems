#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[0 for j in range(m + 1)] for i in range(2)]
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[j % 2][i] = dp[(j - 1) % 2][i - 1] + 1
                else:
                    dp[j % 2][i] = max(dp[(j - 1) % 2][i], dp[j % 2][i - 1])
        
        return m + n - dp[n % 2][-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends