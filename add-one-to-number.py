class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) < 1:
            return A
            
        lz = 0
        
        for d in A:
            if d == 0:
                lz += 1
            else:
                break
        
        A = A[lz:]
        
        if not A:
            A = [0]
            
        c = 1
        
        for i in range(len(A)-1, -1, -1):
            t = A[i] + c
            A[i] = t % 10
            c = t // 10
            
        if c:
            A = [c] + A
            
        return A
        
        
