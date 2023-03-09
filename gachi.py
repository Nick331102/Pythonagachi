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
            
        
        