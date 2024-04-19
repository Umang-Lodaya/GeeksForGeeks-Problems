#User function Template for python3


class Solution:
    def findMissing(self, a, b, n, m):
        d = {}
        for i in b:
            d[i] = d.get(i, 0) + 1
            
        res = []
        for i in a:
            if not d.get(i, False):
                res.append(i)
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends