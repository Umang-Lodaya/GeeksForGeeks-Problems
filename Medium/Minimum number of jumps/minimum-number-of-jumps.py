#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    s = 0; e = 0
	    count = 0
    
        for i in range(n - 1):
            s = max(s, i + arr[i])
            if i == e:
                count += 1
                e = s
                if e >= n - 1:
                    return count
    
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends