def find_contact(numbers):
    print("Найти контакт")
    name = input("введите имя: ")
    if name in numbers:
        print("Номер телефона", numbers[name])
        print()
    else:
        print(name, "Контакт не найден")
        print()     