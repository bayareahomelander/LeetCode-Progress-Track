class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num3 = sorted(nums1 + nums2) # Creating new merged sorted array.
        
        if len(num3) % 2 == 0: # If length is even, divide the sum by 2.
            median = (num3[len(num3) // 2] + num3[len(num3) // 2 - 1]) / 2
            return median
        
        else: # Else, return the number in the middle.
            return num3[len(num3) // 2]

'''
Time: O(nlogn)
Space: O(n)
'''
