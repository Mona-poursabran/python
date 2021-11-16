from first_part import *
from second_part import *

renter= Person('Jack','smith','Jack@gmail.com','5487481254','0933648544871')
owner = Person('Ali','Emadi','Aliemadi@gmail.com','3245698716','09351247896')
addr = Address('Tehran','Vanak',3,15467)
# owner.edite_info('3245698716')


house = House(owner, renter,addr, 2,70,30.0,1,500000000,1500000,950000000,'active',False,True )
# house.edite_house_info(addr)

estate = Estate()
# estate.search_rent('house')


buyer = Person('Nazanin', 'Mosafer', 'Nazi@gmail.com', '9631475233', '22448322')
sale_contract = ContractSale(buyer)
sale_contract.show_all_sale_house_and_apartment('house')
sale_contract.sale('house','1400/06/28')
print(sale_contract.deactivate())
print(sale_contract)


print('\n',"########"*5,'\n')

renter = Person('Amir', 'Alizadeh', "Amir354@mail.com", '2244778899', '09171245986')
rent_contract = ContractRent(renter)
rent_contract.show_all_sale_house_and_apartment('house')
rent_contract.rent('house', '1400/06/25', '1401/06/22')
print(rent_contract.deactivate())
print(rent_contract)




