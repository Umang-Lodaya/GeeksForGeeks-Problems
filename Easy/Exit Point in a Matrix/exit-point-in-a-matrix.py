#User function Template for python3

class Solution:
    
    def FindExitPoint(self, n, m, matrix):
        prow = -1
        pcol = -1
        row = 0
        col = 0
        
        while 0 <= row < n and 0 <= col < m:
            slope_r = row - prow
            slope_c = col - pcol
            
            prow = row
            pcol = col
         
            if matrix[row][col]==0 and slope_r==1 and slope_c==1:
                row = row
                col = col+1;
                
            elif matrix[row][col]==1 and slope_r==1 and slope_c==1:
                matrix[row][col] = 0
                row = row+1;
                col = col
                
            else:
                if matrix[row][col]==0:
                    if slope_r == 0 and slope_c==1:
                        row = row;
                        col = col+1;
                        
                    elif slope_r==1 and slope_c==0:
                        row+=1;
                        col = col
                        
                    elif slope_r==0 and slope_c == -1:
                        row = row;
                        col-=1;
                        
                    else:
                        row-=1;
                        col = col;
                        
                else:
                    matrix[row][col] = 0
                    if slope_r == 0 and slope_c==1:
                        row = row+1;
                        col = col;
                        
                    elif slope_r==1 and slope_c==0:
                        row=row;
                        col = col-1
                        
                    elif slope_r==0 and slope_c == -1:
                        row = row-1;
                        col=col;
                        
                    else:
                        row = row;
                        col = col+1;
            
        return [prow , pcol]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends