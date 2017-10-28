import commands

def initilize():
    galaxy = {  "sol" : ["eta helion", "agromega", "pi abbidon"]
               ,"eta helion" : ["agromega", "sol"]
               ,"agromega" : ["eta helion", "eurian", "sol"]
               ,"pi abbidon" : ["sol", "devolin"]
               ,"devolin" : ["pi abbidon", "euridian", "ross 128"]
               ,"euridian" : ["agromega", "acrux", "carina 369", "devolin"]
               ,"acrux" : ["euridian"]
               ,"carina 369" : ["euridian", "ross 128"]
               ,"ross 128" : ["devolin", "carina 369"]
        }
    gamestate = { "galaxy" : galaxy , "location" : "sol" }
    return gamestate

def print_loc(gamestate):
    print("Your are in the", gamestate["location"].title(), "system.")

def get_command(gamestate):
    command = input("What are going to do captin? ")
    command = command.lower()
    command = command.strip(" ")

    if command == "warp":
        return commands.warpdrive(gamestate)
    else:
        return False

def loop():
    gamestate = initilize()
    while True:
        print_loc(gamestate)
        update = get_command(gamestate)
        if not update:
            print("We don't know what to do captain!")
        else:
            gamestate = update

loop()
