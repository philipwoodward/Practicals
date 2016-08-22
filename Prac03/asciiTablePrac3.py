"""
Create a function called get_number(lower, upper) to get a number, making sure that user input is
numeric and within the given range. You can use exceptions to check the string is a valid number.
Repeatedly re-prompt for a number until a valid  one is entered, then return it."""


def main():
    print('{:12}{:15}'.format("ASCII", "Characters"))
    lower = -10
    upper = 120
    this_number = get_number(lower, upper)
    print("My number was " + str(this_number))


def get_number(lower, upper):
    my_number = 0
    valid_input = False
    while not valid_input or my_number < lower or my_number > upper:
        try:
            my_number = int(input("Please enter a number which is between " + str(lower) + " and " + str(upper) + " > "))
            valid_input = True
        except ValueError:
            print("Your number must be a valid number!")
            valid_input = False
    return my_number


main()
