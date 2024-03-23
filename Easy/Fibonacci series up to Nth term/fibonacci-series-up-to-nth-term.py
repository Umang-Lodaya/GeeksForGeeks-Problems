#User function Template for python3

class Solution:
    def series(self, n):
        mod = 10 ** 9 + 7
        
        ans = [0, 1]
        t1, t2 = 0, 1
        
        for i in range(2, n + 1):
            temp = (t1 + t2) % mod
            ans.append(temp)
            t1 = t2
            t2 = temp
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends