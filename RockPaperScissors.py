import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
weapons = ["rock", "paper", "scissors"]
print(f"You have chosen {weapons[choice]}. Prepare for battle!")
computer_choice = random.randint(0,2)
print(f"The computer has chosen {weapons[computer_choice]}. She is prepared for battle!")
if choice == computer_choice:
    print(f"You have both chosen {weapons[choice]}! This battle ends in a tie. Prepare to duel again!")
elif choice == 0 and computer_choice == 1:
    print(f"{weapons[computer_choice].title()} beats {weapons[choice].title()}. You have failed!")
elif choice == 0 and computer_choice == 2:
    print(f"{weapons[choice].title()} beats {weapons[computer_choice]}. You are victorious!")
elif choice == 1 and computer_choice == 2:
    print(f"{weapons[computer_choice].title()} beats {weapons[choice].title()}. You have failed!")
elif choice == 1 and computer_choice == 0:
    print(f"{weapons[choice].title()} beats {weapons[computer_choice]}. You are victorious!")
elif choice == 2 and computer_choice == 0:
    print(f"{weapons[computer_choice].title()} beats {weapons[choice].title()}. You have failed!")
elif choice == 2 and computer_choice == 1:
    print(f"{weapons[choice].title()} beats {weapons[computer_choice]}. You are victorious!")
