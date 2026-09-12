# rooms/komnata_2.py
from assets.images import CANDLE, KEY, CHEST
from inventory import add_item, remove_item, has_item

def komnata_2() -> str:
    print("\n" + "="*50)
    print("Вы вошли в тёмную комнату. Освещённую свечами.")
    print(CANDLE)

    key_taken = not has_item("ключ") and not has_item("верёвка")
    chest_opened = has_item("верёвка")

    if key_taken and not chest_opened:
        print("На полу лежит ржавый ключ, а в углу — старый сундук.")
    elif not key_taken and not chest_opened:
        print("В углу стоит старый сундук. (Ключ вы уже подобрали.)")
    elif chest_opened:
        print("В углу стоит открытый пустой сундук. (Верёвку вы уже забрали.)")

    choice = input("1 - взять ключ, 2 - открыть сундук, 3 - вернуться назад: ")

    if choice == "1":
        if not has_item("ключ") and not has_item("верёвка"):
            print("Вы подобрали ржавый ключ.")
            print(KEY)
            add_item("ключ")
        elif has_item("ключ"):
            print("Ключ уже у вас.")
        else:
            print("На полу ничего нет — ключа здесь больше не лежит.")
    elif choice == "2":
        print(CHEST)
        if has_item("ключ"):
            print("Вы открыли сундук ключом. Внутри — верёвка! Вы берёте её.")
            add_item("верёвка")
            remove_item("ключ")
        elif has_item("верёвка"):
            print("Сундук уже открыт и пуст.")
        else:
            print("Сундук заперт. Нужен ключ.")
    elif choice == "3":
        return "bolshaya"
    else:
        print("Непонятное действие. Введите 1, 2 или 3.")

    return "komnata_2"