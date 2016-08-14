"""
Program to calculate and display
the total cost to ship a number of items.
If the total cost is under $100, the user gets a 10% discount.
This discount is applied before the cost is printed.
"""
number_items = int(input("Enter the number of items to ship: "))
ship_cost_total = 0
MENU = "Please enter the shipping cost for the item. $"
for i in range(number_items):
    ship_cost = float(input("Please enter the shipping cost of the item: $"))
    ship_cost_total += ship_cost
if ship_cost_total > 100:
    ship_cost_total = ship_cost_total * .9
print("The total cost of shipping these items (including any discount) is $", ship_cost_total)

print("Thank you.")
