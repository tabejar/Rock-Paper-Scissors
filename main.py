import random 
from choices import result, retry

player = input("rock, paper, or scissors: ").lower()
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
result(player, computer)
play_again = input("Wanna play again? (yes/no)").lower()
retry(play_again)
while play_again == "yes":
  player = input("rock, paper, or scissors: ").lower()
  choices = ["rock","paper","scissors"]
  computer = random.choice(choices)
  result(player,computer)
  play_again = input("Wanna play again? (yes/no)").lower()
  retry(play_again)