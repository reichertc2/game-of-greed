import random
from collections import Counter

class GameLogic:
    
    @staticmethod
    def calculate_score(rolled_dice):
        start = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        collection = dict(Counter(rolled_dice))
        collection = {**start, **collection}
        score = 0
        
        if collection[5] == 1 or collection[5] == 2:
            score += 50 * collection[5]
            
    
        if collection[1] == 1 or collection[1] == 2:
            score += 100 * collection[1]
            
        
        # Check for 3 of a kind 
        for i in range(1,7):
            if i == 1 and collection[1] == 3:
                score += 1000
                
            if i != 1 and collection[i] == 3:   
                score += i * 100
                
        # Check for 4 of a kind
        for i in range(1,7):
            if i == 1 and collection[1] == 4:
                score += 2000
                
            if i != 1 and collection[i] == 4:   
                score += i * 200
        
        # Check for 5 of a kind
        for i in range(1,7):
            if i == 1 and collection[1] == 5:
                score += 3000
                
            if i != 1 and collection[i] == 5:   
                score += i * 300
        
        # Check for 6 of a kind
        for i in range(1,7):
            if i == 1 and collection[1] == 6:
                score += 4000
                
            if i != 1 and collection[i] == 6:   
                score += i * 400
        

        if collection[1] == 1 and collection[2] == 1 and collection[3] == 1 and collection[4] == 1 and collection[5] == 1 and collection[6] == 1:
            score = 1500
            
        count = 0 
        
        for i in range(1,7):
            if collection[i] == 2:
                count += 1
        if count == 3:
            score = 1500    
        
        
        return score
    
    
    
    
    @staticmethod
    def roll_dice(num_dice):
        rolls = []
        
        for _ in range(num_dice):
            roll = random.randint(1,6)
            rolls.append(roll)
        
        return tuple(rolls)
    
    @staticmethod
    def get_scorers(rolled_dice):
        start = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        collection = dict(Counter(rolled_dice))
        collection = {**start, **collection}
        output = []
        
        if collection[5] == 1 or collection[5] == 2:
            for _ in range(0, collection[5]):
                output.append(5)
            
    
        if collection[1] == 1 or collection[1] == 2:
            for _ in range(0, collection[1]):
                output.append(1)
            
        
        # Check for 3 of a kind 
        for i in range(1,7):
                
            if collection[i] == 3:   
                for _ in range(0, collection[i]):
                    output.append(i)
                
        # Check for 4 of a kind
        for i in range(1,7):
            if collection[i] == 4:   
                for _ in range(0, collection[i]):
                    output.append(i)
        
        # Check for 5 of a kind
        for i in range(1,7):
            if collection[i] == 5:   
                for _ in range(0, collection[i]):
                    output.append(i)
        
        # Check for 6 of a kind
        for i in range(1,7):
           if collection[i] == 6:   
                for _ in range(0, collection[i]):
                    output.append(i)
        

        if collection[1] == 1 and collection[2] == 1 and collection[3] == 1 and collection[4] == 1 and collection[5] == 1 and collection[6] == 1:
            output.append(1,2,3,4,5,6)
            
        count = 0 
        temp = []
        
        for i in range(1,7):
            if collection[i] == 2:
                count += 1
                temp.append(i)
                temp.append(i)
        if count == 3:
            output = temp 

        return output








#This is the test requirement
    # def test_validate_legal_keepers():
    # roll = (1, 2, 3, 4, 5)
    # keepers = (5, 1)
    # actual = GameLogic.validate_keepers(roll, keepers)
    # expected = True
    # assert actual == expected

    @staticmethod
    def validate_keepers(roll, keepers):
        start = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        roll_counted = dict(Counter(roll))
        possible_keepers = {**start, **roll_counted}
        # print(possible_keepers)

        legal_keepers = []
        kept_dice = []
        kept_dice_length = len(kept_dice)
        testing = True
        while testing:
            for die in possible_keepers:
                if possible_keepers.get(die) > 0:
                    legal_keepers.append(die)
                    # print('legal_keepers:', legal_keepers)
            # print(legal_keepers)
            for die in keepers:
                # print('die in second for loop:', die)
                if die in legal_keepers:
                    kept_dice.append(die)
                    if possible_keepers[die] <=0: 
                        testing = False
                        return False
                    possible_keepers[die] -= 1
                    # print('keepers: ',die)     
                    # print('possible_keepers :',possible_keepers)
                    True
                    kept_dice_length -= 1
                    
                else: 
                    # print('false die:',die)
                    testing = False
                    return False
            testing = False
        return True