class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        mi = 0
        ans = 0
        
        for ai in A:
            mi = max(mi + ai, 0)
            ans = max(mi, ans)
            
        if not ans:
            return max(A)
            
        return ans
