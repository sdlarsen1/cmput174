class Account:
    def __init__(self, account_number = 0, balance = 100.0):
        self.__accountID = account_number
        self.__balance = balance
    
    def getID(self):
        return self.__accountID
    
    def getbalance(self):
        return self.__balance
    
    def setID(self,newValue):
        self.__accountID = newValue
    
    def setbalance(self,newValue):
        self.__balance = newValue
    
    def deposit(self, value):
        self.__balance = self.__balance + value
        
    def withdraw(self, value):
        if self.__balance >= value:
            self.__balance = self.__balance - value