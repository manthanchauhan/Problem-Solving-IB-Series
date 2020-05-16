def pfact(A, sv):
    if A == 1:
        return []
    root = int(A**0.5)
    f = None
    
    for i in range(2, root+1):
        if not sv[i]:
            continue
        
        if A%i == 0:
            f = i
            break
    
    if f is None:
        return [A]
        
    else:
        return [f] + pfact(A//f, sv)

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a 
        
    if a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)


def GCD(vals):
    if len(vals) == 1:
        return vals[0]
        
    g_ = GCD(vals[1:])
    return gcd(vals[0], g_)

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if not A:
            return 0
            
        if A == 1:
            return 1
        
        mx = int(A**0.5) + 1
        sv = [True]*mx
        sv[0] = False
        sv[1] = False
        
        for i in range(2, mx):
            if not sv[i]:
                continue
            
            j = i*i
            while j < mx:
                sv[j] = False
                j += i
                
        # print(sv)
            
        facts = pfact(A, sv)
        facts.sort()
        
        d = {facts[0]: 1}
        n = len(facts)
        
        for i in range(1, n):
            if facts[i] == facts[i-1]:
                d[facts[i]] += 1
            else:
                d[facts[i]] = 1
                
        # print(d)
        vals = list(d.values())
        
        if GCD(vals) > 1:
            return 1
        else:
            return 0
      
            
