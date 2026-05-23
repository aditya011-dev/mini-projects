contacts = {}

def add_contact():
    name   = input("Enter name: ")
    number = input("Enter phone: ")
    if name in contacts:
        print(f"{name} already exists! ❌")
        return
    contacts[name] = number
    print(f"{name} added successfully! ✅")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name:   {name}")
        print(f"Number: {contacts[name]}")
    else:
        print(f"{name} not found ❌")

def delete_contact():
    name = input("Enter name to delete: ")
    if name not in contacts:
        print(f"{name} not found ❌")
        return
    del contacts[name]
    print(f"{name} deleted successfully! ✅")

def view_all():
    if len(contacts) == 0:
        print("No contacts yet! ❌")
        return
    print("\n📱 All Contacts:")
    print("─" * 25)
    for name, number in contacts.items():
        print(f"{name} → {number}")
    print("─" * 25)
    print(f"Total contacts: {len(contacts)}")

def main():
    while True:
        print("\n📱 Contact Book")
        print("─" * 25)
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contacts")
        print("5. Exit")
        print("─" * 25)
        choice = input("Choose option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option! Pick 1-5 ❌")

main()