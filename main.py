import random
import choice

def game():
    # This program also accepts the options in lower case
    
    options = ["R", "P", "S"]
    while True:
        user_choice = input("Pick an option: ")
        user_choice = user_choice.upper()
        if user_choice in options:
            break
        else:
            print("You have chosen an invalid option. Try again!")
            continue
    computer_choice = random.choice(options)
    print(f'Player {user_choice} : CPU {computer_choice}')
    
    if user_choice == computer_choice:
       game()
    if user_choice == "S" and computer_choice == "P":
        return print("Winner is Player!")
    elif user_choice == "P" and computer_choice == "S":
        return print("Winner is CPU!")
    elif user_choice == "P" and computer_choice == "R":
        return print("Winner is Player!")
    elif user_choice == "R" and computer_choice == "P":
        return print("Winner is CPU!")
    elif user_choice == "R" and computer_choice == "S":
        return print("Winner is Player!")
    elif user_choice == "S" and computer_choice == "R":
        return print("Winner is CPU!")
    
if __name__ == '__main__':
    game()
