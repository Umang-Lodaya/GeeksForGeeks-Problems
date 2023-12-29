#User function Template for python3
class Solution:
	def kSubstrConcat(self, n, s, k):
		if n % k != 0:
		    return 0
		
		sett = set()
		e = k
		for i in range(0, n - k + 1, k):
		    sub = s[i:e]
		    e += k
		    sett.add(sub)
		
		return 0 if len(sett) > 2 else 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends