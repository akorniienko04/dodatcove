def create_character_system():
    """Ініціалізує систему управління персонажами"""
    return {}

def create_character(system):
    """
    Створює нового персонажа.
    Запитує ім'я та клас персонажа.
    """

    while True:
        name = input("Введіть ім'я героя: ")
        class_of_char = input("Введіть клас вашого героя(Маг, Воїн, Крадій): ").lower()
        if class_of_char in ["маг", "воїн", "крадій"]:
            print("Непоганий вибір!")
            break

        print("Такий клас відсутній!")

    system[name] = {
        'class': class_of_char,
        'level': 0,
        'stats' : {
            'магія': 0,
            'красномовність': 0,
            'скритність': 0
        }
    }

    print(f"Герой {name} успішно створений!")


def level_up(system):
    """
    Підвищує рівень персонажа.
    Дозволяє покращити одну характеристику.
    """
    name = input("Ввведіть ім'я героя для підвищення рівня: ")
    if name in system:
        system[name]['level'] += 1
        print(f"Рівень твого героя був підвищений! {name} тепер {system[name]['level']} рівня!")
    else:
        print("Ім'я такого героя відсутнє!")

    while True:
        stat_name = input("Яку характеристику ти обираєш для підвищення? (Магія, Красномовність, Скритність): ").lower()
        if stat_name in ["магія", "красномовність", "скритність"]:
            print("Файно!")
        #if stat_name in system:
            system[name]['stats'][stat_name] += 10
            print(f"{stat_name.upper()} була вдосконалена!")
            break

        print("Така здібність відсутня!")

def display_characters(system):

    """Показує всіх створених персонажів та їх характеристики"""
    if not system:
        print("Персонаж відсутній!")
    else:
        for name, others in system.items():
            print(f"Герой: {name}")
            print(f"  Клас: {others['class']}")
            print(f"  Рівень: {others['level']}")
            print(f"  Здібності: {others['stats']}")
    pass


if __name__ == '__main__':
    system = create_character_system()
    create_character(system)
    level_up(system)
    display_characters(system)