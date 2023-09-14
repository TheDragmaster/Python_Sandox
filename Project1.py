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
    print_slow("Inside the cave, you encounter a giant snake blocking your path!")
    print_slow("The snake appears to be guarding something.")
    print_slow("Do you want to fight the snake or try to sneak past it?")

    while True:
        choice = input("Enter 'fight' or 'sneak': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the giant snake in a battle...")
            if random.choice([True, False]):
                print_slow("You defeated the giant snake in a fierce battle!")
                print_slow("The snake's lair holds a valuable treasure chest!")
                print_slow("Congratulations! You've conquered the snake and found treasure.")
                cave_treasure()
            else:
                print_slow("The giant snake overpowers you and defeats you in combat.")
                print_slow("Game Over.")
                exit()
        elif choice == "sneak":
            print_slow("You attempt to sneak past the giant snake...")
            if random.choice([True, False]):
                print_slow("You successfully sneak past the snake and discover a treasure chest!")
                print_slow("Congratulations! You've found treasure without a fight.")
                cave_treasure()
            else:
                print_slow("The snake notices your attempt to sneak and attacks you.")
                print_slow("Game Over.")
                exit()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'sneak'.")

def cave_treasure():
    print_slow("You open the treasure chest and find a fortune in gold and jewels!")
    print_slow("Congratulations! You've won the game.")
    exit()

def right_path():
    print_slow("You discover a river with a small boat.")
    print_slow("Do you want to take the boat downstream or upstream?")

    while True:
        choice = input("Enter 'downstream' or 'upstream': ").strip().lower()

        if choice == "downstream":
            print_slow("You paddle downstream and reach a calm riverbank.")
            riverbank_challenge()
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
    print_slow("The dragon guards a treasure chest in the corner of the room.")
    print_slow("Do you want to fight the dragon or try to negotiate for the treasure?")

    while True:
        choice = input("Enter 'fight' or 'negotiate': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the dragon in a fierce battle...")
            if random.choice([True, False]):
                print_slow("After a long and intense struggle, you manage to defeat the dragon!")
                print_slow("Congratulations! You've slain the dragon and found treasure.")
                castle_treasure()
            else:
                print_slow("The dragon's might proves too much, and it defeats you.")
                print_slow("Game Over.")
                exit()
        elif choice == "negotiate":
            print_slow("You attempt to negotiate with the dragon...")
            if random.choice([True, False]):
                print

if __name__ == "__main__":
    start_game()
