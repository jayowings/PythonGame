import random
a = 1
possible_choices = ['Rock','Paper','Scissors']

# loop through code until user wants to quit
while True:
    # User selection -- get info from user
    print('What is your selection? (Rock, Paper, Scissors):')
    player = input()
    #TODO Validate user selection
    print ('You chose', player)
    #-----------Cheat--------
    if player == 'Dragon':
        print ("AHHHH! A Dragon! Run for your life!")
        if a == a:
            if a < a:
                print (" ")
            else:
                print (" ")
        print(" ")
        print ("...")
        print ("I think you've won")
    else:
        # Computer selection -- find way for the computer to select the options
        computer_selection = random.choice(possible_choices)
        print ('Computer chose', str(computer_selection))
        # Evaluate the results --conditional statement
        if computer_selection == player:
            print ("It's a tie!")
            #----------------------Rock-------------------------
        elif player == 'Rock':
            #computer selects Paper
            if computer_selection == 'Paper':
                print ('You lose!')
                #computer selects Scissors
            else:
                print ("You win!")
    #------------------------Paper----------------------------
        elif player == 'Paper':
            #computer selects Rock
            if computer_selection == 'Rock':
                print ('You win!')
            #computer selects Scissors
            else:
                print ("You lose!")
    #-----------------------Scissors----------------------
        else:
        #computer selects Rock
            if computer_selection == 'Rock':
                print ('You lose!')
        #computer selects Paper
            else:
                print ("You win!")
    play_again = input("Do you want to play again (y/n): ")
    if play_again == 'n':
        break

print ('Thanks for playing')
