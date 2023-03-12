import random

# define the creature class
class Creature:
    def __init__(self, name):
        self.name = name.title()
        
        # Attributes to track playing the game
        hunger = 0
        boredom = 0
        tiredness = 0
        dirtiness = 0
        
        # track how much food in inventory
        food = 2
        
        is_sleeping = False
        is_alive = True
        
    def eat(self):
        if self.food > 0:
            food -= 1
            decrease = random.randint(1,4)
            hunger -= decrease
            print(f"{self.name} just ate a great meal!")
        else:
            print(f"{self.name} doesn't have any food available...")
            
        if self.hunger < 0:
            self.hunger == 0
            
     # generate random number and handle user guesses       
    def play(self):
        # Create a random number between 0 and 2:
        num = random.randint(0,2)
        print("The create wants to play a game....")
        print("It's thinking of a number that is either 0, 1, or 2")
        user_guess = int(input("Please enter your guess:  "))
        if user_guess ==  num:
            print("You guessed correctly!")
            self.boredom -= 3
        else:
            print("You guessed incorrectly...")
            self.boredom -= 1
            # boredom cant be less than 0
            if self.boredom < 0:
                self.boredom == 0
            
        
            