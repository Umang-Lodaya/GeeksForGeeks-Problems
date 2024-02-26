#User function Template for python3

class Solution:
    def isDivisibleBy10(self, b):
        # ODD
        if b[-1] == '1':
            return 0
        
        n = int(b, 2)
        n = str(n)
        return 1 if n[-1] == '0' else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        bin=input()
        ob=Solution()
        print(ob.isDivisibleBy10(bin))
# } Driver Code Ends