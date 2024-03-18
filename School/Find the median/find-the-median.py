#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		n = len(v)
		
		if n % 2 == 1:
		    mid = n // 2
		    return v[mid]
		else:
		    m1 = n // 2 - 1
		    m2 = m1 + 1
		    return (v[m1] + v[m2]) // 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends