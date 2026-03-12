from Contact import contact

class address_book:

    def __init__(self):
        self.contact=[]
        print("Address book created")

    def add_contact(self,contact):
        self.contact.append(contact)

    def display_contacts(self):
        for contact in self.contact:
            contact.display()
