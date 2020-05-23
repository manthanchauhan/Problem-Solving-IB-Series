# time: O(N logN)
# extra-space: O(1)

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        n = len(arrive)
        
        arrive.sort()
        depart.sort()
        
        # print(arrive, depart)
        
        occ = 0
        ai = 0
        di = 0
        
        # return True
        while (ai < n) or (di < n):
            # print(ai, di, n)
            if (ai < n) and (di < n):
                if arrive[ai] < depart[di]:
                    occ += 1
                    ai += 1
                elif arrive[ai] > depart[di]:
                    occ -= 1
                    di += 1
                else:
                    ai += 1
                    di += 1
                    
            elif ai < n:
                occ += 1
                ai += 1
            else:
                occ -=1
                di += 1
                
            if occ > K:
                return False
        
        return True
                
