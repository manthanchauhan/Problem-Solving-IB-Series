class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = A < 0
        A = abs(A)
        Ar = 0
        
        while A:
            d = A%10
            A //= 10
            
            Ar *= 10
            Ar += d
            
        if neg:
            Ar *= -1
            
        return Ar
