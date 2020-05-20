# time: O(I)
# extra-space: O(I)
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

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        f = None
        fi = None
        l = None
        li = None
        ni = new_interval
        ix = 0
        
        for ind, i in enumerate(intervals):
            if i.start < ni.start:
                ix += 1
                
            if (f is None) and overlap(i, ni):
                f = i
                fi = ind
            if (f is not None) and not overlap(i, ni):
                    l = intervals[ind-1]
                    li = ind-1
                    break
                
        # print (fi, li)
        # print(f.start, l.start)
        # print(ni.start, ni.end)
        
        if f is None:
            return intervals[:ix] + [ni] + intervals[ix:]
            
        if l is None:
            l = intervals[-1]
            
        newI = Interval(min(f.start, ni.start), max(l.end, ni.end))
        return intervals[:fi] + [newI] + intervals[li+1:]
