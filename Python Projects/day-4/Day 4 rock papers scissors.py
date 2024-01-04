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

#Write your code below this line 👇
import random

options = [rock, paper, scissors]
game = input("Do you want to play a game? Type 0 Rock, 1 for Paper, 2 for Scissors?\n")
game = int(game)
computer_choice = random.randint(0,2)

if game >= 3 or game < 0:
  print("You failed to follow the rules. You lose.")

elif game == computer_choice:
  print(f"you chose {options[game]}")
  print(f"computer choice {options[computer_choice]}\nthis is a draw")
  
elif game == 0 and computer_choice == 2:
  print(f"you chose{options[game]}") 
  print(f"computer choice{options[computer_choice]}\nyou win")
  
elif computer_choice == 0 and game == 2:
  print(f"you chose{options[game]}") 
  print(f"computer choice{options[computer_choice]}\ncomputer win")
  
elif game > computer_choice:
  print(f"you chose{options[game]}") 
  print(f"computer choice{options[computer_choice]}\nyou win")
  
elif computer_choice > game:
  print(f"you chose{options[game]}")
  print(f"computer choice{options[computer_choice]}\ncomputer wins")