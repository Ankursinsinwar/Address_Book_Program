from Address_Book import address_book
from Contact import contact

book = address_book()

c1 = contact(
    "Ankur",
    "Sinsinwar",
    "Township",
    "Mathura",
    "Uttar Pradesh",
    "281006",
    "9045735010",
    "ayu@gmail.com"
)

book.add_contact(c1)
book.display_contacts()