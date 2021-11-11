from datetime import date

class Card : #  class parent 
   
    def __init__(self, quantity):
        self.quantity = quantity   # quantity of trip 
        self.expense = None
        
    def set_expense (self):  # each trip expense is 1000 Toman
        self.expense = self.quantity * 1000
    
    
class SingleCard (Card): 

    def used_once (self) :
        if self.quantity == 1 :
            print("Enjoy your trip!")
        else:
            print("This Card can't be used more than once!\n")

class CreditMetroCard (Card):
    credit = 10000

    def __init__(self, quantity):
        super().__init__(quantity)
        self.deduction = None
        self.charge = None
   
    def set_deduction (self) :
        self.deduction = self.credit - self.expense
        if self.deduction <= 0:
            self.deduction = 0
            return "You need to charge the card!\n"
            
    
    def set_charge (self, q_trips):
        self.charge = (q_trips * 1000) + self.deduction
        self.credit +=  self.charge
        print(f"Credit: {self.deduction}\nThis card is charged for {q_trips} trips.\nCurrent credit is {self.charge} Toman\n")
    

class CardWithExpiryDate (CreditMetroCard) :

    def __init__(self, quantity) :
        super().__init__(quantity)
        self.expiry_date = date(2021,8,23)  
        self.today = date.today()
        self.expiry = None


    def set_expiration(self):
        self.expiry = (self.expiry_date - self.today).days

    def expiration (self):
        if self.today > self.expiry_date :
            print(f"You've got {self.deduction} Toman But your card is expired.\n")
        elif self.today == self.expiry_date :
            print(f"Today is the last day of the expiration date!\n")
        else :
            print(f"{abs(self.expiry)} day(s) before the expiration date. You've got {self.deduction} Toman\n")



print("Pass!\n")

single_card = SingleCard(2)
single_card.used_once()



credit_Mcard = CreditMetroCard(9)
credit_Mcard.set_expense()
credit_Mcard.set_deduction()
credit_Mcard.set_charge(10)



credit_exCard = CardWithExpiryDate(3)
credit_exCard.set_expense()
credit_exCard.set_deduction()
credit_exCard.set_expiration()
credit_exCard.expiration()





