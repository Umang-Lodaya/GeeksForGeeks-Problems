#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        dp = [0 for _ in range(n)]
        seen = {0: True}
        
        for i in range(1, n):
            x = dp[i - 1] - i
            if x > 0 and not seen.get(x, False):
                dp[i] = dp[i - 1] - i
            else:
                dp[i] = dp[i - 1] + i

            seen[dp[i]] = True
        
        return dp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends