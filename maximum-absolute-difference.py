class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A) < 1:
            return -1
            
        alp = [A[i] + i for i in range(0, len(A))]
        bet = [A[i] - i for i in range(0, len(A))]
        
        a1 = max(alp) - min(alp)
        a2 = max(bet) - min(bet)
        
        return max(a1, a2)
