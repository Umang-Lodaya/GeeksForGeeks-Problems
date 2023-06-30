class Solution:
    def smallestSubWithSum(self, arr, n, x):
        mx = 0
        l = 0; r = 0
        ans = float('inf')
        
        while r < n:
            mx += arr[r]
            r += 1
            while mx > x:
                ans = min(ans, r-l)
                mx -= arr[l]
                l += 1
                
        return 0 if ans == float('inf') else ans
#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends