from App.services.Address_Book_Manager import Address_Book_Manager

def main():
    print("\n--- Wellcome to Address Book ---\n")
    books = Address_Book_Manager()
    book = None
    filename = "address_book"
    while True:
        print("1. Add/Initialize Address Book")
        print("2. Create and Add Contact")
        print("3. Display Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Display Contacts in all Address Books")
        print("7. Display multiple person in the city or state in all Address Books")
        print("8. Display all person in the city and state in all Address Books")
        print("9. Display number of person in the city and state in all Address Books")
        print("10. Sort person details by name")
        print("11. sort the person contact details on the basis of city, state, zip")
        print("12. Save Contacts to File")
        print("13. Load Contacts from File")
        print("14. Save Contacts to JSON")
        print("15. Load Contacts from JSON")
        print("0. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            bok_name = input("Enter address book name: ")
            book = books.add_Address_book(bok_name)
            print("\nAddress Book initialized.\n")

        elif choice == '2':
            if book is None:
                print("\nError: Please initialize the Address Book first (Option 1).\n")
                continue

            book.create_contact()

        elif choice == '3':
            if book:
                book.display_contacts()
            else:
                print("\nAddress book is empty or not initialized.\n")

        elif choice == '4':
            if book:
                name = input("Enter the first name of the contact to edit: ")
                book.edit_contact(name)
                books.save_to_file(filename)
            else:
                print("\nAddress book is empty or not initialized.\n")
            
        elif choice == '5':
            if book:
                name = input("Enter the first name of the contact to delete: ")
                book.delete(name)
                books.save_to_file(filename)
            else:
                print("\nAddress book is empty or not initialized.\n")

        elif choice == '6':
            books.display_Address_books()

        elif choice == '7':
            city_state = input("Enter City or state: ")
            books.search_Person(city_state)

        elif choice == '8':
            city_name = input("Enter City : ")
            State_name = input("Enter State : ")
            view = books.view_Person(city_name,State_name)
            print(view)

        elif choice == '9':
            city_state = input("Enter City or state: ")
            books.count_Person(city_state)
        
        
        elif choice == '10':
            if book is None:
                print("\nError: Please initialize the Address Book first (Option 1).\n")
                continue
            book.sort_alphabetically()
            book.display_contacts()


        elif choice == '11':
            if book is None:
                print("\nError: Please initialize the Address Book first (Option 1).\n")
                continue
            print("----------sort AddressBook on the basis of city, state, zip--------------")
            print("a. sort on the basis of city")
            print("b. sort on the basis of state")
            print("c. sort on the basis of zip")
            sort=input("Enter your choice: ")
            book.sort_city_state_zip(sort.lower())
            book.display_contacts()


        elif choice == '12':
                books.save_to_file(filename)

        elif choice == '13':
                books.load_from_file(filename)

                
        elif choice == '14':
            books.save_to_json()

        elif choice == '15':
            books.load_from_json()



        elif choice == '0':
            break

        else:
            print("\nInvalid choice. Please try again.\n")



if __name__ == "__main__":
    main()
