import random
from collections import Counter

class GameLogic:
    
    @staticmethod
    def calculate_score(rolled_dice):
        if 5 in rolled_dice:
            score = 50
            return score   
        
    @staticmethod
    def roll_dice(num_dice):
        rolls = []
        
        for _ in range(num_dice):
            roll = random.randint(1,6)
            rolls.append(roll)
        
        return tuple(rolls)