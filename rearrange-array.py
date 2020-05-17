from math import log

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        bs = int(log(A, 2)+1)
        
        mul = 2**bs
        
        for i, num in enumerate(A):
            A[i] += mul * (A[num]%mul)
            
        for i, num in enumerate(A):
            A[i] //= mul
            
        return A
