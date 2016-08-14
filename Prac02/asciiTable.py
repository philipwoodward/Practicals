
print ("{:12}{:15}".format("ASCII","Characters"))
for i in range(10, 120, 11):
    print("{:5} {:>15}".format(i, chr(i)))
