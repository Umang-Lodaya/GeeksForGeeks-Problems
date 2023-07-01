#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        di={}
        summ=0; maxi=0
        di[0] = -1
        
        for i in range(n):
            summ += arr[i]
            
            if summ-k in di.keys():
                maxi=max(maxi,i-di[summ-k])
            
            if summ not in di.keys():
                di[summ] = i
                
        return maxi



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends