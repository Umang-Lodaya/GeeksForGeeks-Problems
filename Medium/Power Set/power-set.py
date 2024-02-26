#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        m = len(s)
        ans = []
        
        def dfs(idx = m - 1):
            nonlocal s, ans
            if idx < 0:
                return
            
            tmp = []
            for prv in ans:
                tmp.append(s[idx] + prv)
            
            tmp.append(s[idx])
            ans.extend(tmp)
            dfs(idx - 1)
            
        dfs()
        return sorted(ans)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends