import time
import random

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game():
    print_slow("Welcome to the Text Adventure Game!")
    print_slow("You find yourself in a dark forest. You can go left, right, or forward.")

    while True:
        choice = input("Do you want to go left, right, or forward? ").strip().lower()

        if choice == "left":
            print_slow("You venture deeper into the forest.")
            left_path()
        elif choice == "right":
            print_slow("You head towards a clearing in the forest.")
            right_path()
        elif choice == "forward":
            print_slow("You follow a narrow path ahead.")
            forward_path()
        else:
            print_slow("Invalid choice. Please enter 'left', 'right', or 'forward'.")

def left_path():
    print_slow("You stumble upon a mysterious cave entrance.")
    print_slow("Do you want to enter the cave or go back to the forest?")
    
    while True:
        choice = input("Enter 'cave' or 'back': ").strip().lower()

        if choice == "cave":
            print_slow("You enter the cave...")
            cave_path()
        elif choice == "back":
            print_slow("You return to the forest.")
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'cave' or 'back'.")

def cave_path():
    print_slow("Inside the cave, you encounter a giant snake!")
    print_slow("Do you want to fight the snake or try to run away?")

    while True:
        choice = input("Enter 'fight' or 'run': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the giant snake in a battle...")
            if random.choice([True, False]):
                print_slow("You defeated the giant snake in a fierce battle!")
                print_slow("Congratulations! You've conquered the snake and continue exploring the cave.")
                cave_treasure()
            else:
                print_slow("The giant snake overpowers you and defeats you in combat.")
                print_slow("Game Over.")
                exit()
        elif choice == "run":
            print_slow("You attempt to flee from the giant snake but are caught and defeated.")
            print_slow("Game Over.")
            exit()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'run'.")

def cave_treasure():
    print_slow("After defeating the snake, you find a hidden chamber with a valuable treasure chest!")
    print_slow("Do you want to open the chest or leave it alone?")

    while True:
        choice = input("Enter 'open' or 'leave': ").strip().lower()

        if choice == "open":
            print_slow("You open the chest and find a fortune in gold and jewels!")
            print_slow("Congratulations! You've won the game.")
            exit()
        elif choice == "leave":
            print_slow("You decide to leave the chest and return to the forest.")
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'open' or 'leave'.")

def right_path():
    print_slow("You discover a river with a small boat.")
    print_slow("Do you want to take the boat downstream or upstream?")

    while True:
        choice = input("Enter 'downstream' or 'upstream': ").strip().lower()

        if choice == "downstream":
            print_slow("You paddle downstream...")
            shark_battle()
        elif choice == "upstream":
            print_slow("You paddle upstream but get caught in a strong current and drown.")
            print_slow("Game Over.")
            exit()
        else:
            print_slow("Invalid choice. Please enter 'downstream' or 'upstream'.")

def forward_path():
    print_slow("You come across a rickety bridge leading to a castle.")
    print_slow("Do you want to cross the bridge or go back to the forest?")

    while True:
        choice = input("Enter 'cross' or 'back': ").strip().lower()

        if choice == "cross":
            print_slow("You cross the bridge and enter the castle.")
            castle_path()
        elif choice == "back":
            print_slow("You decide to go back to the forest.")
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'cross' or 'back'.")

def castle_path():
    print_slow("Inside the castle, you encounter a dragon!")
    print_slow("Do you want to fight the dragon or try to sneak past it?")

    while True:
        choice = input("Enter 'fight' or 'sneak': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the dragon in a fierce battle...")
            print_slow("After a long and intense struggle, you manage to defeat the dragon!")
            print_slow("Congratulations! You've slain the dragon and won the game.")
            exit()
        elif choice == "sneak":
            print_slow("You attempt to sneak past the dragon but are caught and devoured.")
            print_slow("Game Over.")
            exit()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'sneak'.")

def shark_battle():
    print_slow("As you paddle downstream, you encounter a giant shark!")
    print_slow("Do you want to fight the shark or try to escape back to shore?")

    while True:
        choice = input("Enter 'fight' or 'escape': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the giant shark in a battle...")
            if random.choice([True, False]):
                print_slow("You defeated the giant shark in a fierce battle!")
                print_slow("Congratulations! You've conquered the shark and continue your journey.")
                start_game()
            else:
                print_slow("The giant shark overwhelms you and defeats you in combat.")
                print_slow("Game Over.")
                exit()
        elif choice == "escape":
            print_slow("You try to paddle back to shore but the giant shark catches up and attacks.")
            print_slow("Game Over.")
            exit()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'escape'.")

if __name__ == "__main__":
    start_game()
