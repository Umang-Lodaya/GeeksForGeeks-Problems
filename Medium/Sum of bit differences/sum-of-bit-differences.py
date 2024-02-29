#User function Template for python3
class Solution:
	def sumBitDifferences(self, arr, n):
    	count = 0
    	for i in range(31, -1, -1):
    	    a = 0
    	    for j in range(n):
    	        a += (arr[j] >> i) & 1
    	    
    	    count += 2 * a * (n - a)
    	
    	return count



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends