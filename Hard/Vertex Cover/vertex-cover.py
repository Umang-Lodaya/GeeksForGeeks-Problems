from typing import List


class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        from collections import defaultdict
        from itertools import combinations
        
        ve = defaultdict(set)
        
        for i, e in enumerate(edges):
            u, v = e
            ve[u - 1].add(i)
            ve[v - 1].add(i)
            
        numedges = len(edges)
        
        def ok(lim):
            nonlocal ve, numedges, n
            for comb in combinations([*range(n)], lim):
                seen = set()
                for ele in comb:
                    for i in ve[ele]:
                        seen.add(i)
                        if len(seen) == numedges:
                            return True
            
            return False
        
        l = 0
        r = n + 1
        
        while l < r:
            m = l + (r - l)//2
            if ok(m):
                r = m
            else:
                l = m + 1
                
        return l
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends