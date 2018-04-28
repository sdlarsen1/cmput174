from Account_Class import Account
def main():
    accountA = Account()
    
    accountA.setID(1234)
    accountA.setbalance(20500)
    print("Account ID:", accountA.getID())
    print("Account balance:", accountA.getbalance())
    
    accountA.withdraw(500)
    accountA.deposit(1500)
    print("Account ID:", accountA.getID())
    print("Account balance:", accountA.getbalance())    
main()