class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()
        for i in emails:
            name, domain = i.split('@') 
            local = name.split('+')[0].replace('.', '')
            valid.add(local + '@' + domain)
        
        return len(valid)
      
'''
Time: O(n)
Space: O(n)
'''
