def result(player, computer):
  #prints player's and computer's choice and the result
  print("Computer: ", computer)
  print("Player: ", player)
  if player == computer:
    print("DRAW :0")
  elif player == "rock":
    if computer == "paper":
      print("I win :)")
    if computer == "scissors":
      print("I lose :(")
    if computer == player:
      print("DRAW :0")
  elif player == "paper":
    if computer == "rock":
      print("I lose :(")
    if computer == player:
      print("DRAW :0")
    if computer == "scissors":
      print("I win :)")
  elif player == "scissors":
    if computer == "rock":
      print("I win :)")
    if computer == player:
      print("DRAW :0")
    if computer == "paper":
      print("I lose :(")
  else: 
    #allows the player to replay the game
    print("HEY!!! STOP THAT!!! STOP BEING SILLY!!!!!!!! THAT IS NOT HOW ITS SUPPOSED TO GO!!")
def retry(play_again):
  if play_again == "yes":
    print("Alright then, come at me. Goofy.")
  else:
    print("Alright then. Don't come back")
    exit()
  
  