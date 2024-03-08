#User function Template for python3
class Solution:
    def all_equal(self, list1):
        return all(x == list1[0] for x in list1)
        
    def check(self, z):
        m = max(z)
        index = z.index(m)
        z[index] = z[index] - 1
        return self.all_equal(z)
        
    def sameFreq(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
            
        z = list(d.values())
        c = self.all_equal(z) or self.check(z)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends