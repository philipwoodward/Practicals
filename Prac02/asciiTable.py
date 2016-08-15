"""
Create a function called get_number(lower, upper) to get a number, making sure that user input is
numeric and within the given range. You can use exceptions to check the string is a valid number.
Repeatedly re-prompt for a number until a valid  one is entered, then return it."""

def main():
    print ("{:12}{:15}".format("ASCII","Characters"))
    lower = 10
    upper = 120

    for i in range(lower, upper, 11):
        print (my_number)


#def get_number(lower,upper):
    print (lower)
    print (upper)
    try:
    print ("Please enter a number which is between " + str(lower) + " and " + str(upper))
    my_number = int(input("My number is > "))
    except ValueError:
    print("Your number must be a valid number!")
    return my_number

#main()