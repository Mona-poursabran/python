import csv
from datetime import datetime
import pandas as pd
import test1
from first_part import *
import HandleFile

class Estate :
    def __init__(self) -> None:
        self.on_sale = True
        self.rent =True
        self.area = None
        self.sale_price = None
        self.mortgage_amount = None
        self.rent_amount = None
        self.counter= 0

    def search_sale (self, type) :
        type = str(type).strip().lower()
        if type == "house" :
            self.on_sale = True 
            print("you are looking for a sale house:")
            self.area = float(input("area: "))
            self.sale_price = int(input('price: '))
            lst_find_sale_house = []
            with open('house.csv', 'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    if row['on_sale'] == str(self.on_sale).capitalize() and float(row['house_area'])== self.area and int(row['sale']) == self.sale_price:
                        # print('found')
                        self.counter += 1
                        lst_find_sale_house.append(row)
                        a = 0
                        for i in lst_find_sale_house :  ## Ading Code to each house 
                                a += 1
                                i.update({'code':a})
                        Show_info = pd.DataFrame(lst_find_sale_house)
                        print(Show_info)
            if self.counter == 0:
                print("No house is found")

        elif type == "apartment" or type == "flat" :
            self.on_sale = True
            print("you are looking for a sale apartment:")
            self.area = float(input("area: "))
            self.sale_price = int(input('price: '))
            lst_find_sale_flat=[]
            with open('apartment.csv', 'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    if row['on_sale'] == str(self.on_sale).capitalize() and float(row['house_area']) == self.area and int(row['sale']) == self.sale_price:
                        # print('found')
                        self.counter += 1
                        lst_find_sale_flat.append(row)
                        a = 0
                        for i in lst_find_sale_flat :  ## Ading Code to each house 
                                a += 1
                                i.update({'code':a})
                        Show_info = pd.DataFrame(lst_find_sale_flat)
                        print(Show_info)
            if self.counter == 0:
                print("No flat is found")
        else:
            print('This type is invalid!')
                    
    def search_rent(self, type) :
        type = str(type).lower()
        self.on_rent =True
        if type == "house" :
            print("you are looking for a rent house!")
            self.area = float(input("area: "))
            self.mortgage_amount  = int(input("mortgage_amount: "))
            self.rent_amount = int(input("rent_amount: "))
            lst_find_rent_house = []
            with open('house.csv', 'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    if row['on_rent'] == str(self.rent).capitalize() and float(row['house_area']) == self.area and int(row['mortgage']) == self.mortgage_amount and int(row['rent']) == self.rent_amount :
                        # print("found")
                        self.counter += 1
                        lst_find_rent_house.append(row)
                        Show_info = pd.DataFrame(lst_find_rent_house)
                        print(Show_info)
            if self.counter == 0:
                print("No house is found")

        elif type == "apartment" or type == "flat" :
            print("you are looking for a rent apartment!")
            self.area = float(input("area: "))
            self.mortgage_amount  = int(input("mortgage_amount: "))
            self.rent_amount = int(input("rent_amount: "))
            lst_find_rent_flat =[]
            with open('apartment.csv', 'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    if row['on_rent'] == str().capitalize(self.rent) and float(row['house_area']) == self.area and int(row['mortgage']) == self.mortgage_amount and int(row['rent']) == self.rent_amount :
                        # print("found")
                        self.counter += 1
                        lst_find_rent_flat.append(row)
                        Show_info = pd.DataFrame(lst_find_rent_flat)
                        print(Show_info)
            if self.counter == 0:
                print("No flat is found")
        else:
            print('this type is not valid!')


class ContractSale:
    list_check_sale =[]
    # list_check_sale_flat = []
    file_name_update_apartment = HandleFile.HandleFile('sale_apartment.csv')
    file_name_update_house =HandleFile.HandleFile('sale_house.csv')

    def __init__(self, buyer) :
        self.buyer = buyer
        self.owner = ''
        self.date_of_contract = None
        self.expiration_contract = None
        self.type = ''
        self.code = ''


    def show_all_sale_house_and_apartment (self,type):
        if type == 'apartment' :
             with open('sale_apartment.csv','r') as f :
                read = csv.DictReader(f)
                for row in read :
                    print(row) 

        if type == 'house':
            with open('sale_house.csv','r') as f :
                read = csv.DictReader(f)
                for row in read :
                    print(row)

       
        
    def sale (self,type, date_of_contract='1400/06/25'):
        self.code = int(input('Code: '))
        self.type = type
        self.date_of_contract = datetime.strptime(date_of_contract, "%Y/%m/%d")
        list_sale = test1.list_sale(type)

        for i in list_sale :
            for j in i :
                if j['code'] == self.code:
                    print(j)
                    print("Done!")
                    self.owner = j['owner']
                    j['owner'] = self.buyer.fname +' '+self.buyer.last_name
                    self.list_check_sale.append((j, self.date_of_contract.date(), self.type))
        if self.type == 'apartment':
            f =HandleFile.HandleFile('sale_apartment.csv')
            for i in self.list_check_sale:
                if i[2] == 'apartment' :
                    f.write_info_user(i[0])
        elif self.type == 'house':
            f = HandleFile.HandleFile('sale_house')
            for i in self.list_check_sale:
                if i[2] == 'house' :
                    f.write_info_user(i[0])

            
  
    
    def validation_sale (self,):
        pass


    def deactivate(self): # Honestly i don't get this part :(
        return f'this {self.type} is deactivate with code: {self.code}'


    def __str__(self):
        return f'{self.owner} sold the house to {self.buyer} in {self.date_of_contract.date()}'


class ContractRent:
    list_check_rent =[]
    # list_check_rent_flat = []
    def __init__(self, renter) :
        self.renter = renter
        self.owner = ''
        self.date_of_contract = None
        self.expiration_contract = None
        self.type =''
        self.code = 0


    def show_all_sale_house_and_apartment (self,type):
        if type == 'house':
            with open('rent_house.csv','r') as f :
                read = csv.DictReader(f)
                for row in read :
                    print(row)
        elif type == 'apartment' :
             with open('rent_apartment.csv','r') as f :
                read = csv.DictReader(f)
                for row in read :
                    print(row) 


    def rent (self, type,  date_of_contract, expiration_contract):
        self.code = int(input('Code: '))
        self.type = type
        self.date_of_contract =  datetime.strptime(date_of_contract, "%Y/%m/%d")
        self.expiration_contract=  datetime.strptime(expiration_contract, "%Y/%m/%d")
        list_rent  = test1.list_rent(type)
        # print(list_rent)
        for i in list_rent:
            for j in i :
                if j['code'] == self.code:
                    self.owner = j['owner']
                    j['renter'] = self.renter.fname +' ' + self.renter.last_name
                    # print(j)
                    print('Done!')
                    self.list_check_rent.append((j, self.date_of_contract.date(), self.type))

                # print(self.owner)
    def validation_rent(self): # Honestly i don't get this part :(
            pass

    def deactivate(self):
        return f'this {self.type} is deactivate with code: {self.code}.'

    def __str__(self):

        return f'{self.owner} rent the {self.type} to {self.renter} in {self.date_of_contract.date()} till {self.expiration_contract.date()}'

                    






