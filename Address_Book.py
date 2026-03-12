from Contact import contact

class address_book:

    def __init__(self):
        self.contact=[]

    def add_contact(self,contact):
        self.contact.append(contact)

    def display_contacts(self):
        print("\n--------- Contacts --------------\n")
        for contact in self.contact:
            contact.display()
