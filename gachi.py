import random

# define the creature class
class Creature:
    def __init__(self, name):
        self.name = name.title()
        
        # Attributes to track playing the game
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        
        # track how much food in inventory
        self.food = 2
        
        self.is_sleeping = False
        self.is_alive = True
        
    def eat(self):
        if self.food > 0:
            self.food -= 1
            decrease = random.randint(1,4)
            self.hunger -= decrease
            print(f"{self.name} just ate a great meal!")
        else:
            print(f"{self.name} doesn't have any food available...")
            
        if self.hunger < 0:
            self.hunger = 0
            
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
                self.boredom = 0
    
    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print("Your creature is cureently sleeping.  zzzzzz")
        
        # tiredness cant be less than 0
        if self.tiredness < 0:
            self.tiresness = 0
             # boredom cant be less than 0
        if self.boredom < 0:
            self.boredom = 0
            
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
        
        if self.is_sleeping == False:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)
        
        self.dirtiness += random.randint(0, difficulty)
    
    # conditions that affect the state of the creature
    def kill(self):
        if self.hunger >= 10:
            self.is_alive = False
        elif self.dirtiness >= 10:
            print("Your creature has suffered a fatal infection and has died.")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print("Your creature is bored and will soon be asleep")
            self.is_sleeping == True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print("Your creature is sleepy and will soon be asleep")
            self.is_sleeping = True


def show_menu(creature):
    if creature.is_sleeping:
        choice = int(input("Creature is sleeping. Press 6 to wake up."))
        choice = 6
    else:
        print("Enter 1 to eat.")
        print("Enter 2 to play.")
        choice = int(input("Enter your choice: "))
    
    if choice == 1:
        creature.eat()
    elif choice == 2:
        creature.play()
    elif choice == 6:
        creature.awake()
    else:
        print("Invalid choice!")
 
        
def call_action(creature, choice):
    if choice == 1:
        creature.eat()
    elif choice == 2:
        creature.play()
    elif choice == 3:
        creature.sleep()
    elif choice == 4:
        creature.clean()
    elif choice == 5:
        creature.forage()
    elif choice == 6:
        creature.awake
    else:
        print("You entered an invalid choice...")
        
# Main code
print("Welcome to Pythonagachi 2023")

# active variable
running = True
while running:
    player_name = input("Enter the name of your creature:  ")
    player = Creature(player_name) # creature object created
    
    rounds = 1

     # input to select the difficulty level
    difficulty = int(input("Please enter a difficulty level between 1 and 5:  "))
    if difficulty > 5:
        difficulty = 5
    elif difficulty < 1:
        difficulty = 1
        
    while player.is_alive:
        print(f"\n Round: {rounds} ")
        player.show_values()
        show_menu(player)
        call_action(player)
    
        # show current round    
        print(f"The current round is: {rounds}")
    
        player.show_values()
    
        print("Press enter to continue")
    
        player.increment_values()
        player.kill()
        rounds += 1
        
        if not player.is_alive:
            print(f'Your creature has died!  it survived {rounds} rounds.')
            play_again = input("Would you like to play again?").lower()
            if play_again == "n":
                running = False
            elif play_again == "y":
                break
            else:
                print("Invalid inout, Game over.")
                running = False
        
print("Thank you for playing Pythonagachi 2023!")
                 
            

            

    
    
    
    
        

    
    
    
    
    
    
    
    
    

 

    
        


        
        
        
        
            
            
        
        
        
        
        
            
        
            
        
            
        
        
        
            
        
            