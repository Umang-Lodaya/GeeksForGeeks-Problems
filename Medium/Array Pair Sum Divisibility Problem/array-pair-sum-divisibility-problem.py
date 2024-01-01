#User function Template for python3

class Solution:
	def canPair(self, nums, k):
		mapp = {i: 0 for i in range(k)}
		
		for i in nums:
		    key = i % k
		    mapp[key] += 1
		
		if mapp[0] % 2 != 0:
    	    return False
	
	    del mapp[0]
		
		for key, v in mapp.items():
		    if mapp[key] != mapp[k - key]:
		        return False
		
		return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends