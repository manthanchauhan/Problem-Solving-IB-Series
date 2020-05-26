class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        # create an array from A, of type: [(0, A[0]), (1, A[1]), (2, A[2]), ... ]
        tups = list(enumerate(A))
        
        # sort the array on the basis of A[i]'s
        # so that for each i, possible j's will lie on the right of it for sure
        tups.sort(key=lambda x: x[1])
        
        # create an empty array to store max possible j for each i
        j = [tups[-1][0]]*len(A)
        
        # for the biggest A[i] (last element of `tups` array)
        # the one possible value of j, is i itself
        
        # for every other A[i] (except the last one)
        # max possible j is max(i, <max j on it's right>)
        # or simply, max(i, <max j of A[i+1]>)
        for i in range(len(A)-2, -1, -1):
            j[i] = max(tups[i][0], j[i+1])
            
        # now when the array "j" contains max possible j for each i,
        # simply find the max possible value of j-i
        ans = 0
        for i in range(0, len(A)):
            ans = max(ans, j[i] - tups[i][0])
            
        return ans
        
        
