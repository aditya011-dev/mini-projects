contacts = {}
def add_contact():
    name = input ("Enter name:")
    number = input ("Enter phone:")

    if name in contacts:
        print ("Contact already exists")
        return
    
    contacts[name]= number
    print ("Contact added successfully")

add_contact()
add_contact()
print (contacts)    #checking if the contact is added or not
