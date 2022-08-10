class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set() # Creating a hashSet for recording & searching. Not using Array because O(n) time complexity.
        
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        
        return False # Would reach this line if never found a duplicate after iterating.

'''
Time: O(n)
  -> Brute Force: .count() on each and every element and it'd be O(n^2)
  -> Sorting and checking: O(nlogn)

Space: O(n)
  -> Brute Force: O(1)
  -> Sorting: O(1)
  Both operate within the original array.
'''
