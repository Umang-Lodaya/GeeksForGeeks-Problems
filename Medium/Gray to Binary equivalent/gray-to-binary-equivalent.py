#User function Template for python3

class Solution: 
    def grayToBinary(self, n):
        b = bin(n)[2:]
        prev = int(b[0])
        res = str(prev)
        
        for i in range(1, len(b)):
            t = prev ^ int(b[i])
            res += str(t)
            prev = t
        
        return int(res, 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends