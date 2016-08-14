"""
Program to calculate and display
the electricity bill. Inputs will be price per kWh in cents,
daily use in kWh and the number of days in the billing period
"""
electricity_price = int(input("Enter the price of electricity in cents per kilowatt hour: "))
daily_use = float(input("Enter the kilowatt hours of electricity use per day: "))
number_days = int(input("Enter the number of days in the billing period: "))

print("The estimated electricity bill is $", electricity_price * daily_use * number_days /100)

print("Thank you.")
