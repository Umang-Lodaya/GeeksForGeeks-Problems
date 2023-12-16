#User function Template for python3

class Solution:

    def countStr(self, n):
        case1 = 1 # all a
        case2 = n # one b
        case3 = n # one c
        case4 = n * (n - 1) # one b, one c
        case5 = case4 // 2 # two c
        case6 = case5 * (n - 2) # one b, two c
        
        return case1 + case2 + case3 + case4 + case5 + case6

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends