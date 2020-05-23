# time: O(N logN)
# extra-space: O(N)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        tups = list(enumerate(A))
        tups.sort(key=lambda x: x[1])
        
        j = [tups[-1][0]]*len(A)
        
        for i in range(len(A)-2, -1, -1):
            j[i] = max(tups[i][0], j[i+1])
            
        ans = 0
        for i in range(0, len(A)):
            ans = max(ans, j[i] - tups[i][0])
            
        return ans
        
        
