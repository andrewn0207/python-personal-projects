import random
def play_game():
        print ("Welcome to Python Rock Paper & Scissors")

    #List of choices
        choices = ['rock', 'paper', 'scissors']

    # player score
        user_score = 0
        computer_score = 0
    # main game function
        while user_score < 3 and computer_score < 3:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            computer_choices = random.choice(choices).lower()
            print("Computer chose", computer_choices)
            if user_choice not in choices:
                print("Invalid choice, try again")
                continue
            if user_choice == computer_choices:
                print("Tie!!")
            elif    (user_choice == 'rock' and computer_choices == 'scissors') or \
                    (user_choice == 'paper' and computer_choices == 'rock') or \
                    (user_choice == 'scissors' and computer_choices == 'paper'):
                print("You win!! + 1")
                user_score +=1 
            else:
                print("Computer won!! + 1")  
                computer_score +=1   
        #End of the game       
        print("You scored", user_score, "while the computer scored", computer_score)
        if user_score > computer_score:
            print("You won the game")
        else:
            print("The computer won the game!")
# Start new
while True:
    play_game()  # Run the game
    user_choice = input("Do you want to play again? (y/n): ").lower()
    if user_choice != 'y': 
            print("Thanks for playing!")
            break
    else:
        continue


