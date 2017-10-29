from random import randint

def engine(ship, difficulty):
    if randint(0, ship["engines"]) > difficulty:
        return True
    else:
        return False
