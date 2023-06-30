#User function Template for python3

def missingNumber(A, N):
    ans = N
    for i in range(len(A)):
        ans ^= (i+1)
        ans ^= A[i]
        
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends