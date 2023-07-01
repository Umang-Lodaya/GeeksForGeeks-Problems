#User function Template for python3

class Solution:
    def closest3Sum(self, A, N, X):
        res = 0; diff = float('inf')
        A.sort()
        
        for i in range(N-2):
            low = i + 1
            high = N - 1
            while low < high:
                s = A[i] + A[low] + A[high]
                if s == X:
                    return s
                elif s < X:
                    low += 1
                else:
                    high -= 1
                
                if abs(X - s) < diff:
                    diff = abs(X - s)
                    res = s
        
        return res
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        X = int(input())
        ob = Solution()
        print(ob.closest3Sum(Arr, N, X))
# } Driver Code Ends