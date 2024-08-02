
import random
from art import logo

def new_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def cards_tally(player_cards):
  if 11 in player_cards and sum(player_cards) > 21:
    player_cards.remove(11)
    player_cards.append(1)
  return sum(player_cards)

def compare(user, computer):
  print(f"Your fianl hand: {user_cards}, final score: {user_total} ")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
  if user > computer and user <= 21:
    print("You win!")
  elif user <= 21 and computer > 21:
    print("Opponent went over, you win!")
  elif computer > user and computer <= 21:
    print("You lose!")
  elif user_total > 21:
    print("You went over, You lose!")
  elif computer == user:
    print("Draw!")

user_cards = []
user_cards.append(new_card())
user_cards.append(new_card())
user_total = cards_tally(user_cards)

computer_cards = []
computer_total = 0
while computer_total <17:
  computer_cards.append(new_card())
  computer_total = cards_tally(computer_cards)

print(logo)
print(f"Your cards: {user_cards}, current score: {user_total} ")
print(f"Computer's first card: {computer_cards[0]}")

game = True
while game:
  more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
  if more_cards == "y":
    card = new_card()
    user_cards.append(card)
    user_total += card
    print(f"Your cards: {user_cards}, final score: {user_total} ")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_total > 21:
      game = False
  else:
    game = False
  if user_total > 21:
    compare(user=user_total, computer=computer_total)
if more_cards == "n":
  compare(user=user_total, computer=computer_total)







