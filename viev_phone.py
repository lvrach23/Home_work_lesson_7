def view_phone(numbers):
    print("Телефонный справочник:")
    for x in numbers.keys():
        print("Имя: ", x, "\tНомер:", numbers[x])
    print()
