#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        count = 0
        string = str(N)
        for i in string :
            if i == '0' :
                pass
            elif N % int(i) == 0 :
                count += 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends