#User function Template for python3



class Solution:
    def minNumber(self, arr, n):
        s = 0; ans = 0
        for i in arr:
            s += i
        
        while not self.__isPrime(s):
            s += 1
            ans += 1
        
        return ans
        
    def __isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends