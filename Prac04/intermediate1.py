"""This programme asks the user for 5 numbers which are stored in a list.
Various things (min, max, sum and length) are then output"""

# import math
number_list = []
how_many_inputs = 5
for i in range(0, how_many_inputs, 1):
    list_num = input('Please input a number >  ')
    number_list.append(list_num)
print(number_list)
print('The smallest number was ' + min(number_list))
print('The first number is ' + number_list[0])
print('The last number is ' + number_list[-1])
print('The largest number is ' + max(number_list))
total_of_list = 0
for i in range(0, how_many_inputs, 1):
    total_of_list += int(number_list[i])
    average_list = total_of_list / how_many_inputs
print('The average is ' + str(average_list))
