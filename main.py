############### Blackjack Project #####################
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from replit import clear
from art import logo
def deal_card():
  """Returns a random card"""
  return random.choice(cards)
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards_list):
  sum_of = sum(cards_list)
  if len(cards_list) == 2 and sum_of == 21:
    return 0
  elif sum_of > 21 and 11 in cards_list:
    cards_list.remove(11)
    cards_list.append(1)
    sum_of = sum(cards_list)
  return sum_of

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif user_score > computer_score:
    return "You win"
  elif computer_score > 21:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  should_play = True
      
  for num in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
      #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
      #and returns the score. 
      #Look up the sum() function to help you do this.
  while should_play:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
        
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if computer_score == 0 or  21 < user_score or user_score == 0:
      should_play = False
    else:
      draw = input("Do you wnat to draw another card? Type 'Yes' or 'No' ")
      if draw == "No":
        should_play = False
      else:
        user_cards.append(deal_card())
    
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final score : {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

