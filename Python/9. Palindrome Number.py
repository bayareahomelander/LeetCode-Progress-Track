class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

'''
Time: O(n) -> Comparison takes in every letter in a String and here length is arbitrary.
Space: O(1)
'''
