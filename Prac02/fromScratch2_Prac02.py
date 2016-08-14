"""Open name.txt, raeds the name and prints Your name is xxx"""
temp_file = open("name.txt","r")
for line_str in temp_file:
    print(line_str,end='')