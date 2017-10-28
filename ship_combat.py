from commands import warpdrive

def is_dead(gamestate):
    if gamestate["my_ship"]["structure"] < 1:
        return True
    else:
        return False

def enemy_turn():
    pass

def enemy_fire():
    pass

def your_turn(gamestate):
    command = input("What are going to do captain? ")
    enemy = 
    if "warp":
        enemy_fire()
        gamestate = warpdrive(gamestate)

def combat(gamestate):
    while True:
        combat_over, gamestate = your_turn(gamestate)
        if combat_over():
            return gamestate
        enemy_turn()
