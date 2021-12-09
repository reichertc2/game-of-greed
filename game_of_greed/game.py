from collections import Counter
from os import stat
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self, round = 1, dice_num = 6):
        self.round = round
        self.dice_num = dice_num
        self.status = True
        self.banker = Banker()

        
    def play(self, roller):
        # Print introduction and check if user wants to play if so start game
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        
        if user_input == "n":
            print("OK. Maybe another time")
            
        if user_input == "y":
            while self.status == True:
                self.dice_num = 6
                self.round_start(roller)
            
            
                
    def round_start(self, roll):
        
 
        self.status = False
        print(f"Starting round {self.round}")
        def rolling():
            user_roll = roll(self.dice_num)
            
            roll_num = " ".join(str(i) for i in user_roll)
            print(f"Rolling {self.dice_num} dice...")
            print(f"*** {roll_num} ***")
            if GameLogic.get_scorers(tuple(user_roll)) == []:
                self.banker.clear_shelf()
                print("""****************************************
**        Zilch!!! Round over         **
****************************************""")     
                print(f"You banked 0 points in round {self.round}")   
                print(f"Total score is {self.banker.balance} points")            
                self.round += 1
                self.dice_num = 6
                self.round_start(roll)
            else:  
                print("Enter dice to keep, or (q)uit:")
            
            
            
                
            
            
            dice_input = input("> ")  
            if dice_input == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                return

            saved_dice = [int(x) for x in dice_input if x.isdigit()]
            valid = GameLogic.validate_keepers(tuple(user_roll), tuple(saved_dice))
            while not valid:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {roll_num} ***")
                print("Enter dice to keep, or (q)uit:")
                dice_input = input("> ")  
                saved_dice = [int(x) for x in dice_input if x.isdigit()]
                valid = GameLogic.validate_keepers(tuple(user_roll), tuple(saved_dice))
            if valid:       
                score = GameLogic.calculate_score(tuple(saved_dice))
                shelf = self.banker.shelved
                self.banker.shelf(shelf + score)
            
            self.dice_num -= len(saved_dice) 
            if dice_input:
                print(f"You have {self.banker.shelved} unbanked points and {self.dice_num} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                bank_input = input("> ")
                if bank_input == "b":
                    print(f"You banked {self.banker.shelved} points in round {self.round}")
                    self.banker.bank()
                    print(f"Total score is {self.banker.balance} points")
                    self.dice_num = 6
                    self.round += 1
                    
                elif bank_input == "r":
                    if self.dice_num == 0:
                        self.dice_num = 6
                    rolling()
                    
                elif bank_input == "q":
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                    
                    return
            
            self.status = True
        rolling()

    if __name__ == "__main__":
        
        
        def mock_roller(rolls):
            rolls = []
            return rolls.pop(0) 

        play(mock_roller)