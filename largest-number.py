# time: O(n logN)
# extra-space: O(N)
import functools

def comp(n1, n2):
    # if n1 > n2:
    #     return -1
    # else:
    #     return 1
    n1 = str(n1)
    n2 = str(n2)
    n1, n2 = n1+n2, n2+n1
    
    l1 = len(n1)
    l2 = len(n2)
    
    # print(n1, n2)
    
    i1, i2 = 0, 0
    
    while (i1 < l1) and (i2 < l2):
        # print(n1[i1], n2[i2])
        if n1[i1] > n2[i2]:
            return 1
        elif n1[i1] < n2[i2]:
            return -1
        
        i1 += 1
        i2 += 1
        
    if i1 < l1:
        # print(n1[i1], n1[0])
        if n1[i1] > n1[0]:
            return 1
        else:
            # print('hi')
            return -1
    elif i2 < l2:
        if n2[i2] > n2[0]:
            return -1
        else:
            return 1
    else:
        return 0

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, cmp=comp)
        A = A[::-1]
        # print(A)
        ans = ''
        
        for num in A:
            ans += str(num)

        return ans
        
