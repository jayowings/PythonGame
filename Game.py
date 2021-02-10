from datetime import datetime
import random

possible_choices = ['Rock','Paper','Scissors']

# User selection -- get info from user
print('What is your selection? (Rock, Paper, Scissors):')
player = input()
#TODO Validate user selection
print ('You chose', player)

# Computer selection -- find some way for the computer to select the options
now = datetime.now()
# Computer Selection
current_time = now.strftime("%S")
computer_selection = random.choices(possible_choices)
print ("Computer chose", str(computer_selection))



# Evaluate the results
# Declare a winner