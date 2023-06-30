#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        def GCD(x, y):
            if y == 0: return x
            return GCD(y, x%y)
        
        G = GCD(max(A, B), min(A, B))
        L = (A * B) // G
        return L, G


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends