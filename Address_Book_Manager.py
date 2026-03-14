from Address_Book import address_book
from Contact import contact
import json

class Address_Book_Manager:

    def __init__(self):
        self.__Address_book=dict()

    @property
    def Address_book(self):
        return self.__Address_book

    def add_Address_book(self,name):
        if name not in self.Address_book:
            self.Address_book[name] = address_book()
        return self.Address_book[name]


    def display_Address_books(self):
        print("\n--------- Address_books --------------\n")
        for name, Address_book in self.Address_book.items():
            print("Adderss book name : ", name)
            Address_book.display_contacts()
        print("\n----------------------\n")


    def search_Person(self, city_state):
        for name, book in self.Address_book.items():
            for person in book.contact:
                if person.city == city_state:
                    print("Address book : ",name,', city : ',person.city,' name : ',person.first_name)
                if person.state == city_state:
                    print("Address book : ",name,', state : ',person.state,' name : ',person.first_name)

        
    def view_Person(self,city, state):
        result = {}
        for name, book in self.Address_book.items():
            city_dict = {}
            state_dict = {}
            for person in book.contact:
                if person.city == city:
                    city_dict[person.city]=city_dict.get(person.city, []) + [person.first_name]
                if person.state == state:
                    state_dict[person.state]=state_dict.get(person.state, []) + [person.first_name]
        if len(city_dict)!=0 :
            result[name] = result.get(name,[]) + [city_dict]
        if len(state_dict)!=0:
            result[name] = result.get(name,[]) + [state_dict]
        return result
    

    def count_Person(self,city_state):
        city_count=0
        state_count=0
        for _, book in self.Address_book.items():
            for person in book.contact:
                if(person.city==city_state):
                    city_count+=1
                if(person.state==city_state):
                    state_count+=1
        print("Number of contacts in city",city_state,":",city_count)
        print("Number of contacts in state",city_state,":",state_count)


    def save_to_file(self, filename):
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

