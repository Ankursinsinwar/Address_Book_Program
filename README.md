# Address Book Management System

## Introduction

The Address Book Management System is a Python application used to store and manage person's contact details.
It allows users to add, edit, delete, search, and sort contacts in an address book.

The system also stores data in `.txt | .csv | JSON format` so contacts can be saved and loaded later.

---

## Features

* Add a new address book
* Add a new person contact details to the address book
* Edit contact details
* Delete a contact
* Add multiple contacts
* Avoid duplicate contacts
* Search contacts by city or state
* Sort contacts by name, city, state, or zip
* Sort contacts by name
* Sort contacts by city or state or zip
* Save address books to txt | csv | JSON files
* Load address books from txt | csv | JSON files

---

## Project Files

```
address_book_Program/
│
├── app/                        # Core application package
│   ├── __init__.py
│   │
│   ├── models/                # Data models
│   │   ├── __init__.py
│   │   ├── contact.py
│   │   └── address_book.py
│   │
│   ├── services/              # Business logic
│   │   ├── __init__.py
│   │   └── address_book_manager.py
│   │
│   └──  utils/                 # Utility/helper functions
│       ├── __init__.py
│       ├── file_handler.py
│       ├── Searching.py
│       └── Sorting.py
│
│
├── data/                      # Data storage
│   ├── address_book.json
│   ├── address_book.csv
│   └── address_book.txt
│
├── main.py                    # Entry point (CLI)
├── .gitignore
└── README.md
```

---

## How to Run

Run the main program:

```
python main.py
```

Follow the menu instructions to manage contacts.

---

## Technologies Used

* Python
* JSON (for storing data)
* CSV (for storing data)
* TEXT (for storing data)

---

## Design Principles

* **Modularity** – Code is divided into multiple files.
* **Single Responsibility** – Each class has a specific task.
* **Reusability** – Classes can be reused or extended.

---

## Conclusion

This project demonstrates basic **Object-Oriented Programming concepts**, file handling, and data management using Python.