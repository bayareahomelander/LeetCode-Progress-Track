class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        if len(bills) == 1:
            return True
        
        # Quantity of 20 bill is constant. Will not be given out as changes.
        fives = 0
        tens = 0
        
        for i in bills:
            if i == 5:
                fives += 1
            else:
                if i == 10: # If received a $10 bill, give out one $5 and increment quantity of $10 bills by 1.
                    tens += 1
                    fives -= 1
                elif i == 20: # If received a $20 bill:
                    if tens != 0: # If still have $10 bills left, give out one $10 and one $5.
                        tens -= 1
                        fives -= 1
                    else: # No $10 bills left, give out three $5 bills as change.
                        fives -= 3
            if fives < 0: # If true, means cannot provide each customer with correct change. End loop and return False.
                return False
        
        return True
        
'''
Time: O(n)
Space: O(1)
'''
