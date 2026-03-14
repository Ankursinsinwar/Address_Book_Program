from Address_Book import address_book

class Address_Book_Manager:

    def __init__(self):
        self.__Address_book={}

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