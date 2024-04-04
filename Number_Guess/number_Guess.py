
Game_over = False
import random
from art import logo

answer = random.randint(1,100)
attempts = 0
guess = 0


def game_start():
  global attempts
  """This starts the game and sets the difficulty, allotting the player 10 or 5 attempts"""
  print(logo)
  print("Welcome to the Number Guessing Game!\n")
  print("I'm thinking of a number between 1 and 100.\n")
 
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5
  else:
    print("Invalid input")
    game_start()
    

  

def check_guess(guess, answer):
  """Checks guess against answer. Returns the number of turns remaining."""
  guess = int(input("Guess a number between 1 and 100: "))
  global Game_over
  global attempts 
  if guess == answer:
    print(f"You got it! The answer was {answer}\n\n")
    Game_over = True
  else:
    if guess > answer:
      print("Too high")
      attempts -= 1
      return attempts
      return guess
      return answer
    elif guess < answer:
      print("Too low")
      attempts -= 1
      return attempts
      return guess
      return answer
  




game_start()
check_guess(guess, answer)

if Game_over == True:
  play_again = input("Would you like to play again?\n Type 'y' for yes or 'n' for no\n")
  if play_again == "y":
    game_start()
  else:
    print("Thanks for Playing! Goodbye")
elif Game_over == False:    
  while not Game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    check_guess(guess, answer)
    if attempts == 0:
      print("You've run out of guesses, you lose.\n")
      play_again = input("Would you like to play again?\n Type 'y' for yes or 'n' for no\n")
      if play_again == "y":
        game_start()
      else:
        Game_over = True