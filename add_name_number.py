def add_name(numbers):
    print("Добавить имя и номер")
    name = input("Имя: ")
    phone = input("Номер: ")
    numbers[name] = phone
        
    f = open("PhoneBook.txt", "a")
    mystring = ""
    for x in numbers:
        mystring = x +" " + numbers[x] + "\n"
    f.write(mystring)
    f.close()
    print()