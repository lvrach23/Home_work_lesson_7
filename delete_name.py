def delete(numbers):
    print("Удаление контакта")
    name = input("введите имя контакта: ")
    if name in numbers:
        with open("PhoneBook.txt", "r") as fp:
            lines = fp.readlines()

        with open("PhoneBook.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != name + " " + numbers[name]:
                    fp.write(line)
        del numbers[name]
        print('Контакт удален')
    else:
        print(name, "Контакт не найден")
        print()
