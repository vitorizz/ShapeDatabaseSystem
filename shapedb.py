from operations import *
from shapes import *


def menu():
    print("Here are your options:\n"
          + "Enter 1 for LOAD\n"
          + "Enter 2 for TOSET\n"
          + "Enter 3 for SAVE\n"
          + "Enter 4 for PRINT\n"
          + "Enter 5 for SUMMARY\n"
          + "Enter 6 for DETAILS\n"
          + "Enter 7 for QUIT\n"
          )
    choice = input()
    return choice


def performingOptions():
    choice = menu()
    shape_list = list()
    while choice != '7':
        if choice == '1':
            file = input("Enter the file name containing the database: ")
            shape_list = load(file)
        if choice == '2':
            temp_list = toSet(shape_list)
            shape_list = temp_list
        if choice == '3':
            file = input(
                "Enter the file name you wish to add the database to: ")
            save(file, shape_list)
        if choice == '4':
            print_(shape_list)
        if choice == '5':
            summary(shape_list)
        if choice == '6':
            print(details(shape_list))
        choice = menu()
        print()
    quit()


def main():
    print("Welcome to the shape Program!")
    performingOptions()


if __name__ == "__main__":
    main()
