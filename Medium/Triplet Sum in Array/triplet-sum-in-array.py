#User function Template for python3
class Solution:
    def find3Numbers(self, A, n, target):
        A = sorted(A)
        ans = 0
        
        for i in range(len(A)):
            j = i+1
            k = len(A) - 1
            while j < k:
                s = A[i] + A[j] + A[k]
                if s == target:
                    return True
                elif s > target:
                    k -= 1
                else:
                    j += 1
        
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends