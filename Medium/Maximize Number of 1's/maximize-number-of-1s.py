#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    ones = 0; zeros = 0
    left = 0; right = 0
    while right < n:
        if arr[right] == 0:
            zeros += 1
        if zeros > m:
            if arr[left] == 0:
                zeros -= 1
            left += 1
        
        ones = max(ones, right - left + 1)
        right += 1
    
    return ones


#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends