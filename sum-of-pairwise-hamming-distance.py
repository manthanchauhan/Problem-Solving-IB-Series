from math import log2
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        ans = 0
        A = list(A)
        mx = max(A)
        n = len(A)
        MOD = 1000000007
        
        if mx == 0:
            mb = 1
        else:    
            mb = int(log2(mx)+1)
        
        for b in range(0, mb):
            zs = 0
            
            for i, num in enumerate(A):
                if not (num % 2):
                    zs += 1
                
                A[i] //= 2
                
            ans_ = (zs * (n - zs))%MOD
            ans = (ans + ans_)%MOD
            
        return (ans+ans)%MOD
                
        
