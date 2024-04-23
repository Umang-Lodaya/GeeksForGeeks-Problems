#User function Template for python3
class Solution:
    def mullmat(self,a,b):
        p = [[0,0], [0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    p[i][j] += (a[i][k] * b[k][j]) % self.MOD
                    p[i][j] %= self.MOD
        
        return p
    
    def exponentiation(self, a, n):
        ans = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                ans = self.mullmat(ans, a)
            a = self.mullmat(a, a)
            n >>= 1
            
        return ans
    
    def firstElement (self, n):
        self.MOD = 1000000007
        a = [[1, 1],
             [1, 0]]
        p = self.exponentiation(a,n)
        
        return p[1][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends