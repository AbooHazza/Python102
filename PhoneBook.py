


# =========================================
#           PHONE BOOK PROJECT
# =========================================


phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}

print('<><><><><><><ListOfNumbers><><><><><><>')

for number, name in phone_book.items():
    print(number, ":", name)

print('<><><><><><><><><><><><><><><><><><><><>')


def is_valid_number(number):

    if len(number) != 10:
        return False

    for char in number:
        if char < '0' or char > '9':
            return False

    return True


def find_name_by_number():

    phone_number = input("Enter the phone number: ")

    if is_valid_number(phone_number):

        if phone_number in phone_book:
            print(phone_book[phone_number])

        else:
            print("Sorry, the number is not found")

    else:
        print("This is invalid number")


def find_number_by_name():

    name = input("Enter the name: ")

    for number, owner in phone_book.items():

        if owner == name:
            print(number)
            return

    print("Sorry, the name is not found")


def add_new_contact():

    new_name = input("Add new name: ")
    new_number = input("Add new number: ")

    if is_valid_number(new_number):

        phone_book[new_number] = new_name
        print("Contact added successfully!")

    else:
        print("This is invalid number")


def display():

    print('\n===== Updated Phone Book =====')

    for number, name in phone_book.items():
        print(number, ":", name)


def main():

    find_name_by_number()
    print('---------------------')

    find_number_by_name()
    print('---------------------')

    add_new_contact()
    print('---------------------')

    display()


print('==========================')

main()

print('==========================')