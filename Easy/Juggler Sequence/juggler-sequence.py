#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        arr = []
        
        while n > 1:
            arr.append(n)
            if n % 2 == 1:
                n = int(n ** 1.5)
            else:
                n = int(n ** 0.5)
        
        return arr + [1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends