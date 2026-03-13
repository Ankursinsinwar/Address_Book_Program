from Address_Book import address_book

class Address_Book_Manager:

    def __init__(self):
        self.__Adress_books={}

    def add_Adress_book(self,name):
        self.__Adress_books[name] = address_book()
        return self.__Adress_books[name]


    def display_Adress_books(self):
        print("\n--------- Adress_books --------------\n")
        for name, Adress_book in self.__Adress_books.items():
            print("Adderss book name : ", name)
            Adress_book.display_contacts()
        print("\n----------------------\n")

