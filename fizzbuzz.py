class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ans = [i for i in range(1, A+1)]
        
        for i, num in enumerate(ans):
            if num % 15 == 0:
                ans[i] = 'FizzBuzz'
            elif num % 5 == 0:
                ans[i] = 'Buzz'
            elif num % 3 == 0:
                ans[i] = 'Fizz'
            else:
                ans[i] = str(ans[i])
                
        return ans
