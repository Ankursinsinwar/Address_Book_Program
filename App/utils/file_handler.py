import json
from App.models.Contact import contact


class file_handler:
    def save_to_file(self, filename):
        '''
        - Save Address books with contacts to a file
        
        '''
        file_type = input(" Save to file [1] | to CSV [2] : ")
        if(file_type=='1'):
            type=' | '
            extention=".txt"
        elif(file_type=='2'):
            type=","
            extention=".csv"
        else:
            print("Enter valid option!")
            return

        with open(f"Data\\{filename}{extention}", "w") as file:
            for name,book in self.Address_book.items():
                for contact in book.contact:
                    data = f"{name}{type}{contact.first_name}{type}{contact.last_name}{type}{contact.address}{type}{contact.city}{type}{contact.state}{type}{contact.zip}{type}{contact.phone_number}{type}{contact.email}\n"
                    file.write(data)

        print("Contacts saved to file successfully!")


    def load_from_file(self, filename):
        '''
        - Load Address books with contacts from a file
        
        '''
        file_type = input(" Load from file [1] | to CSV [2] : ")
        if(file_type=='1'):
            type=' | '
            extention=".txt"
        elif(file_type=='2'):
            type=","
            extention=".csv"
        else:
            print("Enter valid option!")
            return
        try:
            with open(f"Data\\{filename}{extention}", "r") as file:
                for line in file:
                    data = line.strip().split(type)

                    if len(data) == 9:
                        self.add_Address_book(data[0])
                        book = self.Address_book[data[0]]
                        new_contact = contact(
                            data[1], data[2],
                            data[3], data[4], data[5],
                            data[6], data[7],  data[8]
                        )
                        book.add_contact(new_contact)
                file.seek(0)
                print("Adderss book : ",filename)
                print(file.read())

            print("Contacts loaded from file successfully!")

        except FileNotFoundError:
            print("File not found!")

    
    def save_to_json(self):
        '''
        - Save Address books with contacts to JSON
        
        '''
        books = {}
        for name, book in self.Address_book.items():
            contacts = []
            for person in book.contact:
                data = {
                "first_name": person.first_name,
                "last_name": person.last_name,
                "address": person.address,
                "city": person.city,
                "state": person.state,
                "zip": person.zip,
                "phone_number": person.phone_number,
                "email": person.email
                }
                contacts.append(data)
            books[name] = books.get(name,[]) + contacts
        json.dump(books, open("Data\\address_book.json",'w'), indent=4)
    
    
    def load_from_json(self):
        '''
        - Load Address books with contacts from JSON
        
        '''
        try:
            books = json.load(open("Data\\address_book.json",'r'))
            for name, value in books.items():
                if self.Address_book.get(name,None) is None:
                    self.add_Address_book(name)
                book = self.Address_book[name]
                for person in value:
                    new_contact = contact(
                        person["first_name"],
                        person["last_name"],
                        person["address"],
                        person["city"],
                        person["state"],
                        person["zip"],
                        person["phone_number"],
                        person["email"]
                    )
                    book.add_contact(new_contact)

            print("Contacts loaded from JSON successfully!")

        except FileNotFoundError:
            print("File not found!")

