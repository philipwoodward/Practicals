"""Create a text file called   numbers.txt (Ctrl-N and choose File) Put 17 and 42 on separate lines and save.
Open this file, read the numbers and then adds them together.
Extend this to read any number of numbers."""
temp_file = open("numbers.txt","r")
total=0
for line_str in temp_file:
    total += int(line_str)
print (total)
temp_file.close()