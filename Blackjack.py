logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True

game_start = input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no. ")

if game_start == 'n':
    should_continue == False

while should_continue:
    os.system('clear')
    print(logo)
    player_card = []
    computer_card = []
    player_card.append(random.choice(cards))
    player_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))

    print(f'Your cards:{player_card}, current score: {sum(player_card)}') 
    print(f"Computer's first card: {computer_card[0]}")
    if sum(player_card) == 21:
        print("Blackjack! You win.")
    elif sum(computer_card) == 21:
        print("Computer got Blackjack. You lose.")
    else:
        next_card = 'y'
        while next_card == 'y':
            next_card = input("Type 'y' to get another card, type 'n' to pass. ")
            if next_card == 'y':
                player_card.append(random.choice(cards))
                if sum(player_card) > 21:
                    if 11 in player_card:
                        player_card = [1 if card == 11 else card for card in player_card]
                    else:
                        next_card = 'n' 
                print(f"Your cards: {player_card}, current score: {sum(player_card)}")
                print(f"Computer's first card: {computer_card[0]}")

                    

        while sum(computer_card) < 17:
            computer_card.append(random.choice(cards))
            if sum(computer_card) > 21:
                if 11 in computer_card:
                    computer_card = [1 if card == 11 else card for card in computer_card]

        print(f"Your final hand: {player_card} Final score: {sum(player_card)}")
        print(f"Computer's final hand: {computer_card} Final score: {sum(computer_card)}")

        if sum(player_card) > 21:
            print("Busted. You lose.")
        elif sum(computer_card) > 21:
            print("Computer busted. You win!")
        elif sum(player_card) == sum(computer_card):
            print("Draw.")
        elif sum(player_card) > sum(computer_card):
            print("You win!")
        else:
            print("You lose.")

    new_game = input("Do you want to play a new Blackjack? Type 'y' or 'n'. ")
    if new_game == 'y':
        os.system('clear')
    else:    
        should_continue = False

print("Bye!")