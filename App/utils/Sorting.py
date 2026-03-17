
class Sorting:

    def sort_alphabetically(self):
        '''
        - Sort contacts by `first_name` in a address book
        
        '''
        self.contact.sort(key = lambda person: person.first_name)

    
    def sort_city_state_zip(self,sort):
        '''
        - Sort contacts by `city | state | zip` in a address book
        
        '''
        match sort:
            case 'a':
                self.contact.sort(key=lambda person: person.city)
            case 'b':
                self.contact.sort(key=lambda person: person.state)
            case 'c':
                self.contact.sort(key=lambda person: person.zip)