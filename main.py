#Declares cards that will be drawn from. Imports needed modules.
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Functions declared at the top that perform various functions. Doc strings have more information
def sum(deck):
    """Return the value of a list with numbers added together. Same as sum function."""
    total = 0
    for number in deck:
        total += number
    return total

def Draw(user_cards, cards):
    """Is a function that draws cards based on the inputs. It also checks
    if the user lost and if so, do they have a blackjack or an 11"""
    #First it draws a card
    user_cards.append(random.choice(cards))
    #If the total is over twenty one it checks if there is an eleven which can become
    #a 1.
    if sum(user_cards) >= 21:
        #Checks for 11 and replaces it with 1.
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
        if sum(user_cards) > 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
            else:
                #Since they didn't have an eleven, they lost.
                print("You lose because you got more than 21")
                print(f"Your cards were {user_cards}")
                #Declares that it should stop the game.
                lost_game = True
        if sum(user_cards) == 21 and len(user_cards) == 2:
            return 0
        return user_cards
    return user_cards
def check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum):
    """Called at the end of the game which checks who won the game. Requires inputs
    of the cards of the user, computer, and the sum of the user's cards and computers,
    cards."""
    #Checks if the user went over.
    if user_final_sum > 21:
        #Checks just like draw() function if there is an eleven to become a one.
        if 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            user_final_sum - 10
            #Recalls the function to restart and hopefully allow the user to win
            check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum)
        #There was not an 11 in the card deck. User lost
        print("You lost. Your guess was too high")
    #Checks the same thing for computer:
    elif computer_final_sum > 21:
        if 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_final_sum - 10
            check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum)
        print("You won! The computer busted")
    #Checks who got the higher amount and declares them winner.
    elif user_final_sum > computer_final_sum:
        print("You won! The computer guessed less than you")
    elif user_final_sum < computer_final_sum:
        print("You lost! Computer got higher guess")
    #Checks if it is a tie:
    elif user_final_sum == computer_final_sum:
        print("Draw!")
    #Prints the cards the computer and user had and the sums:
    print(f"Your cards were {user_cards} and the computers were {computer_cards}")
    print(f"Your sum was {user_final_sum} and computer's sum was {computer_final_sum}")
#The play_game function is the rest of the game.
# This allows the game to be rerun using the function
def play_game():
    """Starts the actual game and handles the calling of functions and gameplay."""
    #First three lines declare starting variables
    user_cards = []
    computer_cards = []
    lost_game = False
    #Draws the initial two cards for the user. Range does not include the last number.
    for time in range(1, 3):
        computer_cards.append(random.choice(cards))
    for time in range(1, 3):
        user_cards = Draw(user_cards, cards)
    More_Cards = True
    #Starts the loop to ask the user until they want to stop getting cards.
    while More_Cards is True and not lost_game:
        #Clears the screen on windows
        os.system('cls')
        #Prints out what is happening in the game. This is the first thing printed.
        print(f"Your cards are {user_cards}. Your score is {sum(user_cards)}. The computer's first card is {computer_cards[0]}")
        #Asks if they want another card. If so then it calls the draw function
        another_card = input("Would you like another card? Type 'y' for yes and 'n' for no: ").lower()
        if another_card == 'y':
            user_cards = Draw(user_cards, cards)
            #0 means they got blackjack so they instantly win
            if user_cards == 0:
                print(f"You won! Your cards were {user_cards}")
                lost_game = True
        #If they don't want any more cards then the while loop ends.
        elif another_card == "n":
            More_Cards = False
        #Checks if the user went over
        if sum(user_cards) > 21:
            #If they went over, this line skips the final part because they already
            #lost the game.
            lost_game = True
    #The computer/dealer draws until it is less than 17. Does not repeat this if
    #Computer recieved blackjack
    while sum(computer_cards) < 17 and sum(computer_cards) != 0:
        computer_cards.append(random.choice(cards))
    #The computer got blackjack so the user lost.
    if sum(computer_cards) == 0:
        print(f"You lost. Your cards were {user_cards} and computer's cards were '11', '10'")
    #If the user already lost, lost_game will be true which will prevent these other
    #functions from running.
    if lost_game == False:
        #Gets the sum of the cards
        user_final = sum(user_cards)
        computer_final = sum(computer_cards)
        #Clears screen and then passes arguements to the check_winner function like
        #decribed by the doc string.
        os.system('cls')
        check_winner(user_cards, computer_cards, user_final, computer_final)
Play_Again = True
#This allows the game to run.
while Play_Again:
    #Calls the actual game
    play_game()
    #Asks if the game should repeat. If yes then it loops back and clears screen
    #otherwise it will end the loop and say goodbye.
    Play = input("Would you like to play again? Type 'y' to continue or 'n' to stop:  ").lower()
    if Play == 'n':
        print("Okay goodbye")
        Play_Again = False
    else:
        os.system('cls')






