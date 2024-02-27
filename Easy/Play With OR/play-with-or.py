#User function Template for python3

class Solution:
    def game_with_number(self, arr, n) : 
        ans = []
        for i in range(n):
            a = arr[i]
            if i == n - 1:
                ans.append(a)
                break
            
            b = arr[i + 1]
            # print(i, a, b)
            OR = a | b
            ans.append(OR)
        
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends