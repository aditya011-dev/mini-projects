contacts = {}
def add_contact():
    name = input ("Enter name:")
    number = input ("Enter phone:")

    if name in contacts:
        print ("Contact already exists")
        return
    
    contacts[name]= number
    print ("Contact added successfully")

def search_contact():
    name = input("Enter name to search:")
    if name in contacts:
        print (f"Name: {name}")
        print (f"Phone: {contacts[name]}")
    else:
        print ("Contact not found")
         
def delete_contact():
    name = input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print ("Contact deleted successfully")
    else:
        print ("Contact not found")