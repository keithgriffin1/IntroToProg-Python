# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Keith Griffin>,<11/17/20>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
filename = "ToDoList.txt"   # An object that represents a file
objFile = None
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# If the file ToDoList.txt hasn't been created a try statement catches the FileNotFound Error
try:
    objFile = open(filename, 'r')
    for row in objFile:
        lstTable = row.split(",")
        print(f"{lstTable[0]}\n")
    objFile.close()
except FileNotFoundError:
    print("You need to add some data.")
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove the last item entered.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for key, value in dicRow.items():
            print(f"Priority:{key} Task:{value}")
            continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Please enter a task. ")
        priority = input("Please enter the priority of your task. ")

        dicRow[priority] = task
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        response = input("Select item you would like to delete based on priority ")
        dicRow.pop(response)
        print(dicRow)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        with open(filename, 'a') as f:
            for key, value in dicRow.items():
                f.write(f"Priority: {key} Task: {value}\n")
        f.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("I hope you complete all your tasks!")
        break  # and Exit the program