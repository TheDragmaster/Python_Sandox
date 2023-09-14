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
    print_slow(f"You find yourself in {location}.", YELLOW)
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
    print_slow("Do you want to fight the snake or try to sneak past it?")

    while True:
        choice = input("Enter 'fight' or 'sneak': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the giant snake in a fierce battle...", YELLOW)
            if random.choice([True, False]):
                print_slow("With determination, you defeat the giant snake in a battle of wits and strength!")
                print_slow("The snake's lair holds a valuable treasure chest!", GREEN)
                print_slow("Congratulations! You've conquered the snake and found treasure.")
                cave_treasure()
            else:
                print_slow("The giant snake overpowers you and defeats you in combat.")
                print_slow("Game Over.", RED)
                death_adventures()
        elif choice == "sneak":
            print_slow("You attempt to sneak past the giant snake...", YELLOW)
            if random.choice([True, False]):
                print_slow("You successfully sneak past the snake and discover a treasure chest!", GREEN)
                print_slow("Congratulations! You've found treasure without a fight.")
                cave_treasure()
            else:
                print_slow("The snake notices your attempt to sneak and attacks you.")
                print_slow("Game Over.", RED)
                death_adventures()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'sneak'.", RED)

def cave_treasure():
    print_slow("You open the treasure chest and find a vast fortune in gold and jewels!")
    print_slow("The sight of the treasure takes your breath away.", YELLOW)
    print_slow("Congratulations! You've won the game.", GREEN, True)
    choose_next_adventure()

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
            print_slow("Game Over.", RED)
            death_adventures()
        else:
            print_slow("Invalid choice. Please enter 'downstream' or 'upstream'.", RED)

def forward_path():
    print_slow("You come across a rickety bridge leading to a castle.")
    print_slow("The castle looms ahead, its towering spires shrouded in mystery.")
    print_slow("Do you want to cross the bridge or go back to the forest?")

    while True:
        choice = input("Enter 'cross' or 'back': ").strip().lower()

        if choice == "cross":
            print_slow("You cross the bridge and enter the castle...", YELLOW)
            castle_path()
        elif choice == "back":
            print_slow("You decide to go back to the forest.")
            start_game()
        else:
            print_slow("Invalid choice. Please enter 'cross' or 'back'.", RED)

def castle_path():
    print_slow("Inside the castle, you encounter a dragon!")
    print_slow("The dragon is massive, and its scales shimmer with an otherworldly glow.")
    print_slow("The treasure chest lies behind the dragon, and the room echoes with danger.")
    print_slow("Do you want to fight the dragon or try to negotiate for the treasure?")

    while True:
        choice = input("Enter 'fight' or 'negotiate': ").strip().lower()

        if choice == "fight":
            print_slow("You engage the dragon in a fierce battle...", YELLOW)
            if random.choice([True, False]):
                print_slow("After a heroic battle, you manage to defeat the dragon!", GREEN)
                print_slow("The dragon's treasure is now yours.", YELLOW)
                print_slow("Congratulations! You've slain the dragon and acquired the treasure.")
                castle_treasure()
            else:
                print_slow("The dragon's power is too great, and it overcomes you in battle.")
                print_slow("Game Over.", RED)
                death_adventures()
        elif choice == "negotiate":
            print_slow("You attempt to negotiate with the dragon...", YELLOW)
            if random.choice([True, False]):
                print_slow("The dragon is impressed by your courage and wisdom.", GREEN)
                print_slow("It agrees to share the treasure with you.")
                print_slow("Congratulations! You've acquired the treasure without a fight.")
                castle_treasure()
            else:
                print_slow("The dragon rejects your offer and attacks you.")
                print_slow("Game Over.", RED)
                death_adventures()
        else:
            print_slow("Invalid choice. Please enter 'fight' or 'negotiate'.", RED)

def castle_treasure():
    print_slow("You open the treasure chest and find a vast fortune in gold, jewels, and rare artifacts!")
    print_slow("The treasures glitter in the dim light of the castle.", YELLOW)
    print_slow("Congratulations! You've won the game.", GREEN, True)
    choose_next_adventure()

def riverbank_challenge():
    print_slow("You reach the calm riverbank downstream.")
    print_slow("As you explore, you notice a hidden path that leads to a mystical forest.")
    print_slow("The forest is filled with magical creatures and secrets.")
    print_slow("Do you want to explore the mystical forest or return to the river?")

    while True:
        choice = input("Enter 'explore' or 'return': ").strip().lower()

        if choice == "explore":
            print_slow("You venture into the mystical forest, ready for a new adventure...", YELLOW)
            mystical_forest_adventure()
        elif choice == "return":
            print_slow("You decide to return to the river and continue your journey downstream.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'explore' or 'return'.", RED)

def mystical_forest_adventure():
    print_slow("In the mystical forest, you encounter a friendly talking squirrel named Squeaky.")
    print_slow("Squeaky informs you about a magical portal hidden deep within the forest.")
    print_slow("The portal is said to lead to a land of endless wonders and challenges.")
    print_slow("Do you want to follow Squeaky to find the portal or go back to the riverbank?")

    while True:
        choice = input("Enter 'portal' or 'back': ").strip().lower()

        if choice == "portal":
            print_slow("You follow Squeaky through the dense forest, and together you discover the magical portal...", YELLOW)
            portal_adventure()
        elif choice == "back":
            print_slow("You decide to return to the riverbank.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'portal' or 'back'.", RED)

def portal_adventure():
    print_slow("You step through the magical portal and find yourself in a realm of enchanting beauty and mystery.")
    print_slow("This new world is filled with wonders and challenges beyond your imagination.", YELLOW)
    print_slow("As you explore this magical land, you come across two more portals, each leading to a different adventure.", YELLOW)
    print_slow("Which portal do you choose?")

    while True:
        print_slow("Enter 'portal1' to enter the first portal or 'portal2' to enter the second portal.", YELLOW)
        choice = input().strip().lower()

        if choice == "portal1":
            print_slow("You step through the first portal and embark on a new adventure...", YELLOW)
            steampunk_adventure()
        elif choice == "portal2":
            print_slow("You step through the second portal and embark on a different adventure...", YELLOW)
            space_adventure()
        else:
            print_slow("Invalid choice. Please enter 'portal1' or 'portal2'.", RED)

def steampunk_adventure():
    print_slow("You find yourself in a bustling city filled with towering steam-powered machines and airships.", YELLOW)
    print_slow("A mysterious inventor approaches you and tells you about a rogue automaton terrorizing the city.", YELLOW)
    print_slow("The inventor offers you a mechanized suit to stop the automaton.")
    print_slow("Do you want to accept the mission and confront the rogue automaton?")
    
    while True:
        choice = input("Enter 'accept' or 'decline': ").strip().lower()

        if choice == "accept":
            print_slow("You don the mechanized suit and set out to confront the rogue automaton...", YELLOW)
            steampunk_boss_fight()
        elif choice == "decline":
            print_slow("You decline the mission and continue exploring the steampunk city.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'accept' or 'decline'.", RED)

def steampunk_boss_fight():
    print_slow("You track down the rogue automaton to a steam-powered factory.")
    print_slow("The automaton is a formidable opponent with gears and pistons, but you're armed with advanced technology.")
    print_slow("Prepare for a high-stakes boss fight!")

    if random.choice([True, False]):
        print_slow("With precise timing and strategy, you defeat the rogue automaton!")
        print_slow("The city is safe, and the inventor rewards you with a rare steampunk artifact.", GREEN)
        print_slow("Congratulations! You've conquered the steampunk adventure and acquired a valuable artifact.")
        choose_next_adventure()
    else:
        print_slow("The rogue automaton overwhelms you with its relentless power.")
        print_slow("Game Over.", RED)
        death_adventures()

def space_adventure():
    print_slow("You find yourself aboard a futuristic spaceship, hurtling through the cosmos.", YELLOW)
    print_slow("A distress signal from a nearby space station reveals that it's under attack by an alien warship.", YELLOW)
    print_slow("Do you want to respond to the distress signal and engage the alien warship?")
    
    while True:
        choice = input("Enter 'respond' or 'ignore': ").strip().lower()

        if choice == "respond":
            print_slow("You pilot your spaceship toward the space station and prepare for an epic space battle...", YELLOW)
            space_boss_fight()
        elif choice == "ignore":
            print_slow("You decide to ignore the distress signal and continue your journey through space.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'respond' or 'ignore'.", RED)

def space_boss_fight():
    print_slow("You confront the alien warship in a fierce space battle.")
    print_slow("The warship is heavily armed and fires powerful energy beams at your spaceship.")
    print_slow("Get ready for a high-intensity boss fight in the depths of space!")

    if random.choice([True, False]):
        print_slow("With superior piloting skills and well-aimed shots, you defeat the alien warship!")
        print_slow("The space station is saved, and you are hailed as a hero of the cosmos.", GREEN)
        print_slow("Congratulations! You've conquered the space adventure and saved the space station.")
        choose_next_adventure()
    else:
        print_slow("The alien warship's firepower overwhelms your spaceship, and you're left adrift in space.")
        print_slow("Game Over.", RED)
        death_adventures()

def death_adventures():
    print_slow("You have met an unfortunate end. Your journey in this world has come to an end.", RED)
    print_slow("As your consciousness fades, you see a bright light and a dark abyss before you.", YELLOW)
    print_slow("You must make a choice:", YELLOW)
    print_slow("Enter 'light' to walk into the light and start a new adventure in heaven.", YELLOW)
    print_slow("Enter 'dark' to walk into the dark abyss and embark on a new adventure in the abyss.", YELLOW)

    while True:
        choice = input().strip().lower()

        if choice == "light":
            print_slow("You walk into the light and find yourself in a heavenly realm...", YELLOW)
            heaven_adventure()
        elif choice == "dark":
            print_slow("You walk into the dark abyss, and darkness surrounds you...", YELLOW)
            abyss_adventure()
        else:
            print_slow("Invalid choice. Please enter 'light' or 'dark'.", RED)

def heaven_adventure():
    print_slow("You are in a serene and beautiful realm where everything is peaceful.", YELLOW)
    print_slow("But there is a celestial challenge ahead. You encounter a guardian angel who presents you with a quest.", YELLOW)
    print_slow("Will you accept the quest and face the celestial challenge?")
    
    while True:
        choice = input("Enter 'accept' or 'decline': ").strip().lower()

        if choice == "accept":
            print_slow("You accept the quest and prepare to embark on your heavenly adventure...", YELLOW)
            heaven_boss_fight()
        elif choice == "decline":
            print_slow("You decline the quest and bask in the tranquility of this heavenly realm.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'accept' or 'decline'.", RED)

def heaven_boss_fight():
    print_slow("You follow the guidance of the guardian angel and arrive at the celestial challenge.")
    print_slow("A powerful celestial being awaits you, ready to test your spirit and valor.")
    print_slow("Prepare for a divine boss fight!")

    if random.choice([True, False]):
        print_slow("With unwavering faith and determination, you conquer the celestial challenge!", GREEN)
        print_slow("You are rewarded with divine blessings and enlightenment.")
        print_slow("Congratulations! You've conquered the heavenly adventure and gained celestial wisdom.")
        choose_next_adventure()
    else:
        print_slow("The celestial being's power overwhelms you, and you are sent back to the heavenly realm.", RED)
        print_slow("Game Over.", RED)
        death_adventures()

def abyss_adventure():
    print_slow("You find yourself in a dark and foreboding realm filled with shadows and mysterious creatures.", YELLOW)
    print_slow("A sinister figure appears before you, offering you a dark and perilous quest.", YELLOW)
    print_slow("Do you dare to accept the dark quest and face the malevolent forces of the abyss?")
    
    while True:
        choice = input("Enter 'accept' or 'decline': ").strip().lower()

        if choice == "accept":
            print_slow("You accept the dark quest, and the sinister figure leads you into the heart of the abyss...", YELLOW)
            abyss_boss_fight()
        elif choice == "decline":
            print_slow("You reject the dark quest and try to find a way to escape this menacing realm.")
            choose_next_adventure()
        else:
            print_slow("Invalid choice. Please enter 'accept' or 'decline'.", RED)

def abyss_boss_fight():
    print_slow("You confront the malevolent forces of the abyss in a nightmarish battle.")
    print_slow("The dark entities are relentless and formidable.")
    print_slow("Prepare for a harrowing boss fight in the depths of darkness!")

    if random.choice([True, False]):
        print_slow("With sheer determination and a glimmer of hope, you overcome the malevolent forces of the abyss!", GREEN)
        print_slow("You emerge from the abyss with newfound strength and resilience.")
        print_slow("Congratulations! You've conquered the abyssal adventure and faced the darkness head-on.")
        choose_next_adventure()
    else:
        print_slow("The malevolent forces of the abyss consume you, and your essence is forever trapped in darkness.", RED)
        print_slow("Game Over.", RED)
        death_adventures()

def choose_next_adventure():
    print_slow("Would you like to embark on a new adventure?")
    print_slow("Enter 'yes' to start a new adventure or 'no' to end the game.", YELLOW)

    while True:
        choice = input("Enter 'yes' or 'no': ").strip().lower()

        if choice == "yes":
            start_game()
        elif choice == "no":
            print_slow("Thank you for playing! Goodbye.", GREEN, True)
            exit()
        else:
            print_slow("Invalid choice. Please enter 'yes' or 'no'.", RED)

if __name__ == "__main__":
    start_game()
