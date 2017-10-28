
def print_text():
    pass

def get_command():
    command = input("What are going to do captin?")
    command = command.lower()
    command = command.strip(" ")
    return command

def use_command(command):
    pass

def loop():
    while True:
        print(print_text())
        use_command(get_command())

loop()
