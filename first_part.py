# seperate each house according to sale or rent 
import csv
import HandleFile

class Address :
    addr = HandleFile.HandleFile('Adress.csv')
    counter = 0
    def __init__ (self, city_name, street_name, plaque, postal_code):
        self.city_name = city_name
        self.street_name = street_name
        self.plaque = plaque
        self.postal_code = postal_code

    def edite_address(self, **kwargs):
        all_keys = self.__dict__.keys() - {"postal_code"}
        if all(x in all_keys for x in kwargs.keys()):
            self.__dict__.update((k, v) for k, v in kwargs.items())
            return self
        else:
            raise Exception ("there is an error")


    def save_address (self):
        Address.addr.append_info_user(self.__dict__)


    def __str__ (self):
        return f'{self.city_name}-{self.street_name} _ plaque= {self.plaque} _ postalcode= {self.postal_code}'


class Person :
    file_name = HandleFile.HandleFile('person.csv')
    counter = 0
    def __init__(self, name, last_name, email_addr, id, telephon):
        self.fname = name
        self.last_name = last_name
        self.email = self.validation_address_email(email_addr)
        self.id =self.validation_id(id) 
        self.telephon = str(telephon)
        
        
        
    def validation_address_email (self, email):
        try :
            sample = '@'
            if not str(email).endswith('.com') :
                raise Exception('Email must end with .com')
            elif sample not in email:
                raise Exception('Email must include @ ')  
            else:
                return email
        except Exception as e :
            print(e)

    def validation_id (self, id):
        try:
            if len(str(id)) == 10 and str(id).isdigit() :
               return id
            else:
                raise Exception ('This Id is not valid.')
        except Exception as e :
            print(e)
       

    def edite_info (self, id):
        
        with open('person.csv', 'r') as f :
            r = csv.DictReader(f)
            lst = list(r)
        end = ''
        while end != 'n': #todo
            for dic in lst:
                if str(id) in dic['id']:
                    self.counter += 1
                    print(dic)
                    change= input('part that you want to change: ').lower()
                    dic[change] = input(f"{change}: ")  
                    end = input('change mor? (y/n) ').lower()

            self.file_name.write_info_user(lst)
            if self.counter == 0 :
                print('This id is not found')
                break 



    def save_info(self):
        self.file_name.append_info_user(self.__dict__)


    def __str__(self) -> str:
        return f"{self.fname} {self.last_name}"


class House  :
    file = HandleFile.HandleFile('house.csv')
    counter = 0
    def __init__(self, owner, renter, address, rooms, house_area,
                number_of_floor,mortgage_amount, rent_amount,
                sale_amount, yard_area=30, tel= 'active', on_sale = False,on_rent= True):
        self.owner = owner
        self.renter = renter
        self.address= address
        self.rooms = rooms
        self.house_area = float(house_area)
        self.yard_area = float(yard_area)
        self.num_of_floor = number_of_floor
        self.mortgage= mortgage_amount
        self.rent = rent_amount
        self.sale = sale_amount
        self.tel = tel
        self.on_sale = on_sale
        self.on_rent = on_rent


    def edite_house_info(self, address):
        if isinstance(address, Address):
            with open('house.csv', 'r') as f :
                r = csv.DictReader(f)
                lst_flat = list(r)
            end = ''
            while end != 'n' :
                for d in lst_flat :
                    if str(address) in d['address']:
                        self.counter += 1
                        print(d) 
                        n = input('which part: ').lower()
                        d[n] = input(f'{n}: ')
                        end = input('change mor? (y/n) ').lower()
                self.file.write_info_user(lst_flat)
                if self.counter == 0 :
                    print('This address is not found!')
                    break
        else:
            print('This address is not valid!')

      
    def save_info(self):
        self.file.append_info_user(self.__dict__)


    def __str__(self):
        return f'rooms = {self.rooms}\nHouse_area = {self.house_area}\nyard area =  {self.yard_area}\nnumber of floor = {self.num_of_floor}\nmortgage_amount = {self.mortgage}\nrent_amount = {self.rent}\nsale_price = {self.sale}\non_sale= {self.on_sale}'


class Flat (House) : 
    file_name = HandleFile.HandleFile('apartment.csv')
    counter = 0
    def __init__(self, owner, renter, address, rooms, house_area,
                number_of_floor,mortgage_amount, rent_amount,
                sale_amount, yard_area, parking, on_which_floor='first', tel= 'active', on_sale= False, on_rent = True) :

        super().__init__(owner, renter, address, rooms, house_area,
                        number_of_floor,mortgage_amount, rent_amount,
                        sale_amount, yard_area, tel, on_sale, on_rent)

        self.parking  = parking
        self.floor = on_which_floor
    

    def save_info (self):
        self.file_name.append_info_user(self.__dict__)
        

    def edite_flat_info(self, address):
        if isinstance (address, Address) :
            with open('apartment.csv', 'r') as f :
                r = csv.DictReader(f)
                lst_flat = list(r)
            end = ''
            while end != 'n' :
                for d in lst_flat :
                    if str(address) in d['address']:
                        self.counter += 1
                        print(d) 
                        n = input('which part: ').lower()
                        d[n] = input(f'{n}: ')
                        end = input('change mor? (y/n) ').lower()
                self.file_name.write_info_user(lst_flat)
                if self.counter == 0:
                    print("This address is not found!")
                    break
        else :
            print('This address in not valid')

    def __str__(self):
        return f'rooms = {self.rooms}\nHouse_area = {self.house_area}\non floor =  {self.floor}\nnumber of floor = {self.num_of_floor}\nmortgage_amount = {self.mortgage}\nrent_amount = {self.rent}\nsale_price = {self.sale}\non_sale= {self.on_sale}'


class Store :
    file_name = HandleFile.HandleFile('store.csv')
    counter = 0
    def __init__(self, owner, renter, address,area, mortgage_amount, rent_amount, sale_price ,on_sale = False,on_rent=True , tel ='active'):

        self.owner = owner
        self.renter = renter
        self.address= address
        self.area =float(area)
        self.mortgage= mortgage_amount
        self.rent = rent_amount
        self.sale = sale_price
        self.tel = tel
        self.on_sale = on_sale


    def edite_store_info(self, address):
        if isinstance(address, Address) :
            with open('store.csv', 'r') as f :
                r = csv.DictReader(f)
                lst_flat = list(r)
            end = ''
            while end != 'n' :
                for d in lst_flat :
                    if str(address) in d['address']:
                        self.counter += 1
                        print(d) 
                        n = input('which part: ').lower()
                        d[n] = input(f'{n}: ')
                        end = input('change mor? (y/n) ').lower()
                self.file_name.write_info_user(lst_flat)
                if self.counter == 0 :
                    print('This address is not found!')
                    break
        else:
            print('This address is not valid')

    def save_info(self):
         self.file_name.append_info_user(self.__dict__)


   

    def __str__(self):
        return f'Area= {self.area}\naddress = {self.address}\nTelephone = {self.tel}\nmortgage_amount = {self.mortgage}\nrent_amount = {self.rent}\nsale_price = {self.sale}\non_sale= {self.on_sale}'       
