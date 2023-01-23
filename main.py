from menu import print_menu
from viev_phone import view_phone
from add_name_number import add_name
from delete_name import delete
from load_file import load_file
from find_contact import find_contact

numbers = {}
menu_choice = 0
print_menu()
load_file(numbers)
while menu_choice != 5:
    menu_choice = int(input("введите номер необходимого действия (1-6): "))
    if menu_choice == 1:
        view_phone(numbers)
    elif menu_choice == 2:
        add_name(numbers)
    elif menu_choice == 3:
        delete(numbers)
    elif menu_choice == 4:
        find_contact(numbers)
