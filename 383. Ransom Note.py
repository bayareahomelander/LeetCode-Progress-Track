class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        record = {}
        recordMagazine = {}
        
        for i in ransomNote:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1
        
        for i in magazine:
            if i not in recordMagazine:
                recordMagazine[i] = 1
            else:
                recordMagazine[i] += 1

        for i in record:
            if i in recordMagazine and recordMagazine[i] >= record[i]:
                continue
            else:
                return False
        
        return True
        
'''
Time: O(n)
Space: O(n)
'''
