import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game():
    print_slow("Welcome to the Text Adventure Game!")
    print_slow("You find yourself in a dark forest. You can go left or right.")

    while True:
        choice = input("Do you want to go left or right? ").strip().lower()

        if choice == "left":
            print_slow("You venture deeper into the forest.")
            left_path()
        elif choice == "right":
            print_slow("You head towards a clearing in the forest.")
            right_path()
        else:
            print_slow("Invalid choice. Please enter 'left' or 'right'.")

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
    print_slow("Inside the cave, you find a treasure chest!")
    print_slow("Do you want to open the chest or leave it alone?")

    while True:
        choice = input("Enter 'open' or 'leave': ").strip().lower()

        if choice == "open":
            print_slow("You open the chest and find a pile of gold!")
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
            print_slow("You paddle downstream and reach a peaceful village.")
            print_slow("Congratulations! You've found safety.")
            exit()
        elif choice == "upstream":
            print_slow("You paddle upstream but get caught in a strong current and drown.")
            print_slow("Game Over.")
            exit()
        else:
            print_slow("Invalid choice. Please enter 'downstream' or 'upstream'.")

if __name__ == "__main__":
    start_game()
