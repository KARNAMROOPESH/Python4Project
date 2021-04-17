class Atm:
    def __init__(self,acc,pin,money , total , balance):
        self.acc = card
        self.pin = pincode
        self.money = amount  
        self.total = 10,000    
    def information(self):
        self.balance = balanceam
        balanceam1 = str(self.balance)
        print("Thanks for using RoopBank . As per now your Bank balance is " + balanceam1 )
        
card = input("Enter your Card number :")
pincode = input("Enter your Pin :")
amount = int(input("Enter amount needed :"))
balanceam =  10000 - amount

AnyTimeMoney = Atm(card , pincode , amount , 10000 , balanceam)
AnyTimeMoney.information()