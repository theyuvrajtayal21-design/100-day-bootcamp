import random
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
game = [rock, paper, scissors]
user_choice = int(input('input your choice: type 0 for rock, type 1 for paper, type 2 for scissors: '))
computer_choice = random.randint(0,2)
print(f"computer choice")
print(game[computer_choice])
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

if computer_choice == 2 and user_choice == 0:
    print("win")
elif user_choice >=3 or user_choice <0:
    print("invalid number")
elif computer_choice == 0 and user_choice == 2:
    print("win")
elif computer_choice > user_choice:
    print("lose")
elif computer_choice < user_choice:
    print("win")
elif computer_choice == user_choice:
    print("draw")