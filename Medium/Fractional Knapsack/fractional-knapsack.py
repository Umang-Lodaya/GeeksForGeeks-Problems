#User function Template for python3

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Solution:
    def fractionalknapsack(self, W, arr, n):
        vpw = []
        for i in range(len(arr)):
            vpw.append((arr[i].value / arr[i].weight, i))
        
        vpw.sort(reverse = True)
        
        ans = 0.0
        for i in vpw:
            ii = i[1]
            if arr[ii].weight <= W:
                ans += arr[ii].value
                W -= arr[ii].weight
            else:
                ans += i[0] * W
                break
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends