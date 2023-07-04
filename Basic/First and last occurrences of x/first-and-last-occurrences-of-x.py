#User function Template for python3


def find(arr, n, x):
    if x < arr[0] or arr[-1] < x: return -1, -1
    
    first = n
    
    low = 0; high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    if first == n: return -1, -1
    
    last = 0
    low = 0; high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return first, last

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends