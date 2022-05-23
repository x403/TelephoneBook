telephone_book = {
    '1111111111': 'Amal',
    '2222222222': 'Mohammed',
    '3333333333': 'Khadijah',
    '4444444444': 'Abdullah',
    '5555555555': 'Rawan',
    '6666666666': 'Faisal',
    '7777777777': 'Layla'}

def SearchByNumber():
    Key = input('Write a number to get an owner name: ')
    if len(Key) > 10 or len(Key) < 10:
        print("This is invalid number")
    elif Key in telephone_book:
        print(telephone_book[f'{Key}'])
    elif Key not in telephone_book:
        print("Sorry, the number is not found ")
    else:
        print("This is invalid number")

def SearchByName():
    user_input = input("Write a name to get an owner number: ")
    for number, name in telephone_book.items():
        if user_input == name:
            print(number)
            break
    else:
        print("This is invalid name")

def AddUser():
    add_number = input("Write a number: ")
    add_name = input("write a name of the owner number: ")
    telephone_book.update({f'{add_number}': f'{add_name}'})
    print("The number has been added successfully " , telephone_book)

user_choose = int(input("Press 1 to search by number, press 2 to add a new number, press 3 to search by name, prees 0 to exit: "))
while user_choose != 0:
    if user_choose == 1:
        SearchByNumber()
        user_choose = int(input("Press 1 to search by number, press 2 to add a new number, press 3 to search by name, prees 0 to exit: "))

    elif user_choose ==2:
        AddUser()
        user_choose = int(input("Press 1 to search by number, press 2 to add a new number, press 3 to search by name, prees 0 to exit: "))

    elif user_choose ==3:
        SearchByName()
        user_choose = int(input("Press 1 to search by number, press 2 to add a new number, press 3 to search by name, prees 0 to exit: "))

    else:
        print("You have to enter a correct number. ")
        user_choose = int(input("Press 1 to search by number, press 2 to add a new number, press 3 to search by name, prees 0 to exit: "))
