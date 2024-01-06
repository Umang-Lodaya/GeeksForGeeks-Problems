
from typing import List


class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        ans = 0
        prime = [1 for _ in range(b + 1)]
        prime[0] = prime[1] = 0
        i = 2
        while i * i <= b:
            if prime[i] == 1:
                for j in range(i*i, b + 1, i):
                    prime[j] = i
            i += 1
        
        for i in range(2, b + 1):
            if prime[i] == 1:
                prime[i] = i
        
        for i in range(a, b + 1):
            val = i
            while val > 1:
                val //= prime[val]
                ans += 1
        
        return ans



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends