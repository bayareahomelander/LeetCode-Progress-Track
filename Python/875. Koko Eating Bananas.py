class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        output = r
        
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            
            for i in piles:
                hours += math.ceil(i / mid)
                
            if hours <= h:
                output = min(output, mid)
                r = mid - 1
            else:
                l = mid + 1
                
        return output
        
'''
Time: O(logn)
Space: O(1)
'''
