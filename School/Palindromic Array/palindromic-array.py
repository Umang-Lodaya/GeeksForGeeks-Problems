# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    def p(N):
        return str(N) == str(N)[::-1]
    
    for i in arr:
        if not p(i): return False
    
    return True



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends