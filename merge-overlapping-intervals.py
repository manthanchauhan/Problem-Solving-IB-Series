# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def overlap(i, ni):
    if ni.end == i.start or i.end == ni.start:
        return True
        
    if ni.start == i.start and ni.end == i.end:
        return True
        
    if i.start > ni.start and i.end < ni.end:
        return True
        
    if i.start < ni.start and i.end > ni.end:
        return True
        
    if ni.start < i.end <= ni.end:
        return True
        
    if i.start < ni.end <= i.end:
        return True

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        ans = []
        
        while intervals:
            i = intervals[0]
            intervals.pop()
            # print(i.start, i.end)
            l = i
            
            while intervals:
                i_ = intervals[0]
                print(l.start, l.end, i_.start, i_.end)
                
                if overlap(i_, l):
                    if i_.end >= l.end:
                        l = i_
                        
                    intervals.pop()
                    
                else:
                    break
            
            newI = Interval(i.start, l.end)
            ans.append(newI)
            
        return ans

