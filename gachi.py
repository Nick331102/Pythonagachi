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
    
    def sleep(self):
        self.is_sleeping == True
        self.tiredness -= 3
        self.boredom -= 2
        print("Your creature is cureently sleeping.  zzzzzz")
        
        # tiredness cant be less than 0
        if self.tiredness < 0:
            self.tiresness == 0
             # boredom cant be less than 0
        if self.boredom < 0:
            self.boredom == 0
            
    def awake(self):
        num = random.randint(0,2)
        if num == 0:
            print("Your creature is just waking up.  Give it a second.")
            self.is_sleeping == False
            self.boredom == 0
        else:
            print("Your creature wont wake up...")
            self.sleep()
            
    def clean(self):
        self.dirtiness == 0
        print("Your creature just took a nice bath!")
        
    def forage(self):
        food_found = random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        print(f"Your creature just found {food_found} morsels of food.")
    
    # display the current state of the creature   
    def show_values(self):
        print("Name:", self.name)
        print("Hunger:", self.hunger)
        print("Boredom:", self.boredom)
        print("Tiredness:", self.tiredness)
        print("Dirtiness:", self.dirtiness)
        print("Food Inventory:", self.food)
        print("Sleeping Status:", self.is_sleeping)
        
    def increment_values(self, difficulty):
        self.hunger += random.randint(0, difficulty)
        
        
        
        
        
            
        
            
        
            
        
        
        
            
        
            