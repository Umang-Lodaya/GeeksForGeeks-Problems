#User function Template for python3

class Solution:
    def numberSequence(self, m, n):
        return self.solve(n, m)
        
    def solve(self, n, m):
        if m < n:  return 0
        if n == 0: return 1
        t = self.solve(n - 1, m // 2)
        nt = self.solve(n, m - 1)
        return t + nt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        arr = input().split()
        m = int(arr[0])
        n = int(arr[1])
        
        ob = Solution()
        print(ob.numberSequence(m, n))
# } Driver Code Ends