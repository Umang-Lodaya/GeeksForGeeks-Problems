from collections import Counter
class Solution:
	def topK(self, nums, k):
	    return [i for i,j in sorted([(i,j) for i,j in Counter(nums).items()],key=lambda x: (-x[1], -x[0]))[:k]]


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends