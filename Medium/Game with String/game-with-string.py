#User function Template for python3

class Solution:
    def minValue(self, s, k):
        freq = [0] * 26
        
        for char in s:
            i = ord(char) - ord('a')
            freq[i] += 1
        
        freq.sort()
        
        for i in range(k):
            if not freq[-1]:
                break
            freq[-1] -= 1
            freq.sort()
        
        s = 0
        for i in freq:
            s += (i * i)
        
        return s
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends