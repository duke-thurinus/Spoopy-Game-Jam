def get_warp_options(gamestate):
    return gamestate["galaxy"][gamestate["location"]]

def warpdrive(gamestate):
    warp_options = get_warp_options(gamestate)
    while True:
        print("\nThe systems in range are:")
        for i in warp_options:
            print(i.title())
        loc = str(input("\nWhich system do you want to warp to? "))
        loc = loc.lower()
        loc = loc.strip(" ")
        if loc in warp_options:
            gamestate["location"] = loc
            return gamestate
