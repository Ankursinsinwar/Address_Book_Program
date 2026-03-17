class contact:
    '''
        - Contact Class
          - `first_name`
          - `last_name`
          - `address`
          - `city`
          - `state`
          - `zip`
          - `email`
          - `phone_number`
        
        '''
    def __init__(self, first_name, last_name, address, city,state, zip, phone_number, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__email = email
        self.__phone_number = phone_number


    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value



    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value



    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value



    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value



    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value



    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value



    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value



    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value


        
    def display(self):
        '''
        - Display person contact details
        
        '''
        print("Name\t: ", self.first_name, self.last_name)
        print("Address\t: ", self.address)   
        print("City\t:", self.city)
        print("State\t:", self.state)
        print("Zip\t:", self.zip)
        print("Phone\t:", self.phone_number)
        print("Email\t:", self.email, '\n')

    