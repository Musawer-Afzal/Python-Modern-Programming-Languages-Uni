import os
# os.system("color")

# COLOR = {
#     "HEADER": "\033[95m",

# }
while True:
    print("************************* PHONE BOOK MENU *******************")
    
    print("Welcome to Phonebook Application")
    print("1. Add new contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("\n***********************************************************************************************")

    choice = int(input("Select Option: "))
    if choice == 1:
        file = open("data.txt", "a")
        name = input("Enter contact name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        rec = name + "," + email + "," + phone
        print(f"Info Saved: {rec}")
        file.write(rec + "\n")
        file.close()
    elif choice == 2:
        found = False
        search = input("Enter Contact Name: ").lower()
        file = open("data.txt")
        info = file.readlines()
        for rec in info:
            temp = rec.split(",")
            name = temp[0]
            if name.lower() == search:
                print("Contact Found.....")
                print("--------------------")
                print(f"Name: {name}")
                print(f"Email: {temp[1]}")
                print(f"Phone Number: {temp[2]}")
                found = True
        file.close()
        if found == False:
            print("Sorry, no record found...")
    elif choice == 3:
        found = False
        search = input("Enter Contact Name: ").lower()
        
        # Read all contacts into a list
        with open("data.txt", "r") as file:
            info = file.readlines()

        updated_info = []  # store updated contacts here

        for rec in info:
            temp = rec.strip().split(",")
            name = temp[0]
            
            if name.lower() == search:
                print("Contact Found.....")
                print("--------------------")
                name = input("Enter New Name: ")
                email = input("Enter New Email: ")
                phone = input("Enter New Phone Number: ")
                rec = name + "," + email + "," + phone
                print(f"Info Updated to: {rec}")
                updated_info.append(rec + "\n")  # add updated record
                found = True
            else:
                updated_info.append(rec.strip() + "\n")  # keep old record as is

        # Write everything back to the file
        with open("data.txt", "w") as file:
            file.writelines(updated_info)

        if not found:
            print("Sorry, no record found...")
    elif choice == 4:
        found = False
        search = input("Enter Contact Name: ").lower()
        file = open("data.txt", "r")
        info = file.readlines()
        for rec in info:
            temp = rec.split(",")
            name = temp[0]
            if name.lower() == search:
                print("Contact Found.....")
                print("--------------------")
                print(f"Name: {name}")
                print(f"Email: {temp[1]}")
                print(f"Phone Number: {temp[2]}")
                found = True
            else:
                pass
        file.close()
        if found == False:
            print("Sorry, no record found...")
    elif choice == 5:
        print("Thank you for using this Application")
        break
    else:
        print("Wrong Option Selected")
    input("Press ENTER to continue")
    # os.system("cls")