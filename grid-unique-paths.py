from math import factorial

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
	    if A == 1 or B == 1:
	        return 1
	        
        return (factorial(A + B - 2)//factorial(A-1))//factorial(B - 1)
