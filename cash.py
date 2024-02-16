class Account:
    def __init__(self):
        self._balance = 0 

    @property
    def balance(self):
        return self._balance
      
    def deposit(self,n):
        self._balance += n
    
    def withdraw(self,n):
        self._balance -= n
    
jimmy = Account()  
print("balance : ", jimmy.balance)
jimmy.deposit(500)   
jimmy.withdraw(200)      
print("balance : ", jimmy.balance)