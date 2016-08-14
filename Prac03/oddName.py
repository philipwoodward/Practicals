"""Philip Woodward
Ask user their name, ensure not blank.
Print every second letter"""
user_name = ""
while user_name == "":
    user_name = input("My name is > ")
    name_length = len(user_name)
for i in range(0,name_length,2):
    print (user_name[i], end=' ')
