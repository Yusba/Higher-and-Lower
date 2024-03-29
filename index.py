from art import logo,vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')

def format_account(account):
  """Take the account data and return the printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(guess,a_followers,b_followers):
  """Take the user guess and follow counts and return if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# display art
score = 0
print(logo)
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable
while game_should_continue:

  # generate a random account from the game_data
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A : {format_account(account_a)}.")
  print (vs)
  print(f"Against B : {format_account(account_b)}.")
  
  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # check if user is correct
  # get follower account for each account
  a_follower_count = account_a ["follower_count"]
  b_follower_count = account_b ["follower_count"]
  is_correct = check_answer(guess, a_follower_count,b_follower_count)

  # clear the screen between rounds
  clear()
  print(logo)
  # give user feedback on their guess
  # score keeping
  if is_correct:
    score+=1
    print(f"You are right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry,that's wrong. Final score: {score}.")
  




 
