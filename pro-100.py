class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkbalance(self):
        print("Your Balance is 4000")
    def withdrawel(self,amount):
        newamount=4000-amount
        print("You have withdrawn"+str(amount)+"Your new balance is"+str(newamount))
def main():
    cardnumber=input("Enter your Cardnumber")
    pin=input("ENter your Pin")
    p1=Atm(cardnumber,pin)
    print("choose your activity")
    print("1.Balance enquiry,2.withdrawel")
    activity=int(input("ENter the activity number"))
    if(activity==1):
        p1.checkbalance()
    elif(activity==2):
        amount=int(input("ENter the amount"))
        p1.withdrawel(amount)
    else:
        print("Enter a vaild activity number")
if __name__=="__main__":
    main()