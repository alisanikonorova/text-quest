# rooms/bolshaya.py
from inventory import get_items

def bolshaya_room() -> str:
    print("\n" + "="*50)
    print("Большая комната. В центре — старый стол с пыльной лампой. Три двери: налево, направо и прямо.")
    print(f"Ваш инвентарь: {get_items()}")
    choice = input("Куда пойдёте? 1 - налево (Комната 2), 2 - направо (Комната 3), 3 - прямо (Комната 4): ")

    if choice == "1":
        return "komnata_2"
    elif choice == "2":
        return "komnata_3"
    elif choice == "3":
        return "komnata_4"
    else:
        print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")
        return "bolshaya"