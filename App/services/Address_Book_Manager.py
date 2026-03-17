import json

from App.models.Address_Book import address_book
from App.models.Contact import contact
from App.utils.Searching import Searching
from App.utils.file_handler import file_handler

class Address_Book_Manager(file_handler, Searching):
    '''
    - Address Book manager
     - `Address book` {}
    '''
    def __init__(self):
        self.__Address_book=dict()

    @property
    def Address_book(self):
        return self.__Address_book

    def add_Address_book(self,name) -> address_book:
        '''
        - Create and add Address book in the Address book manager
        
        '''
        if name not in self.Address_book:
            self.Address_book[name] = address_book()
        return self.Address_book[name]


    def display_Address_books(self) -> None:
        '''
        - Display contacts Of all Address books  
        
        '''
        print("\n--------- Address_books --------------\n")
        for name, Address_book in self.Address_book.items():
            print("Adderss book name : ", name)
            Address_book.display_contacts()
        print("\n----------------------\n")


    