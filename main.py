
def initilize():
    galaxy = [  ["Eta Helion", "Agromega", "Pi Abbidon"]#Sol
               ,["Agromega", "Sol"]#Eta Helion
               ,["Eta Helion", "Eurian", "Sol"]#Agromega
               ,["Sol", "Devolin"]#Pi Abbidon
               ,["Pi Abbidon", "Euridian", "Ross 128"]#Devolin
               ,["Agromega", "Acrux", "Carina 369", "Devolin"]#Euridian
               ,["Euridian"]#Acrux
               ,["Euridian", "Ross 128"]#Carina 369
               ,["Devolin", "Carina 369"]#Ross 128
        ]

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
    initilize()
    while True:
        print(print_text())
        use_command(get_command())

loop()
