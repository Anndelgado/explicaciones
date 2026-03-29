import os

FILE_NAME = "database.txt"


# Create and Append
def add_blocker():
    blocker = input("Enter your daily blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print("Blocker saved successfully!\n")


# Read (Fecth)
def fetch_blockers():
    if not os.path.exists(FILE_NAME):
        print("Error: File does not exist.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

        if not lines:
            print("No blockers found.\n")
        else:
            print("\n___ Team Daily Blockers ___")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
            print()


# Overwrite (with warning)
def overwrite_file():
    if os.path.exists(FILE_NAME):
        confirm = input("Warning: This will overwrite all data. Continue? (yes/no): ")
        
        if confirm.lower() != "yes":
            print("Operation cancelled.\n")
            return

    new_data = input("Enter new content: ")

    with open(FILE_NAME, "w") as file:
        file.write(new_data + "\n")

    print("File overwritten successfully.\n")


# Menu
def menu():
    while True:
        print("____ Team Daily Status System ____")
        print(" 1. Add Blocker,\n 2. Fetch Blockers,\n 3. Overwrite File,\n 4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_file()
        elif option == "4":
            print("Exiting of the program...")
            break
        else:
            print("Invalid option. Try again.\n")


# Run program
menu()


"""
Step 5: English practice

Protocol selection:
I will reach out to the team via Slack because the issue is an immediate blocker.
I will also send an email if the issue requires formal documentation and tracking.
If the error is related to a task, I would report it in Jira to keep it properly documented.


Vocabulary integration:
This script demonstrates persistence by storing data in a text file. 
It allows users to fetch stored blockers and review them easily. 
The overwrite function includes a warning to prevent accidental data loss. 
If any issue occurs, I would reach out to the team to resolve it quickly.
"""