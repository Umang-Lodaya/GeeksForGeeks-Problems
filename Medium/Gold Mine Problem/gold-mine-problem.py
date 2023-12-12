# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        def findmaxgold(i,j):
            if i<0 or i>=n or j>=m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = max(
                        findmaxgold(i,j+1),
                        findmaxgold(i-1,j+1),
                        findmaxgold(i+1,j+1)
                    ) + M[i][j]
            return dp[i][j]

        dp = [[-1]*m for i in range(n)]
        max_g = -1
        for i in range(n):
            max_g = max(findmaxgold(i, 0), max_g)
        return max_g


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends