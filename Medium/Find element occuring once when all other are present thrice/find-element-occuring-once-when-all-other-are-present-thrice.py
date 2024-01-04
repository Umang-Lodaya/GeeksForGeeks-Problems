#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        
        for k, v in freq.items():
            if v == 1:
                return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends