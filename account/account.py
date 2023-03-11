class Account:
    name = "account_dummy"
    balance = 0

    # default constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, a):
        if self.balance < a:
          return "Error: Raised when the balance less or equal than zero"
        else:
            self.balance -= a
            return self.balance
            
               
   