import art
import game_data
import random
import os

# function that picks random celebrity
def pick_celeb():
  return random.choice(game_data.data)

# function that print formatted version
def format_data(celeb):
  return f"{celeb['name']}, a {celeb['description']}, from {celeb['country']}"

# start of game
def higher_lower_game():
  score = 0
  should_continue = True
  compare_a = pick_celeb()
  while should_continue:
    print(art.logo)
    if score != 0:
      print(f"You're right! Current score: {score}")
    
    print(f"Compare A: {format_data(compare_a)}")
    compare_b = pick_celeb()
    while compare_b == compare_a:
      compare_b = pick_celeb()
    print(art.vs)
    print(f"Compare B: {format_data(compare_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare_a['follower_count'] > compare_b['follower_count']:
      winner = compare_a
    else:
      winner = compare_b
  
    # check if the user guessed it right
    if guess == 'a' and winner == compare_a:
      score += 1
      compare_a = compare_b
      os.system('clear')
    elif guess == 'b' and winner == compare_b:
      score += 1
      compare_a = compare_b
      os.system('clear')
    else:
      os.system('clear')
      print(art.logo)
      print(f"Sorry, that was wrong. Your final score: {score}")
      should_continue = False

  
higher_lower_game()