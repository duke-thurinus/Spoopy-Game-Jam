import skill_check, user
from commands import warpdrive
from random import randint
from start import initilize

def is_dead(ship):
    if ship["structure"] < 1:
        return True
    else:
        return False

def enemy_turn(ship, enemy):
    targets = ["engines", "weapons", "sensors"]
    target = targets[randint(0,2)]
    return fire(enemy, ship, target)

def take_damage(ship, damage, target):
    shields = ship["shields"]
    if shields > 0:
        shields -= damage
        if shields < 0:
            damage = shields * -1
            shields = 0
    ship["shields"] = shields

    structure = ship["structure"]
    system = ship[target]
    if damage > 0:
        structure -= damage // 2
        system -= damage // 2
    if system < 0:
        system = 0
    ship["structure"] = structure
    ship[target] = system
    
    return ship

def fire(firing_ship, defending_ship, target):
    damage = randint(0, firing_ship["weapons"])
    print(damage)
    defending_ship = take_damage(defending_ship, damage, target)
    print(defending_ship)
    return defending_ship

def your_turn(gamestate, ship, enemy):
    command = input("What are going to do captain? ")
    if command == "fire":
        target = user.get_from_list(["engines", "weapons", "sensors"])
        enemy = fire(ship, enemy, target)
        return gamestate, ship, enemy, not is_dead(enemy)
    elif command == "warp":
        if skill_check.engine(ship, randint(0, enemy["engines"])):
            gamestate = warpdrive(gamestate)
            return gamestate, ship, enemy, False
        else:
            print("You failed to escape!")
            return gamestate, ship, enemy, True

def do_turn(gamestate, ship, enemy, turn):
    if turn == 1:
        gamestate, ship, enemy, fighting = your_turn(gamestate, ship, enemy)
        return gamestate, ship, enemy, fighting , turn
    else:
        ship = enemy_turn(ship, enemy)
        return gamestate, ship, enemy, not is_dead(ship), turn

#tracks turns
def combat(gamestate, enemy):
    enemy = gamestate["ships"][enemy]
    ship = gamestate["ships"]["my ship"]
    fighting = True
    turn = 1
    print("enemy:",enemy)
    while fighting:
        gamestate, ship, enemy, fighting, turn = do_turn(gamestate, ship, enemy, turn)
        turn = turn % 2 + 1 #switch player
        print("me:",ship)
        print("enemy:",enemy)
    gamestate["ships"]["my ship"] = ship
