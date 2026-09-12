# main.py
from rooms.start import start_room
from rooms.bolshaya import bolshaya_room
from rooms.komnata_2 import komnata_2
from rooms.komnata_3 import komnata_3
from rooms.komnata_4 import komnata_4

def main():
    rooms = {
        "start": start_room,
        "bolshaya": bolshaya_room,
        "komnata_2": komnata_2,
        "komnata_3": komnata_3,
        "komnata_4": komnata_4,
    }

    current_room = "start"
    while current_room != "end":
        current_room = rooms[current_room]()

    print("\n" + "="*50)
    print("Спасибо за игру! Программа завершена.")

if __name__ == "__main__":
    main()