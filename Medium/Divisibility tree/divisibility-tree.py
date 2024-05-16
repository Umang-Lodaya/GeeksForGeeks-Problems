
from typing import List


class Solution:
    def minimumEdgeRemove(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        
        for u, v in edges:
            adj[u - 1] = adj.get(u - 1, []) + [v - 1]
            adj[v - 1] = adj.get(v - 1, []) + [u - 1]
        
        ans = 0
        def dfs(adj, u, prt):
            nonlocal ans
            count = 0
            for v in adj.get(u, []):
                if v != prt:
                    x = dfs(adj, v, u)
                    if x % 2 == 0:
                        ans += 1
                    else:
                        count += x
            
            return count + 1
        
        dfs(adj, 0, -1)
        return ans
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends