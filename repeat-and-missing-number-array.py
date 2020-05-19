class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        if len(A) < 2:
            return A
            
        n = len(A)
        
        sg = (n*(n+1))//2
        ssg = (n*(n+1)*(2*n +1))//6
        
        s = 0
        for n in A:
            s += n
            
        ss = 0
        for n in A:
            ss += n**2
            
        diff = s - sg
        d2 = ss - ssg
        add = d2 // diff
        
        a = (diff + add)//2
        b = add - a
        
        return [a, b]
