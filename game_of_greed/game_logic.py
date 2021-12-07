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
            print(1)
    
        if collection[1] == 1 or collection[1] == 2:
            score += 100 * collection[1]
            print(1)
        
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
        
        # res = True 
  
        # test_val = list(collection.values())[0]
  
        # for ele in collection:
        #     if collection[ele] != test_val:
        #         res = False 
                
        # if res == True:
        #     score = 1500 
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