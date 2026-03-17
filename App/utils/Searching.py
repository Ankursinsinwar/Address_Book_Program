
class Searching:

    def search_Person(self, city_state):
        '''
        - Search all the contacts in a `city or state` accross all address books
        
        '''
        for name, book in self.Address_book.items():
            for person in book.contact:
                if person.city == city_state:
                    print("Address book : ",name,', city : ',person.city,' name : ',person.first_name)
                if person.state == city_state:
                    print("Address book : ",name,', state : ',person.state,' name : ',person.first_name)

        
    def view_Person(self,city, state):
        '''
        - View all contacts by `city and state` accross all address books
        
        '''
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
        '''
        - Count all the contacts in a `city or state` accross all address books
        
        '''
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


    