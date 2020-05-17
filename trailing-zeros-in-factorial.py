# from math import log10

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        ans = 0
        
        div = 5
        
        while A >= div:
            ans += A // div
            div *= 5
                
        # print(fs, ts)
        return ans
