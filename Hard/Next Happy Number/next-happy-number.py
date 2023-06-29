#User function Template for python3


class Solution:
    def nextHappy (self, N):
        def check(n):
            if n in [1, 7]:
                return True
            if n in [2, 4, 8, 3, 9, 5, 6]:
                return False
            
            ss = list(str(n))
            ss = list(map(int, ss))
            ss = list(map(lambda x:x**2, ss))
            ss = sum(ss)
            return check(ss)
        
        while True:
            N += 1
            if check(N): return N

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends