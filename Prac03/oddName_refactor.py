"""Philip Woodward
Ask user their name, ensure not blank.
Print every second letter"""
def main():
    every_nth_letter = 1
    every_nth_letter = input ("Please select every nth number to print from your name. ")
    name = get_name()
    name_length = len(name)
    print(name)
    for i in range(0,name_length,int(every_nth_letter)):
        print (name[i], end=' ')


def get_name():
    user_name = ""
    while user_name == "":
        user_name = input("My name is > ")
    return user_name

main()