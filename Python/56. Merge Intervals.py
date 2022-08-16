class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]] # Edge case -> input array only contains one interval.
        
        for s, e in intervals[1:]:
            prev = output[-1][1] # Second number in each interval.
            
            if prev >= s:
                output[-1][1] = max(prev, e) # Second number in previous interval vs. First number in next interval
                                             # Take the maximum number to avoid cases like [[1,5],[2,4]]
            
            else:
                output.append([s,e]) # If not overlapped then append to Output.
        
        return output
        
'''
Time: O(nlogn)
Space: O(n)
'''
