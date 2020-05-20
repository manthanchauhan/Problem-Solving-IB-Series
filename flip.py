# time: O(A)
# extra-space: O(1)

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        mi = 0
        ans = 0
        b = 0
        b_ = 0
        e = 0
        
        for i in range(1, len(A)+1):
            if A[i-1] == '0':
                mi += 1
                
                if mi > ans:
                    e = i
                    b = b_
                    ans = mi
            else:
                mi = max(mi-1, 0)
                
                if mi == 0:
                    b_ = i
                    
        if ans == 0:
            return []
            
        else:
            return [b+1, e]
