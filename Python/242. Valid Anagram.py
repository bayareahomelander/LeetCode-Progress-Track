class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t)) # 'car' & 'rat' would be -> ['a', 'c', 'r'] & ['a', 'r', 't']

'''
Time: O(nlogn)
Space: O(n)
'''
