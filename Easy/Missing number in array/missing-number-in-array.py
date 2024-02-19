#User function Template for python3


class Solution:
    def missingNumber(self, array, n):
        exp = n * (n + 1) // 2
        act = sum(array)
        return exp - act


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends