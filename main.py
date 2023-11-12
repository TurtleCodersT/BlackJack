import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def sum(deck):
    total = 0
    for number in deck:
        total += number
    return total

def Draw(user_cards, cards):
    user_cards.append(random.choice(cards))
    if sum(user_cards) >= 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
        if sum(user_cards) > 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
            else:
                print("You lose because you got more than 21")
                print(f"Your cards were {user_cards}")
                lost_game = True
        if sum(user_cards) == 21 and len(user_cards) == 2:
            return 0
        return user_cards
    return user_cards
def check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum):
    if user_final_sum > 21:
        if 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            user_final_sum - 10
            check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum)
        print("You lost. Your guess was too high")
    elif computer_final_sum > 21:
        if 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_final_sum - 10
            check_winner(user_cards, computer_cards, user_final_sum, computer_final_sum)
        print("You won! The computer busted")
    elif user_final_sum > computer_final_sum:
        print("You won! The computer guessed less than you")
    elif user_final_sum < computer_final_sum:
        print("You lost! Computer got higher guess")
    elif user_final_sum == computer_final_sum:
        print("Draw!")
    print(f"Your cards were {user_cards} and the computers were {computer_cards}")
    print(f"Your sum was {user_final_sum} and computer's sum was {computer_final_sum}")
def play_game():
    user_cards = []
    computer_cards = []
    lost_game = False
    for time in range(1, 3):
        computer_cards.append(random.choice(cards))
    for time in range(1, 3):
        user_cards = Draw(user_cards, cards)
    More_Cards = True
    while More_Cards is True and not lost_game:
        os.system('cls')
        print(f"Your cards are {user_cards}. Your score is {sum(user_cards)}. The computer's first card is {computer_cards[0]}")
        another_card = input("Would you like another card? Type 'y' for yes and 'n' for no: ").lower()
        if another_card == 'y':
            user_cards = Draw(user_cards, cards)
            if user_cards == 0:
                print(f"You won! Your cards were {user_cards}")
                lost_game = True
        elif another_card == "n":
            More_Cards = False
        if sum(user_cards) > 21:
            lost_game = True
    while sum(computer_cards) < 17 and sum(computer_cards) != 0:
        computer_cards.append(random.choice(cards))
    if sum(computer_cards) == 0:
        print(f"You lost. Your cards were {user_cards} and computer's cards were '11', '10'")
    if lost_game == False:
        user_final = sum(user_cards)
        computer_final = sum(computer_cards)
        os.system('cls')
        check_winner(user_cards, computer_cards, user_final, computer_final)
Play_Again = True
while Play_Again:
    play_game()
    Play = input("Would you like to play again? Type 'y' to continue or 'n' to stop:  ").lower()
    if Play == 'n':
        print("Okay goodbye")
        Play_Again = False
    else:
        os.system('cls')



