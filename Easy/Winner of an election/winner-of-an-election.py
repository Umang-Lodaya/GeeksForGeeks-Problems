#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self, arr, n):
        votes = {}
        for cand in arr:
            votes[cand] = votes.get(cand, 0) + 1
            
        votes = [[votes[i], i] for i in votes]
        
        l = sorted(votes, key = lambda x: (-x[0], x[1]))
        return l[0][::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends