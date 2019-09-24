def game_menu():
    """Return of parameters for menu"""
    print("To start game press 1.\nTo leave game press 2.")
    menu = input("Input your choice:\n")
    if menu == "1":
        return menu
    if menu == "2":
        return menu
    else:
        return game_menu()


def create_var():
    """Creating of variables for game"""
    name = input("Input your name:")
    sleep = input("Input time of sleep. If you want fast result choose 0.")
    return (name, sleep)