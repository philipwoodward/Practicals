try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print ("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print ("Cannot divide by zero!")
print ("Finished.")
"""         Q1 A ValueError will occur if  anything but a number is entered.
            Q2 A ZeroDivisionError happens if the divisor is zero.
            Q3 Yes - you could add a While loop so if a zero is entered, an error message could ask for a number that was not zero
"""
