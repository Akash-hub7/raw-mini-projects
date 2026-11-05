contacts = []

while True:
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Search contacts")
    print("4. Delete contacts")
    print("5. EXIT")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter your name:")
        number = input("Enter number:")

        contact = {"name": name, "number": number}
        contacts.append(contact)

        print("Contact Saved!!!")

    elif choice == 2:
        if len(contacts) ==0:
            print("NO CONTACTS YET!!!")
        else:
            for i in range(len(contacts)):
                print(i + 1, contacts [i]["name"], contacts[i]["number"])

    elif choice == 3:
        search_name = input("Enter name to search:")
        found = False

        for c in contacts:
            if c["name"].lower() == search_name.lower():
                print(c["name"],"_",c ["number"])
                found = True

        if not found:
            print("Contact NoT Found!!")

    elif choice == 4:
        num= int(input("Enter contact number"))

        if num > 0 and num <= len(contacts):
            removed = contacts.pop(num-1)
            print("Delete", removed["name"])
        else:
            print("Invalid section!!")
 
    elif choice == 5:
        print("Exiting the program...")
        break 
    else:
        print("Invalid choice. Please try again.")


