import random
from typing import List

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images: List[str] = [rock, paper, scissors]


def get_user_choice() -> int:
  try:
    choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    if choice not in [0, 1, 2]:
      raise ValueError("Choice must be 0, 1, or 2.")
    return choice
  except ValueError as e:
    print(f"Invalid input: {e}")
    return -1


def get_computer_choice() -> int:
  return random.randint(0, 2)


def display_choices(user_choice: int, computer_choice: int):
  print(f"You chose:\n{game_images[user_choice]}")
  print(f"Computer chose:\n{game_images[computer_choice]}")


def determine_winner(user_choice: int, computer_choice: int) -> str:
  if user_choice == computer_choice:
    return "It's a draw!"
  elif (user_choice == 0 and computer_choice == 2) or \
       (user_choice == 1 and computer_choice == 0) or \
       (user_choice == 2 and computer_choice == 1):
    return "You win!"
  else:
    return "You lose!"


def play_game():
  user_choice = get_user_choice()
  if user_choice == -1:
    return
  computer_choice = get_computer_choice()
  display_choices(user_choice, computer_choice)
  result = determine_winner(user_choice, computer_choice)
  print(result)


if __name__ == "__main__":
  play_game()
