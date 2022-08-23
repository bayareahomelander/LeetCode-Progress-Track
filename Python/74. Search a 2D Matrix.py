class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        
        for i in matrix:
            temp += i
        
        return target in temp
     
'''
Time: O(n)
Space: O(n)
'''
