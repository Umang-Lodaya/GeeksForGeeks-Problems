#User function Template for python3
class Solution:
    def maximumSumSubarray (self, K, arr, N):
        ans = 0
        for i in arr[:K]:
            ans += i
        
        x = ans
        j = 0
        for i in range(K, N):
            x += (arr[i] - arr[j])
            ans = max(ans, x)
            j += 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends