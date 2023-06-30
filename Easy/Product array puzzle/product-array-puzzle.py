#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        P = 1
        ans = [1] * n
        for i in range(n):
            ans[i] = P
            P *= nums[i]
            
        P = 1
        for i in range(n-1, -1, -1):
            ans[i] *= P
            P *= nums[i]
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends