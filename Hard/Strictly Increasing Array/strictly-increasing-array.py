#User function Template for python3

class Solution:
    def min_operations(self,nums):
        n = len(nums)
        LIS = [1] * n  
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and (i - j) <= (nums[i] - nums[j]):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        return n - max(LIS)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends