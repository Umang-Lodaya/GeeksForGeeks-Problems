#User function Template for python3

class Solution:
    def Solve(self, N, piles, H):
        low = 1; high = max(piles)
        while low <= high:
            mid = low + (high - low)//2
            if self.subfunction(mid, piles, H) > H:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
        
    def subfunction(self, speed, piles, H):
        answer = 0
        for fruits in piles:
            answer += (fruits + speed - 1)//speed
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends