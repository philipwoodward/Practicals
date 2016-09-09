"""
CP1404/CP5632 Practical
Colours/codes in a dictionary

"""


COLOUR_HEX = {"antiquewhite": "#faebd7", "black": "#000000", "brown": "#a52a2a", "green1": "#00ff00",
               "honeydew1": "#f0fff0", "indianred": "  #cd5c5c", "khaki": "#f0e68c", "lavender": "#e6e6fa", "lawngreen": "#7cfc00", "navyblue": "#000080"}

colour = input("Enter the name of the colour: ").lower()
while colour != "":
    if colour in COLOUR_HEX:
        print(colour, "is", COLOUR_HEX[colour])
    else:
        print("Sorry, your colour is not in this dictionary")
    colour = input("Enter the name of the colour: ").lower()

for colour in COLOUR_HEX:
    print("{:4} is {}".format(colour, COLOUR_HEX[colour]))
