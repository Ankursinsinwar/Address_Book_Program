from Address_Book import address_book
from Contact import contact
from utils import edit_contact, create_contact

def main():
    print("\n--- Wellcome to Address Book ---\n")
    book = None

    while True:
        print("1. Add/Initialize Address Book")
        print("2. Create and Add Contact")
        print("3. Display Contacts")
        print("4. Edit Contact")
        print("0. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            book = address_book()
            print("\nAddress Book initialized.\n")

        elif choice == '2':
            if book is None:
                print("\nError: Please initialize the Address Book first (Option 1).\n")
                continue

            create_contact(book)
            print("\nContact added successfully!\n")

        elif choice == '3':
            if book:
                book.display_contacts()
            else:
                print("\nAddress book is empty or not initialized.\n")

        elif choice == '4':
            if book:
                name = input("Enter the first name of the contact to edit: ")
                edit_contact(book, name)
            else:
                print("\nAddress book is empty or not initialized.\n")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
