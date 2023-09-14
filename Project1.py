import time
import random

# ANSI escape codes for text formatting
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

def print_slow(text, color=None, bold=False, underline=False):
    formatted_text = text
    if color:
        formatted_text = f"{color}{formatted_text}{RESET}"
    if bold:
        formatted_text = f"{BOLD}{formatted_text}{RESET}"
    if underline:
        formatted_text = f"{UNDERLINE}{formatted_text}{RESET}"

    for char in formatted_text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game(location="the Dark Forest"):
    print_slow(f"Welcome to {location}!", YELLOW)
    print_slow("The air is thick with anticipation as you ponder your next move.", YELLOW)
    print_slow("You can go left, right, or forward.", YELLOW)

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
            print_slow("Invalid choice. Please enter 'left', 'right', or 'forward'.", RED)

def left_path():
    print_slow("You stumble upon a mysterious cave entrance.")
    print_slow("The cave entrance beckons, and you feel a sense of foreboding.")
    print_slow("Do you want to enter the cave or go back to the forest?")
    
    while True:
        choice = input("Enter 'cave' or 'back': ").strip().lower()

        if choice == "cave":
            print_slow("You enter the cave...", YELLOW)
            cave_path()
        elif choice == "back":
            print_slow("You decide to return to the forest.")
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'cave' or 'back'.", RED)

def cave_path():
    print_slow("Inside the cave, you encounter a giant snake blocking your path!")
    print_slow("The snake's scales glisten in the dim light, and its eyes fixate on you.")
    print_slow("You engage the giant snake in a fierce battle...", YELLOW)

    while True:
        print_slow("You have three choices:", YELLOW)
        print_slow("1. Fight the giant snake.")
        print_slow("2. Try to calm the giant snake.")
        print_slow("3. Attempt to sneak past the giant snake.")

        choice = input("Enter '1', '2', or '3': ").strip()

        if choice == "1":
            print_slow("You confront the giant snake in a thrilling battle...", YELLOW)
            if random.choice([True, False]):
                print_slow("With precise timing and strategy, you defeat the giant snake!", GREEN)
                print_slow("The snake's lair holds a valuable treasure chest!", GREEN)
                print_slow("Congratulations! You've conquered the snake and found treasure.")
                choose_space_or_steampunk()
            else:
                print_slow("The giant snake overpowers you and defeats you in combat.")
                death_adventure()
        elif choice == "2":
            print_slow("You attempt to calm the giant snake...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your soothing words and gestures calm the giant snake.", GREEN)
                print_slow("The snake peacefully slithers away, allowing you to continue your journey.", GREEN)
                choose_space_or_steampunk()
            else:
                print_slow("The giant snake remains hostile and attacks you.")
                death_adventure()
        elif choice == "3":
            print_slow("You cautiously attempt to sneak past the giant snake...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your stealthy movements allow you to evade the giant snake.", GREEN)
                print_slow("You find yourself back in the Dark Forest.", GREEN)
                choose_space_or_steampunk()
            else:
                print_slow("The giant snake's keen senses detect your presence, and it confronts you.")
                death_adventure()
        else:
            print_slow("Invalid choice. Please enter '1', '2', or '3'.", RED)

def right_path():
    print_slow("You discover a river with a small boat.")
    print_slow("The river flows with a serene elegance, but there's an air of uncertainty.")
    print_slow("Do you want to take the boat downstream or upstream?")
    
    while True:
        choice = input("Enter 'downstream' or 'upstream': ").strip().lower()

        if choice == "downstream":
            print_slow("You paddle downstream along the tranquil river...")
            riverbank_challenge()
        elif choice == "upstream":
            print_slow("You paddle upstream but get caught in a strong current and drown.")
            death_adventure()
        else:
            print_slow("Invalid choice. Please enter 'downstream' or 'upstream'.", RED)

def riverbank_challenge():
    print_slow("As you drift downstream, you encounter a massive water serpent!")
    print_slow("The water serpent rises from the depths, its enormous coils glistening with water droplets.")
    print_slow("Do you want to fight the water serpent, attempt to evade it, or try to negotiate?")
    
    while True:
        choice = input("Enter 'fight', 'evade', or 'negotiate': ").strip().lower()

        if choice == "fight":
            print_slow("You pilot your boat into an epic battle with the water serpent...", YELLOW)
            if random.choice([True, False]):
                print_slow("With heroic effort and strategy, you defeat the water serpent!", GREEN)
                print_slow("The river is now safe to navigate, and you continue downstream.", GREEN)
                choose_space_or_steampunk()
            else:
                print_slow("The water serpent capsizes your boat, and you struggle in the water.")
                death_adventure()
        elif choice == "evade":
            print_slow("You skillfully maneuver your boat to evade the water serpent.", YELLOW)
            if random.choice([True, False]):
                print_slow("Your quick reflexes allow you to escape the water serpent's pursuit.", GREEN)
                print_slow("You find yourself downstream, safe from danger.", GREEN)
                choose_space_or_steampunk()
            else:
                print_slow("The water serpent's relentless pursuit catches up to you.")
                death_adventure()
        elif choice == "negotiate":
            print_slow("You attempt to negotiate with the water serpent...", YELLOW)
            if random.choice([True, False]):
                print_slow("The water serpent agrees to let you pass peacefully.", GREEN)
                print_slow("You continue downstream, unharmed by the encounter.", GREEN)
                choose_space_or_steampunk()
            else:
                print_slow("The water serpent rejects your offer and attacks your boat.")
                death_adventure()
        else:
            print_slow("Invalid choice. Please enter 'fight', 'evade', or 'negotiate'.", RED)

def forward_path():
    print_slow("You follow the narrow path, and it leads you deeper into the forest.")
    print_slow("Suddenly, you come across a massive dragon blocking your way!")
    print_slow("The dragon's scales shimmer with an otherworldly luster, and its fiery gaze locks onto you.")
    print_slow("Do you want to fight the dragon, negotiate with it, or attempt to sneak past it?")
    
    while True:
        choice = input("Enter 'fight', 'negotiate', or 'sneak': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the dragon in a fierce battle...", YELLOW)
            if random.choice([True, False]):
                print_slow("After a heroic battle, you manage to defeat the dragon!", GREEN)
                print_slow("The dragon's treasure is now yours.", YELLOW)
                print_slow("Congratulations! You've slain the dragon and acquired the treasure.")
                choose_space_or_steampunk()
            else:
                print_slow("The dragon's power is too great, and it overcomes you in battle.")
                death_adventure()
        elif choice == "negotiate":
            print_slow("You attempt to negotiate with the dragon...", YELLOW)
            if random.choice([True, False]):
                print_slow("The dragon is impressed by your courage and wisdom.", GREEN)
                print_slow("It agrees to share the treasure with you.", YELLOW)
                print_slow("Congratulations! You've acquired the treasure without a fight.")
                choose_space_or_steampunk()
            else:
                print_slow("The dragon rejects your offer and attacks you.")
                death_adventure()
        elif choice == "sneak":
            print_slow("You cautiously attempt to sneak past the dragon...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your stealthy movements allow you to evade the dragon.", GREEN)
                print_slow("You find yourself back in the Dark Forest.", YELLOW)
                choose_space_or_steampunk()
            else:
                print_slow("The dragon's keen senses detect your presence, and it confronts you.")
                death_adventure()
        else:
            print_slow("Invalid choice. Please enter 'fight', 'negotiate', or 'sneak'.", RED)

def death_adventure():
    print_slow("Unfortunately, you have met an untimely end.", YELLOW)
    print_slow("In this moment, you are faced with a choice.", YELLOW)
    print_slow("You can either choose to walk into the light or embrace the abyss.", YELLOW)
    print_slow("Each path leads to a different adventure, and there is no turning back.", YELLOW)
    
    while True:
        choice = input("Enter 'light' to walk into the light, 'abyss' to embrace the abyss, or 'retry' to try again: ").strip().lower()

        if choice == "light":
            light_adventure()
        elif choice == "abyss":
            abyss_adventure()
        elif choice == "retry":
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'light', 'abyss', or 'retry'.", RED)

def light_adventure():
    print_slow("You walk into the blinding light and find yourself in a serene paradise.", YELLOW)
    print_slow("This heavenly realm is filled with beauty and tranquility.", YELLOW)
    
    while True:
        print_slow("You encounter a guardian of the light, a radiant being of great power.", YELLOW)
        print_slow("You have three choices:", YELLOW)
        print_slow("1. Engage in a battle with the guardian.")
        print_slow("2. Attempt to persuade the guardian.")
        print_slow("3. Seek guidance from the guardian.")
        
        choice = input("Enter '1', '2', or '3': ").strip()
        
        if choice == "1":
            print_slow("Prepare for an epic battle against the guardian...", YELLOW)
            if random.choice([True, False]):
                print_slow("With unwavering determination, you defeat the guardian of the light!", GREEN)
                print_slow("The paradise radiates with even more brilliance.", GREEN)
                game_win_screen()
            else:
                print_slow("The guardian's light overwhelms you, and you are consumed by its power.")
                game_over()
        elif choice == "2":
            print_slow("You attempt to persuade the guardian of the light...", YELLOW)
            if random.choice([True, False]):
                print_slow("The guardian is moved by your sincerity and agrees to aid you.", GREEN)
                game_win_screen()
            else:
                print_slow("The guardian remains resolute and challenges you to a test of your resolve.")
                game_over()
        elif choice == "3":
            print_slow("You seek guidance from the guardian of the light...", YELLOW)
            if random.choice([True, False]):
                print_slow("The guardian imparts wisdom that illuminates your path.", GREEN)
                game_win_screen()
            else:
                print_slow("The guardian's guidance leads you to a dead end, and you're lost in the paradise.")
                game_over()
        else:
            print_slow("Invalid choice. Please enter '1', '2', or '3'.", RED)

def abyss_adventure():
    print_slow("You embrace the abyss and find yourself in a dark and eerie realm.", YELLOW)
    print_slow("This abyssal realm is filled with shadows and uncertainty.", YELLOW)
    
    while True:
        print_slow("You encounter a formidable dark entity, the Shadow Lord.", YELLOW)
        print_slow("You have three choices:", YELLOW)
        print_slow("1. Fight the Shadow Lord.")
        print_slow("2. Try to persuade the Shadow Lord.")
        print_slow("3. Attempt to sneak past the Shadow Lord.")
        
        choice = input("Enter '1', '2', or '3': ").strip()
        
        if choice == "1":
            print_slow("Prepare for an epic battle against the Shadow Lord...", YELLOW)
            if random.choice([True, False]):
                print_slow("With unwavering determination, you defeat the Shadow Lord!", GREEN)
                game_win_screen()
            else:
                print_slow("The Shadow Lord's dark powers overwhelm you, and you are consumed by darkness.")
                game_over()
        elif choice == "2":
            print_slow("You attempt to persuade the Shadow Lord...", YELLOW)
            if random.choice([True, False]):
                print_slow("The Shadow Lord is moved by your words and dissipates into the darkness.", GREEN)
                game_win_screen()
            else:
                print_slow("The Shadow Lord remains resolute and attacks you.")
                game_over()
        elif choice == "3":
            print_slow("You cautiously attempt to sneak past the Shadow Lord...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your stealthy movements allow you to evade the Shadow Lord.", GREEN)
                game_win_screen()
            else:
                print_slow("The Shadow Lord's keen senses detect your presence, and it confronts you.")
                game_over()
        else:
            print_slow("Invalid choice. Please enter '1', '2', or '3'.", RED)

# ... (previous code)

def choose_space_or_steampunk():
    print_slow("You've emerged victorious and stand at a crossroads.", YELLOW)
    print_slow("Two mysterious portals appear before you, each leading to a different adventure.", YELLOW)
    print_slow("One portal has a futuristic energy, while the other exudes a steampunk vibe.")
    print_slow("The choice is yours: will you enter the 'steampunk' portal or the 'space' portal?")

    while True:
        choice = input("Enter 'steampunk' or 'space': ").strip().lower()

        if choice == "steampunk":
            print_slow("You step into the 'steampunk' portal and find yourself in a city of marvels...", YELLOW)
            steampunk_adventure()
        elif choice == "space":
            print_slow("You enter the 'space' portal and embark on an interstellar journey...", YELLOW)
            space_adventure()
        else:
            print_slow("Invalid choice. Please enter 'steampunk' or 'space'.", RED)

def steampunk_adventure():
    print_slow("You find yourself in a sprawling steampunk city, filled with gears and gadgets.", YELLOW)
    print_slow("A mechanical menace, a colossal steam-powered robot, threatens the city.", YELLOW)

    while True:
        print_slow("You have three choices:", YELLOW)
        print_slow("1. Engage in a battle with the steam-powered robot.")
        print_slow("2. Attempt to sabotage the robot from within.")
        print_slow("3. Seek the help of an underground resistance group.")

        choice = input("Enter '1', '2', or '3': ").strip()

        if choice == "1":
            print_slow("You confront the steam-powered robot in an epic showdown...", YELLOW)
            if random.choice([True, False]):
                print_slow("With determination and cunning, you defeat the robot!", GREEN)
                print_slow("The city celebrates your victory, and you are hailed as a hero.", GREEN)
                game_win_screen()
            else:
                print_slow("The steam-powered robot's immense strength overwhelms you.")
                game_over()
        elif choice == "2":
            print_slow("You sneak into the heart of the robot to sabotage its mechanisms...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your sabotage efforts cripple the robot, and it grinds to a halt.", GREEN)
                print_slow("The city is saved, and you are celebrated as a hero of the steampunk realm.", GREEN)
                game_win_screen()
            else:
                print_slow("Your sabotage attempt triggers an alarm, and the robot captures you.")
                game_over()
        elif choice == "3":
            print_slow("You seek out the underground resistance group for assistance...", YELLOW)
            if random.choice([True, False]):
                print_slow("The resistance group provides you with advanced weaponry.", GREEN)
                print_slow("With their help, you defeat the steam-powered robot and save the city.", GREEN)
                game_win_screen()
            else:
                print_slow("The resistance group's plan fails, and the robot's forces overwhelm you.")
                game_over()
        else:
            print_slow("Invalid choice. Please enter '1', '2', or '3'.", RED)

# ... (rest of the code)


def space_adventure():
    print_slow("You find yourself aboard a futuristic spaceship, hurtling through the cosmos.", YELLOW)
    print_slow("A distress signal from a nearby space station reveals that it's under attack by an alien warship.", YELLOW)
    
    while True:
        print_slow("You have three choices:", YELLOW)
        print_slow("1. Engage in a space battle with the alien warship.")
        print_slow("2. Attempt to negotiate with the alien race.")
        print_slow("3. Try to sneak onto the space station.")
        
        choice = input("Enter '1', '2', or '3': ").strip()
        
        if choice == "1":
            print_slow("You pilot your spaceship into an epic space battle with the alien warship...", YELLOW)
            if random.choice([True, False]):
                print_slow("With superior piloting skills and well-aimed shots, you defeat the alien warship!", GREEN)
                print_slow("The space station is saved, and you are hailed as a hero of the cosmos.", GREEN)
                game_win_screen()
            else:
                print_slow("The alien warship's firepower overwhelms your spaceship, and you're left adrift in space.")
                game_over()
        elif choice == "2":
            print_slow("You attempt to negotiate with the alien race...", YELLOW)
            if random.choice([True, False]):
                print_slow("The aliens agree to peace, and you successfully avert the conflict.", GREEN)
                game_win_screen()
            else:
                print_slow("The alien race remains hostile and attacks your spaceship.")
                game_over()
        elif choice == "3":
            print_slow("You stealthily maneuver your spaceship to sneak onto the space station...", YELLOW)
            if random.choice([True, False]):
                print_slow("Your stealthy approach allows you to infiltrate the space station successfully.", GREEN)
                game_win_screen()
            else:
                print_slow("Your sneaking attempt is detected, and the space station's defenses capture you.")
                game_over()
        else:
            print_slow("Invalid choice. Please enter '1', '2', or '3'.", RED)

def game_win_screen():
    print_slow("Congratulations! You've achieved a victorious outcome in your adventure.", GREEN)
    print_slow("Your journey has come to a triumphant end.", GREEN)
    print_slow("Thank you for playing!", YELLOW)
    exit()

def game_over():
    print_slow("Unfortunately, your adventure has reached a premature end.", RED)
    print_slow("But fear not, for there are always more adventures awaiting.", RED)
    print_slow("Would you like to start a new adventure?")

    while True:
        choice = input("Enter 'yes' or 'no': ").strip().lower()

        if choice == "yes":
            start_game()
        elif choice == "no":
            print_slow("Thank you for playing! Until next time.", YELLOW)
            exit()
        else:
            print_slow("Invalid choice. Please enter 'yes' or 'no'.", RED)

if __name__ == "__main__":
    start_game()
