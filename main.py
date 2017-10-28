import commands, start
from text import input_clean

def print_loc(gamestate):
    loc = gamestate["location"][1]
    
    if loc == "":
        print("\nYour are in the", gamestate["location"][0].title(), "system.")
    else:
        print("\nYou are near the planet", loc.title(), "in the system"
              , gamestate["location"][0].title() + ".")

def get_command(gamestate):
    command = input("What are going to do captain? ")
    command = input_clean(command)

    if command == "warp":
        return commands.warpdrive(gamestate)
    elif command == "impulse":
        return commands.impulse(gamestate)
    else:
        return False

def loop():
    gamestate = start.initilize()
    while True:
        print_loc(gamestate)
        update = get_command(gamestate)
        if not update:
            print("We don't know what to do captain!")
        else:
            gamestate = update

loop()
