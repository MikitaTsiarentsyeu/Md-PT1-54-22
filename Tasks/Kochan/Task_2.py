class People:
    dict_processed = {}

    def add_singl(self):
        ph_numb = self.validate(input('Please enter the phone number: \n'))
        if ph_numb:
            name = input('Please enter the name: \n').replace(' ', '').capitalize()
            surname = input('Please enter the surname: \n').replace(' ', '').capitalize()
            city = input('Please enter the city: \n').replace(' ', '').capitalize()
            state = input('Please enter the state: \n').replace(' ', '').capitalize()
            self.dict_processed[ph_numb] = [(name, surname), (city, state)]
            return self.dict_processed
        else:
            self.add_singl()

    def add_dict(self, new_dict):
        self.dict_processed = self.dict_processed | new_dict
        return self.dict_processed

    @staticmethod
    def validate(value):
        if value.isdigit() and len(value) == 10:
            return int(value)
        else:
            print('The entered number was wrong')

    def find_pers(self):
        numb = People.validate(input('Please enter the phone number whose host you want to find: \n'))
        if numb in self.dict_processed.keys():
            name_city = self.dict_processed[numb]
            print(f'{name_city[0][0]} {name_city[0][1]} from {name_city[1][0]}, {name_city[1][1]}')
        else:
            print('the number was not found')


dict_raw = {9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
            4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
            9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
            6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
            7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

sprav1 = People()
sprav1.add_dict(dict_raw)
sprav1.find_pers()
