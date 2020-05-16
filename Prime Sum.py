class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        # let the primes be x, y
        # thus, x + y = n
        # 1. since x, y are primes: x, y >= 2
        # 2. also either of x, y <= n/2
        
        # approach:
        # for each number 'num' in 2 to n/2:
        #   if num is prime:
        #       if n - num is prime:
        #           return [num, n - num]
        
        # else return [](empty list)
        
        # to check for primeness 'Prime Sieve' is used
        sv = [True]*(A)
        sv[0], sv[1] = False, False
        
        for i in range(2, A):
            if not sv[i]:
                continue
            
            j = i*2
            while j <= A-1:
                sv[j] = False
                j += i
                
        # print(sv)
        for i in range(0, A//2+1):
            if not sv[i]:
                continue
            
            if not sv[A-i]:
                continue
            
            return [i, A-i]
        
        return []
