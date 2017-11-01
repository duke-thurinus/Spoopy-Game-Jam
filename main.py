import commands, start, game_data
from ship_combat import combat
from user import clean_input

def print_loc(gamestate):
    loc = gamestate["location"][1]
    
    if loc == "":
        print("\nYou are in the", gamestate["location"][0].title(), "system.")
    else:
        print("\nYou are near the planet", loc.title(), "in the system"
              , gamestate["location"][0].title() + ".")

def get_command(gamestate):
    command = clean_input("What are going to do captain? ")

    if command == "quit":
        return "q"
    elif command == "warp":
        return commands.warpdrive(gamestate)
    elif command == "impulse":
        gamestate = commands.impulse(gamestate)
        encounter = game_data.encounter_check(gamestate["location"][1], gamestate)
        if encounter:
            gamestate = encounter
        return gamestate
    else:
        return False

def loop():
    gamestate = start.initilize()
    while True:
        print_loc(gamestate)
        update = get_command(gamestate)
        if update == "q":
            break
        elif not update:
            print("We don't know what to do captain!")
        else:
            gamestate = update

loop()
