from math import log10

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dc = int(log10(C) + 1)
        
        if B > dc:
            return 0
            
        if B < dc:
            ans = len(A)**B
            
            if B != 1 and (0 in A):
                ans -= len(A)**(B-1)
                
            return ans
            
        ans = 0
        ds = []
        
        while C:
            ds.append(C%10)
            C //= 10
            
        ds = ds[::-1]
        # print(ds)
        for i, d in enumerate(ds):
            c = 0
            
            for ai in A:
                if ai < d:
                    c += 1
            # print(d, c)            
            ans += c * (len(A)**(B - i - 1))
            # print(d, ans)
            if not (d in A):
                break
            
        if B > 1 and (0 in A):
            ans -= len(A)**(B-1)
        return ans
        
