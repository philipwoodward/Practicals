number_of_picks = input('How many picks would you like? > ')
import random

for i in range(1,int(number_of_picks)+1):
    random_number = 0
    my_lucky_numbers = []
    while random_number < 7:
        pick = random.randint(0,45)
        if (pick)in my_lucky_numbers:
            continue
        else:
            my_lucky_numbers.append(pick)
            random_number +=1
    my_lucky_numbers = sorted(my_lucky_numbers)
    print(my_lucky_numbers)