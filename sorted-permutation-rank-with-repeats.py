mfact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 628791, 916683, 163, 2119, 29666, 444990, 119819, 36917, 664506, 625578, 511524, 741974, 323380, 437719, 505226, 630614, 395916, 689702, 311599, 36344, 90317, 799821, 594197, 608444, 687036, 46188, 662765, 522233, 844797, 946987, 879369, 54021, 268876, 561635, 711868, 33964, 562341, 429949, 637492, 237015, 850717, 386438, 94716]

def ans(A, cnts):
    myr = 0
    fact = mfact[len(A)-1]
    
    for c, cnt in cnts.items():
        if c < A[0]:
            f = fact
            
            for c_, cnt_ in cnts.items():
                if c_ != c:
                    f //= mfact[cnt_]
                else:
                    f //= mfact[cnt_-1]
            
            myr += f
            
    ans_ = myr
    
    if len(A) > 1:
        cnts[A[0]] -= 1
        ans_ += ans(A[1:], cnts)
        
    ans_ %= 1000003
        
    return ans_


class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        A = [c for c in A]
        cnts = {}
        
        for c in A:
            if c not in cnts:
                cnts[c] = 1
            else:
                cnts[c] += 1
                
        return ans(A, cnts)+1
       
