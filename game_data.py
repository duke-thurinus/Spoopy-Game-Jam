import ship_combat

def is_ships(planet, gamestate):
    if gamestate["ship_locs"][planet]:
        combat(gamestate, gamestate[""][planet])
    else:
        return False
