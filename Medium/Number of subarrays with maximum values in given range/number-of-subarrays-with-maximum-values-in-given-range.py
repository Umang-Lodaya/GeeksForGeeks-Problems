#User function Template for python3

class Solution:
    def countSubarrays(self, a,n,L,R): 
        st = 0
        ans = 0
        emp = 0
        
        for i in range(n):
            if L <= a[i] <= R:
                emp = i - st + 1
            if a[i] > R:
                emp = 0
                st = i + 1
            ans += emp
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends