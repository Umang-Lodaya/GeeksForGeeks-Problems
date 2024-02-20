#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # create a dictionary to store words from the dictionary list
        dic = {}
        # iterate through the words in the dictionary list
        for i in dictionary:
            if i in s:
                dic[i[0]] = dic.get(i[0], []) + [i]
        
        # print(*dic.items(), sep = "\n")
        
        def solve(st, k,  dp):
    
            if len(st) == k:
                return True
            
            elif dp[k] != None:
                return  dp[k]
            
            elif st[k] in dic:
                for i in dic[st[k]]:
                    if len(i)<=len(st[k:]):
                        if st[k: k + len(i)] == i:
                            k += len(i)
                            rt = solve(st,k, dp)
                            if rt:
                                dp[k] = True
                                return True
                            else:
                                k -= len(i)
    
            #     dp[k] = False
            #     return False     
            # else:
            dp[k] = False
            return False
    
        dp = [None] * (len(s) + 1)
        k = 0
        res = solve(s, k,  dp)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends