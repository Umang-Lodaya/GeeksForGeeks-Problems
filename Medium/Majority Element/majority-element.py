#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        e = A[0]
        c = 0
        for i in range(N):
            if c == 0:
                c = 1
                e = A[i]
            elif A[i] == e:
                c += 1
            else:
                c -= 1
        
        return e if A.count(e) > (N // 2) else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends