from ship_combat import combat

def encounter_check(planet, gamestate):
    if gamestate["ship_locs"][planet]:
        return combat(gamestate, gamestate["ship_locs"][planet])
    else:
        return False
