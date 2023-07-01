 #User function Template for python3
 
class Solution:
    def get_longest_subsequence_length(self, subseq_lengths, elements_set, num):
        # Check if the current number is already processed
        if num not in subseq_lengths:
            # Check if the previous number exists in the subsequence
            if num - 1 in subseq_lengths:
                # Calculate the length of subsequence until the current number
                return subseq_lengths[num - 1] + 1
            # Check if the previous number exists in the array
            elif num - 1 in elements_set:
                # Recursively calculate the length of subsequence until the previous number
                return self.get_longest_subsequence_length(subseq_lengths, elements_set, num - 1) + 1
            else:
                # Base case: No previous number found, current number forms a subsequence of length 1
                return 1
        else:
            # Current number already processed, return its length
            return subseq_lengths[num]

    def findLongestConseqSubseq(self, arr, n):
        max_length = 0
        subseq_lengths = {}  # Dictionary to store lengths of subsequences for each number
        elements_set = set(arr)  # Set for efficient membership check

        for num in arr:
            # Calculate the length of the subsequence until the current number
            subseq_lengths[num] = self.get_longest_subsequence_length(subseq_lengths, elements_set, num)
            max_length = max(max_length, subseq_lengths[num])

        return max_length

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends