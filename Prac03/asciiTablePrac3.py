"""
Create a function called get_number(lower, upper) to get a number, making sure that user input is
numeric and within the given range. You can use exceptions to check the string is a valid number.
Repeatedly re-prompt for a number until a valid  one is entered, then return it."""

def main():
    print ("{:12}{:15}".format("ASCII","Characters"))
    lower = 10
    upper = 120
    get_number(lower,upper)

def get_number(lower,upper):
    my_number = 0
    while my_number< lower or my_number> upper:
        try:
            my_number = int(input("Please enter a number which is between " + str(lower) + " and " + str(upper)))
        except ValueError:
            print("Your number must be a valid number!")
            print(my_number)
    print (my_number)

main()
