
from game_of_greed.game_logic import GameLogic

class Game:
    def __init__(self, round = 1, dice_num = 6):
        self.round = round
        self.dice_num = dice_num
        self.status = True
        self.total_points = 0
        
    def play(self, roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        
        if user_input == "n":
            print("OK. Maybe another time")
            
        if user_input == "y":
            while self.status == True:
                self.round_start(roller)
            
            
                
    def round_start(self, roll):
        self.status = False
        print(f"Starting round {self.round}")
        user_roll = roll(6)
        
        roll_num = " ".join(str(i) for i in user_roll)
        print(f"Rolling {self.dice_num} dice...")
        print(f"*** {roll_num} ***")
        print("Enter dice to keep, or (q)uit:")
        
        
        dice_input = input("> ")        
        if dice_input == "q":
            print(f"Thanks for playing. You earned {self.total_points} points")
            return
        saved_dice = []
        for num in dice_input:
            saved_dice.append(int(num))
       
        score = GameLogic.calculate_score(tuple(saved_dice))
       
        self.dice_num -= len(saved_dice)
        if dice_input:
            print(f"You have {score} unbanked points and {self.dice_num} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            bank_input = input("> ")
            if bank_input == "b":
                self.total_points += score
                print(f"You banked {score} points in round {self.round}")
                print(f"Total score is {self.total_points} points")
                self.dice_num = 6
                
            elif bank_input == "r":
                pass
            elif bank_input == "q":
                print(f"Thanks for playing. You earned {self.total_points} points")
                
                return
        self.round += 1
        self.status = True

    if __name__ == "__main__":
        
        
        def mock_roller(rolls):
            rolls = []
            return rolls.pop(0) 

        play(mock_roller)