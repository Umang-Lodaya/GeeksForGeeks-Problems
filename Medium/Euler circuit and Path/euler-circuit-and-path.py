class Solution:
    def isEulerCircuitExist(self, V, adj):
        degree = [0] * V
        
        for r in adj:
            for e in r:
                degree[e] += 1
        
        cnt = sum(1 for e in degree if e % 2 != 0)
        if cnt == 0:
            return 2
        if cnt <= 2:
            return 1
        return 0


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends