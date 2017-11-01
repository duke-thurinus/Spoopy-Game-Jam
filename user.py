def clean_input(string):
    string = input(string)
    string = string.lower()
    return string.strip()

def get_from_list(options, question, allow_quit):
    while True:
        if allow_quit:
            print("0: Quit")
        for i in options:
            print(str(options.index(i) + 1) + ":", i.title())
        if question == None:
            question = "Which option do you choose? "
        try:
            choice = int(input(question))
            if choice == 0 and allow_quit:
                return False
            if choice < 1:
                print("Not a valid selection.")
                continue
            choice = options[ choice - 1]
        except (ValueError, IndexError):
            print("Not a valid selection.")
            continue

        return choice

