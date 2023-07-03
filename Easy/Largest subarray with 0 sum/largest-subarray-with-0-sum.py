#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_length = 0
        sum = 0
        hashmap = {}
        for i in range(n):
            
            sum += arr[i]
            if sum == 0:
                max_length = i+1
                
            elif sum in hashmap:
                max_length = max(max_length,i-hashmap[sum])
                
            else:
                hashmap[sum] = i
        return max_length


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends