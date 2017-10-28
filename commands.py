from text import input_clean

def get_warp_options(gamestate):
    return gamestate["galaxy"][gamestate["location"][0]]

def warpdrive(gamestate):
    warp_options = get_warp_options(gamestate)
    while True:
        print("\nThe systems in range are:")
        for i in warp_options:
            print(i.title())
        
        loc = str(input("\nWhich system do you want to warp to? "))
        loc = input_clean(loc)
        
        if loc in warp_options:
            gamestate["location"] = [ loc, "" ]
            return gamestate

def get_impulse_options(gamestate):
    return gamestate["systems"][gamestate["location"][0]]

def impulse(gamestate):
    impulse_options = get_impulse_options(gamestate)
    while True:
        print("\nThe planets in the system are:")
        for i in impulse_options:
            print(i.title())

        loc = str(input("\nWhich planet do you want to fly to? "))
        loc = input_clean(loc)

        if loc in impulse_options:
            gamestate["location"] = [ gamestate["location"][0], loc]
            return gamestate
        
