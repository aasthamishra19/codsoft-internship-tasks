#rock,paper and scissors
import random

choice=[rock,paper,scissors]


def user1_choice():
  choice1 = input("Player_1 chooses (rock/paper/scissors): ").lower()
  if choice1 not in choices:
    print("Invalid move. Choose among rock/paper/scissors")
  return choice1

def user2_choice():
  choice2 = input("Player_2 chooses (rock/paper/scissors): ").lower()
  if (choice2 not in choices):
    print("Invalid move. Choose among rock/paper/scissors")
  return choice2

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def winner1(user1,computer):
  if user1 == computer:
      print("THIS IS A TIE")

  elif user1 == "rock":
      if computer == "paper":
        print("Paper beats rock. Computer wins")
      else:
        print("Rock beats scissor. User wins")

  elif user1 == "paper":
       if computer == "scissors":
         print("Scissors beats paper. Computer wins")
       else:
        print("Paper beats rock. User wins")

  elif user1 == "scissors":
       if computer == "rock":
        print("Rock beats scissors. Computer wins")
       else:
        print("Scissor beats Paper. User wins")



def winner(user1,user2):
  if user1 == user2:
      print("THIS IS A TIE")

  elif user1 == "rock":
      if user2 == "paper":
        print("Paper beats rock. Player2 wins")
      else:
        print("Rock beats scissor. Player1 wins")

  elif user1 == "paper":
       if user2 == "scissors":
         print("Scissors beats paper. Player2 wins")
       else:
        print("Paper beats rock. Player1 wins")

  elif user1 == "scissors":
       if user2 == "rock":
        print("Rock beats scissors. Player2 wins")
       else:
        print("Scissor beats paper. Player1 wins")

def main():
  print("WELCOME TO THE ROCK PAPER AND SCISSOR GAME ")
  choice = int(input("Enter 1 for SINGLE player,2 for MULTIPLAYER : "))
  if choice == 1:
    print("The game will be played between you and computer")

    user1 = user1_choice()
    computer = computer_choice()
    print(f"User chooses = {user1}")
    print(f"Computer chooses1 = {computer}")
    result = winner1(user1, computer)
    #print(result)
  else:
    print("The game will be played between you and your friend ")
    user1 = user1_choice()
    user2 = user2_choice()
    print(f"Player_1 chooses = {user1}")
    print(f"Player_2 chooses  = {user2}")
    result = winner(user1, user2)
    #print(result)


def another_round():
    ask_for_another_game = input("Do you want to play another round ? y for yes and n for no : ")
    if ask_for_another_game == "y":
      main()
    else:
      print("THANK YOU FOR PLAYING")


main()
#another_round()




