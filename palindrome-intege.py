from math import log10

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A_ = 0
        Ac = A
        
        if A == 0:
            return 1
        
        digs = int(log10(A) + 1)
        
        for d in range(0, digs):
            dig = Ac%10
            Ac //= 10
            
            A_ *= 10
            A_ += dig
            
        if A_ == A:
            return 1
        else:
            return 0
            
        
