#User function Template for python3
class Solution:
    def findMin(self, arr, n):
        mn = n - 1
        low = 0; high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            # print(low, mid, high, mn)
            if arr[low] <= arr[mid]:
                if arr[low] < arr[mn]:
                    mn = low
                low = mid + 1
            else:
                if arr[mid] < arr[mn]:
                    mn = mid
                high = mid - 1
        
        return mn
        
    def findKRotation(self, arr,  n):
        if arr[0] < arr[-1]: return 0
        return self.findMin(arr, n)
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends