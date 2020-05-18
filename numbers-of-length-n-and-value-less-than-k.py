# time: O(logC) [A can have at max 10 values]
# extra-space: O(logC) [to store digits of C]

from math import log10

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # count number of digits in decimal representation of C
        # No. of digits in decimal = Floor(log10(C) + 1)
        # No. of digits in binary = Floor(log2(C) + 1)
        dc = int(log10(C) + 1)
        
        # If B > digits in C
        # No number with B digits can be smaller than C
        if B > dc:
            return 0
            
        # If B < digits in C
        # Every number with B digits will be greater than C
        if B < dc:
            # count of all numbers with B digits is |A|^B
            # This may include numbers which have 0 as the most significant digit, i.e. 0120, 0012. We'll remove them later  
            ans = len(A)**B
            
            # if 0 is a possible digits (A has 0)
            # Remove numbers which have 0 as the most significant digit, except 0.

            if B != 1 and (0 in A):
                ans -= len(A)**(B-1)
                
            return ans

        # Now we'll handle cases where B == digits in C
        # initialize final count to 0    
        ans = 0

 	# keep all digits of C in an array, ds.
        # if C = 123
        # ds = [1, 2, 3]
        ds = []
        
        while C:
            ds.append(C%10)
            C //= 10
            
        ds = ds[::-1]
        # print(ds)

        # for each index i and digit d (ds[i])
        for i, d in enumerate(ds):
            # count the total candidates (from A) which can appear at the place value i
            # such that the number doesn't exceeds C
            c = 0
            
            # count the total candidates (from A) which are strictly less than d
            for ai in A:
                if ai < d:
                    c += 1
            
            # c is the count of such candidates
            # for each such candidate |A|^(B - i - 1) number are possible which are strictly less than C
            # add this count to final ans
            ans += c * (len(A)**(B - i - 1))
           
            # if d is not present at A
            # No more numbers < C are possible, so break the loop.
            if not (d in A):
                break
            

        # Remove numbers with 0 as the most significant digit.
        # i.e. 0122, 0012, 0001, 0000 (we'll keep '0')
        if B > 1 and (0 in A):
            ans -= len(A)**(B-1)

	# return the final ans
        return ans
        
