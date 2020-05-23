# time: O(N)
# extra-space: O(N)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        mna = [A[-1]]*len(A)
        
        for i in range(len(A)-2, -1, -1):
            mna[i] = min(A[i], mna[i+1])
            
        beg = None
        for i in range(0, len(A)):
            if mna[i] != A[i]:
                beg = i
                break

        if beg is None:
            return [-1]
            
        del mna
        
        mxa = [A[0]]*len(A)
        for i in range(1, len(A)):
            mxa[i] = max(A[i], mxa[i-1])
            
            
        end = None
        for i in range(len(A)-1, -1, -1):
            if mxa[i] != A[i]:
                end = i
                break
            
        return [beg, end]
            
        # print(mxa)
