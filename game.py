from game_module import *
from game_module_func import *



session = True


while session:
    print("Hello !")
    menu = game_menu()
    if menu == "1":                                                                                                     # игровой процесс
        name, sleep = create_var()
        Char = Character(name, int(sleep))
        Opponent = Character("Computer", int(sleep))
        while True:
            if Char.step() == 0:
                print("Your step:")
                tp, value = Char.skill()
                if tp == "damage":
                    print("Your opponent`s", end=" ")
                    Opponent.dmg(value)
                else:
                    print("Your", end=" ")
                    Char.hilling()
                y_hp = Char.check_HP()
                op_hp = Opponent.check_HP()
                if y_hp <= 0:
                    print("You lose " + name + ". Try again.\n")
                    del Char
                    del Opponent
                    break
                if op_hp <= 0:
                    print("You win " + name + ".\n")
                    del Char
                    del Opponent
                    break
            else:
                print("Your opponent`s step:")
                op_hp = Opponent.check_HP()
                if op_hp <= 35:                                                                                         # режим увеличенного шанса исцеления компьютера
                    tp, value = Opponent.low_hp_computer()
                    if tp == "damage":
                        print("Your", end=" ")
                        Char.dmg(value)
                    else:
                        print("Your opponent`s", end=" ")
                        Opponent.hilling()
                    y_hp = Char.check_HP()
                    op_hp = Opponent.check_HP()
                    if y_hp <= 0:
                        print("You lose " + name + ". Try again.\n")
                        del Char
                        del Opponent
                        break
                    if op_hp <= 0:
                        print("You win " + name + ".\n")
                        del Char
                        del Opponent
                        break
                else:                                                                                                   # обычный режим
                    tp, value = Opponent.skill()
                    if tp == "damage":
                        print("Your", end=" ")
                        Char.dmg(value)
                    else:
                        print("Your opponent`s step", end=" ")
                        Opponent.hilling()
                    y_hp = Char.check_HP()
                    op_hp = Opponent.check_HP()
                    if y_hp <= 0:
                        print("You lose " + name + ". Try again.\n")
                        del Char
                        del Opponent
                        break
                    if op_hp <= 0:
                        print("You win " + name + ".\n")
                        del Char
                        del Opponent
                        break
    if menu == "2":                                                                                                     # завершение сеанса
        print("Good luck.")
        session = False