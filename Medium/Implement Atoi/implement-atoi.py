#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self, s):
        sign = 1
        if s[0] == "-":
            s = s[1:]
            sign = -1
            
        try:
            s = int(s)
        except:
            return -1
        
        return s * sign
        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends