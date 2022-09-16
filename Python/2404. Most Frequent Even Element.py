class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        even = {}
        
        for i in nums:
            if i % 2 == 0:
                if i not in even:
                    even[i] = 1
                else:
                    even[i] += 1
        
        if not even:
            return -1
        
        flipped = {}
        
        for k,v in even.items():
            if v not in flipped:
                flipped[v] = [k]
            else:
                flipped[v].append(k)
                
        maxFreq = max(flipped.keys())
        
        return min(flipped[maxFreq])
      
'''
Time: O(n)
Space: O(n)
'''
