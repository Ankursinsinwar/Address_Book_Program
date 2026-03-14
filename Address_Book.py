from Contact import contact

class address_book:

    def __init__(self):
        self.__contact=list()

    @property
    def contact(self):
        return self.__contact

    def add_contact(self,contact):
        for cont in self.contact:
            if cont.first_name == contact.first_name and cont.last_name == contact.last_name:
                print("\nContact already exists !\n")
                return
        self.contact.append(contact)
        print("\nContact added successfully!\n")

    def display_contacts(self):
        print("\n--------- Contacts --------------\n")
        for contact in self.contact:
            contact.display()
            print("-----------")

    
    def create_contact(self):
        first_name=input("\nEnter your first name: ")
        last_name=input("Enter your Last name: ")
        address=input("Enter your address: ")
        city=input("Enter your city: ")
        state=input("Enter your state: ")
        zip=input("Enter your zip code: ")
        phone_number=input("Enter your phone number: ")
        email=input("Enter your email: ")

        Contact = contact(first_name, last_name, address, city, state, zip, phone_number, email)
        self.add_contact(Contact)



    def edit_contact(self, name):
        for contact in self.contact:

            if contact.first_name == name:
                edit=True
                while(edit):
                    print("1. Edit First Name")
                    print("2. Edit Last Name")
                    print("3. Edit address")
                    print("4. Edit city")
                    print("5. Edit state")
                    print("6. Edit zip")
                    print("7. Edit phone_Number")
                    print("8. Edit Email")
                    print("0. quit")

                    choice = int(input( "Enter your choice: "))

                    match choice:

                        case 1:
                            first_name = input("Enter new first name: ")
                            contact.first_name = first_name

                        case 2:
                            last_name = input("Enter new last name: ")
                            contact.last_name = last_name
                        case 3:
                            address=input("Enter your address: ")
                            contact.address=address
                        case 4:
                            city=input("Enter your city: ")
                            contact.city=city
                        case 5:
                            state=input("Enter your new State: ")
                            contact.state=state
                        case 6:
                            zip=input("Enter your new zip code: ")
                            contact.zip=zip
                        case 7:
                            phone_number=input("Enter your phone no.:")
                            contact.phone_number=phone_number
                        case 8:
                            email=input("Enter your email :")
                            contact.email=email
                        case 0:
                            edit=False
            else:
                print("User not found!")
 
 

    def delete(self,name):
        found=False
        for contact in self.contact:
            if contact.first_name==name:
                self.contact.remove(contact)
                found=True
                break   
        if(found==True):
            print("User deleted")
        else:
            print("user not found")


    def sort_alphabetically(self):
        self.contact.sort(key = lambda person: person.first_name)

    
    def sort_city_state_zip(self,sort):
        match sort:
            case 'a':
                self.contact.sort(key=lambda person: person.city)
            case 'b':
                self.contact.sort(key=lambda person: person.state)
            case 'c':
                self.contact.sort(key=lambda person: person.zip)

