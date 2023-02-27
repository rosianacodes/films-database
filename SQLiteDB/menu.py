import readFilms
import addFilms
import updateFilms
import deleteFilms
import searchFilms

# create function
def menuOptions():
    options = 0 # flag variable
    # while 0 not in this list ["1","2","3","4","5","6"] execute the code below
    while options not in ["1","2","3","4","5","6"]:
        print("Films Menu Options\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Search.\n6. To Exit.")

        # re-assign the value of the options variable
        # the default data type for input is string
        options = input("Enter an option from the menu choices above: ")
        if options not in ["1","2","3","4","5","6"]:
            print(f"{options} is not a valid choice")
    return options

mainProgram = True # assign mainProgram the value of True which is Boolean data type
while mainProgram:
    mainMenu = menuOptions()
    if mainMenu == "1":
        readFilms.read() # call/ivoke read() subroutine from readFilms python file
    elif mainMenu == "2":
        addFilms.inserttblFilms()
    elif mainMenu == "3":
        updateFilms.update()
    elif mainMenu == "4":
        deleteFilms.delete()
    elif mainMenu == "5":
        searchFilms
    else:
        mainProgram = False #re-assign mainProgram the value of the False to exit he menu
    # Your else must re-assign the value of the mainProgram to False to exit the loop and must be the last option (6)
input("Press enter to Quit the application") #Quit the the application not to quit the menu