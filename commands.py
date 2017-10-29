import user

def get_warp_options(gamestate):
    return gamestate["galaxy"][gamestate["location"][0]]

def warpdrive(gamestate):
    warp_options = get_warp_options(gamestate)
    while True:
        print("\nThe systems in range are:")
        for i in warp_options:
            print(i.title())
        
        loc = user.clean_input("\nWhich system do you want to warp to? ")
        
        if loc == "quit":
            return gamestate
        
        if loc in warp_options:
            gamestate["location"] = [ loc, "" ]
            return gamestate

def get_impulse_options(gamestate):
    return gamestate["systems"][gamestate["location"][0]]

def impulse(gamestate):
    impulse_options = get_impulse_options(gamestate)
    while True:
        print("\nThe planets in the system are:")
        if not impulse_options[0]:
            print("There are no planets in the system")
            return gamestate
        else:
            for i in impulse_options:
                print(i.title())

        loc = user.clean_input("\nWhich planet do you want to fly to? ")
        
        if loc == "quit":
            return gamestate
        
        if loc in impulse_options:
            gamestate["location"] = [ gamestate["location"][0], loc]
            return gamestate
        
