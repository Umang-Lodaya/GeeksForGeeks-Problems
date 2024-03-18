#User function Template for python3

class Solution:
    def count (self, s):
        caps = 0; lows = 0; spec = 0; num = 0
        
        for i in s:
            if not i.isalnum():
                spec += 1
            else:
                if i.isupper():
                    caps += 1
                elif i.islower():
                    lows += 1
                else:
                    num += 1
        
        return caps, lows, num, spec


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends