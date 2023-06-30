#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        arr.reverse()
        arr[:n-d] = reversed(arr[:n-d])
        arr[n-d:n] = reversed(arr[n-d:n])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends