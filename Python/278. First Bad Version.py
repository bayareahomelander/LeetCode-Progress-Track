# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
      
'''
Time: O(logn)
Space: O(1)
'''
