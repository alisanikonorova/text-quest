# rooms/komnata_3.py
from inventory import add_item, has_item

def komnata_3() -> str:
    print("\n" + "="*50)
    print("Комната освещена тусклой лампой.")

    if not has_item("фонарик"):
        print("На полу лежит фонарик.")
    if not has_item("знание_хода"):
        print("На стене висит карта.")
    elif has_item("фонарик"):
        print("Вы уже всё здесь осмотрели.")

    choice = input("1 - взять фонарик, 2 - изучить карту, 3 - пройти в Комнату 2 (налево), 4 - вернуться: ")

    if choice == "1":
        if not has_item("фонарик"):
            print("Вы взяли фонарик.")
            add_item("фонарик")
        else:
            print("Фонарик уже у вас.")
    elif choice == "2":
        if not has_item("знание_хода"):
            print("На карте отмечен тайный ход из Комнаты 4. Запомнили.")
            add_item("знание_хода")
        else:
            print("Вы уже изучили карту.")
    elif choice == "3":
        return "komnata_2"
    elif choice == "4":
        return "bolshaya"
    else:
        print("Непонятное действие. Введите 1, 2, 3 или 4.")

    return "komnata_3"