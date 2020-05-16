class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ''
        
        while A:
            d = A%26
            A //= 26
    
            if d == 0:
                A -= 1
                ans = 'Z' + ans
            else:
                ans = chr(64+d) + ans
        
        return ans
