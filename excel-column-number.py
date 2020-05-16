class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ans = 0
        
        for c in A:
            ans *= 26
            ans += ord(c) - 64
            
        return ans
