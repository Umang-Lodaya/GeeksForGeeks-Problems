
#User function Template for python3

class Solution:
    def determinantOfMatrix(self, matrix, n):
        if n == 1:
            return matrix[0][0]
        
        def newMatrix(matrix, x):
            m = len(matrix)
            ans = []
            for i in range(1, m):
                ans.append(matrix[i][:x] + matrix[i][x+1:])
                
            return ans
            
        ans, sign = 0, 1
        for i in range(n):
            newM = newMatrix(matrix, i)
            ans += sign * matrix[0][i] * self.determinantOfMatrix(newM, len(newM))
            sign *= -1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends