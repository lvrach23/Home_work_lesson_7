def load_file(numbers):
    f = open("PhoneBook.txt", "r")
    if(f.readable):
        arr={}
        for x in f:
            arr=x.split()
            name = arr[0]
            phone = arr[1]
            numbers[name] = phone   
    f.close()
    print()