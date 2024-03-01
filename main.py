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

human_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
    ))

com_choice = random.randint(0, 2)

choice_list = [rock, paper, scissors]

if human_choice <= 2:
    print(choice_list[human_choice])
    print(f"Computer chose: \n {choice_list[com_choice]}")
    if com_choice == human_choice:
        print("Draw")
    elif com_choice == 0 and human_choice == 1:
        print("You win!")
    elif com_choice == 0 and human_choice == 2:
        print("You lose!")
    elif com_choice == 1 and human_choice == 0:
        print("You lose!")
    elif com_choice == 1 and human_choice == 2:
        print("You win!")
    elif com_choice == 2 and human_choice == 0:
        print("You win!")
    elif com_choice == 2 and human_choice == 1:
        print("You lose!")
    else:
        print("Try again!")
else:
    print("Invalid entry! Enter 0, 1, or 2")
