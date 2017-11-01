import user

def get_warp_options(gamestate):
    return gamestate["galaxy"][gamestate["location"][0]]

def warpdrive(gamestate):
    warp_options = get_warp_options(gamestate)
    while True:
        print("\nThe systems in range are:")
        question = "\nWhich system do you want to warp to? "
        loc = user.get_from_list(warp_options, question, True)
        if loc:
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
            question = "\nWhich planet do you want to fly to? "
            loc = user.get_from_list(impulse_options, question, True)
            if loc:
                gamestate["location"] = [ gamestate["location"][0], loc]
            return gamestate
    return gamestate
