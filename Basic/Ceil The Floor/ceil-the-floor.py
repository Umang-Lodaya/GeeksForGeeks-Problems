#User function Template for python3




def getFloorAndCeil(arr, N, X):
    f = -1; c = float('inf')
    for i in range(N):
        if f <= arr[i] and arr[i] <= X:
            f = arr[i]
        if X <= arr[i] and arr[i] <= c:
            c = arr[i]
    
    if c == float('inf'):
        c = -1
    
    return f, c


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends