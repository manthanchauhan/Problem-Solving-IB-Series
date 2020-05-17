def gcd(x, b):
    if x == 0 or b == 0:
        return max(x, b)
        
    if x > b:
        return gcd(b, x%b)
    else:
        return gcd(x, b%x)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        
        for div in range(1, A+1):
            if not (A%div):
                if gcd(A//div, B) == 1:
                    return A//div
                
