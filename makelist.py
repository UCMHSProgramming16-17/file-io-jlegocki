#open a a new file
file = open("listfile.txt", "w")

#create a list of ten items from user input 
for userinput in range(10):
    file.write(str(userinput + 1) + ". " + input("What would you like to add to the list? ") + '\n') 

#close the file
file.close()