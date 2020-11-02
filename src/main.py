from src.smart_house import SmartHouse


def start_program():
    smart_house = SmartHouse()
    smart_house.start_notifying_event()


if __name__ == '__main__':
    start_program()
