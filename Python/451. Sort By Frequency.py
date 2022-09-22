class Solution:
    def frequencySort(self, s: str) -> str:
        
        if len(s) == 1:
            return s
        
        record = {}
        output = ''
        
        for i in list(s):
            if i in record:
                record[i] += 1
            else:
                record[i] = 1
        
        record = dict(sorted(record.items(), key = lambda i: i[1], reverse = True))
        
        for k,v in record.items():
            output += k*v
        
        return output
        
'''
Time: O(nlogn)
Space: O(n)
'''
