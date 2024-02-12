#User function Template for python3

class Solution:
    def sequence(self, n):
        mod = 10**9+7
        ans = 0
        count = 1
        
        for i in range(1, n + 1):
            mul = 1
            for j in range(1, i + 1):
                mul = mul * count
                mul %= mod
                count += 1
                
            ans = (ans + mul) % mod
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends