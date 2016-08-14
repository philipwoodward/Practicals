"""Input user name. Open file called name.txt and write to it"""
user_name = input("My user name is > ")
temp_file = open("name.txt","w")
print (user_name, file=temp_file)
temp_file.close()