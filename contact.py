contacts = {}

def search_contact (name , number):
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print(f"contact {name} not found. ")
    
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"contact {name} deleted. ")
    else:
        print(f"contact {name} not found. ")

def add_contact (name , number):
    contacts [name] = number
    print(f"contact {name} added. ")
    
    
while True:
    print("1. add contact")
    print("2. search contact")
    print("3. delete contact")
    print("4. Exite")
    
    choice = input("Enter your choice : ")
    
    if choice == '1':
        name = input("Enter name : ")
        number = input("Enter number : ")
        add_contact(name , number)
        
    elif choice == '2':
        name == input("Enter name : ")
        search_contact(name , number)
        
    elif choice == '3':
        name = input("Enter name : ")
        delete_contact(name)
        
    elif choice == '4':
        break
    
    else:
        print("invalid choice")
        

