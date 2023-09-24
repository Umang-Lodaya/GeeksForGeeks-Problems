from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
    	a = Counter(arr)
        L = []
        
        for i in a.keys():
            if a.get(i) > 1:
                L.append(i)
        
        return sorted(L) if len(L) > 0 else [-1]
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends