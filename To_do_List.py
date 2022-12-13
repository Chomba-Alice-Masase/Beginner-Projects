#Simple to do list project
#it will be a console based project and will not use gui.
#I intend to utilize lists and loops[]
Tasks = [] # This is where we will store our tasks
Accessing_to_do_list = True # this boolean will be used to keep the program running
while(Accessing_to_do_list):
    #Input should be a string
    Greeting_Prompt = input("What would you like to do?: 1.View Tasks, 2. Edit Tasks, 3.Quit: ")
    if Greeting_Prompt == "View Tasks":
        print(Tasks)
    elif Greeting_Prompt == "Edit Tasks":
        #Input should be a string
        Edit_Prompt = input("What would you like to do with your to do list?: 1. Add Item, 2. Remove item: ") #First bug
        if Edit_Prompt == "Add Item":
            Adding_Task = input("What would you like to add?: ")
            Tasks.append(Adding_Task)
        elif Edit_Prompt == "Remove Item":
            Removing_Task = input("Which task would you like to remove?: ")
            Tasks.remove(Removing_Task)
        else:
            print("Invalid Entry")
    elif Greeting_Prompt == "Quit":
        Accessing_to_do_list = False
    else:
        print("Invalid Entry.")

print("Persistence is key")




