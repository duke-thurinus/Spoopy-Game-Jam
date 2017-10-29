def clean_input(string):
    string = input(string)
    string = string.lower()
    return string.strip()

def get_from_list(options):
    while True:
        for i in options:
            print(str(options.index(i) + 1) + ":", i)
        
        try:
            choice = int(input("Which option do you choose? "))
            if choice < 1:
                print("Not a valid selection.")
                continue
            choice = options[ choice - 1]
        except (ValueError, IndexError):
            print("Not a valid selection.")
            continue

        return choice

