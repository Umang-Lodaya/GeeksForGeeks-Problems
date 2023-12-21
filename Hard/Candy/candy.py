#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        candy = [1 for _ in range(N)]
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            else:
                j = i
                while j > 0 and candy[j] >= candy[j - 1] and ratings[j] < ratings[j - 1]:
                    j -= 1
                    candy[j] += 1
        
        return max(0, sum(candy))
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends