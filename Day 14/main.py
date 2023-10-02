# from art import *
# from game_data import *
# import random

# print(logo)




# def game():
#     score=0

#     account_a= random.choice(data)
#     account_b= random.choice(data)
#     if account_a==account_b:
#         account_b= random.choice(data)

#     account_name_a=account_a['name']
#     account_follower_count_a=account_a['follower_count']
#     account_description_a=account_a['description']
#     account_country_a=account_a['country']


#     account_name_b=account_b['name']
#     account_follower_count_b=account_b['follower_count']
#     account_description_b=account_b['description']
#     account_country_b=account_b['country']

#     print(f"Compare A: {account_name_a}, a {account_description_a}, from {account_country_a}")

#     print(vs)

#     print(f"Against B: {account_name_b}, a {account_description_b}, from {account_country_b}")

#     x=input(f"Who has more followers? Type 'A' or 'B' : ")



#     if (x=='A' and account_follower_count_a>account_follower_count_b):
#         score+=1
#         print(f"You're right! Current score: {score}")
#         game()
#     elif(x=='B' and account_follower_count_b>account_follower_count_a):
#         score+=1
#         print(f"You're right! Current score: {score}")
#         game()
#     else:
#         print(f"Sorry that was wrong. Your final score is {score}")

# game()


from game_data import data
import random
from art import logo, vs

def get_random_account():
  
  return random.choice(data)

def format_data(account):

  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()