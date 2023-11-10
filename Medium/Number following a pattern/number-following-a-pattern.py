#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob, S):
        result = ""
        stack = []
        n = len(S)
        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or S[i] == 'I':
                while stack:
                    result += str(stack.pop())
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends