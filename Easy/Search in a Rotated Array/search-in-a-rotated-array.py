#User function Template for python3

class Solution:
    def search(self, arr : list, l : int, h : int, x : int):
        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] <= arr[h]:
                if arr[mid] < x <= arr[h]:
                    l = mid + 1
                else:
                    h = mid - 1
            elif arr[l] <= arr[mid]:
                if arr[l] <= x < arr[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends