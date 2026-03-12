from Address_Book import address_book
from Contact import contact

book = address_book()

first_name=input("\nEnter your first name: ")
last_name=input("Enter your Last name: ")
address=input("Enter your address: ")
city=input("Enter your city: ")
state=input("Enter your state: ")
zip=input("Enter your zip code: ")
phone_number=input("Enter your phone number: ")
email=input("Enter your email: ")

Contact = contact(first_name, last_name, address, city, state, zip, phone_number, email)

book.add_contact(Contact)
book.display_contacts()