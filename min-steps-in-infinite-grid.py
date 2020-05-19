class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        if len(A) < 2:
            return 0
        ans = 0
        
        for i in range(0, len(A)-1):
            dia = min(abs(A[i] - A[i+1]), abs(B[i] - B[i+1]))
            
            ans += dia
            
            if A[i+1] > A[i]:
                A[i] += dia
            else:
                A[i] -= dia
                
            if B[i+1] > B[i]:
                B[i] += dia
            else:
                B[i] -= dia
                
            ans += max(abs(A[i] - A[i+1]), abs(B[i] - B[i+1]))
            
        return ans
