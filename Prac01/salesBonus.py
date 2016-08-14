"""
Program to calculate
and display
a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MENU = "Please enter you sales"
print(MENU)
sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = 10
        print("Result: Your bonus is $" + str(sales * bonus / 100))
    elif sales >= 1000:
        bonus=15
        print("Result: Your bonus is $"+str(sales*bonus/100))
    else:
        print("Invalid option")
    print(MENU)
    sales = float(input("Enter sales: $"))
print("Thank you.")
