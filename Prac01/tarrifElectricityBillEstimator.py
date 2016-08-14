"""
Program to calculate and display
the electricity bill. Inputs will be price per kWh in cents,
daily use in kWh and the number of days in the billing period
"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = 1
while tariff == 1:
    tariff = int(input("Enter which tariff please - 11 or 31: "))
    if tariff == 11:
        tariff = TARIFF_11
    elif tariff == 31:
        tariff = TARIFF_31
    else:
        tariff = 1
print(tariff)
daily_use = float(input("Enter the kilowatt hours of electricity use per day: "))
number_days = int(input("Enter the number of days in the billing period: "))
print("The estimated electricity bill is $", round(tariff * daily_use * number_days,2))
print("Thank you.")
