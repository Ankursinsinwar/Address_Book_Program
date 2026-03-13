from Address_Book import address_book

class Address_Book_Manager:

    def __init__(self):
        self.__Adress_books={}

    def add_Adress_book(self,name):
        if name not in self.__Adress_books:
            self.__Adress_books[name] = address_book()
        return self.__Adress_books[name]


    def display_Adress_books(self):
        print("\n--------- Adress_books --------------\n")
        for name, Adress_book in self.__Adress_books.items():
            print("Adderss book name : ", name)
            Adress_book.display_contacts()
        print("\n----------------------\n")


    def search_Person(self, city_state):
        for name, book in self.__Adress_books.items():
            for person in book.contact:
                if person.city == city_state:
                    print("Address book : ",name,', city : ',person.city,' name : ',person.first_name)
                if person.state == city_state:
                    print("Address book : ",name,', state : ',person.state,' name : ',person.first_name)