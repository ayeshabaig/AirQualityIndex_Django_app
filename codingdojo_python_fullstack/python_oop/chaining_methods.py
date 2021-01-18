class User:
def_init_(self,name,email):
  self.name = name
  self.email = email
  self.account_balance = 0
  
# adding the deposit method
def make_deposit(self, amount): # takes the argument that is in the amount of the deposit.
    self.account_balance += amount # the specific users' account increases by the amount of the value recieved
    return self

def make_withdrawal(self, amount):
    self.account_balance -= amount
    return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
   
    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount
        return self


samantha = User("Samantha", "todd@todd.com")
bob = User("Bob", "jane@jane.com")
lily = User("Lily", "john@john.com")

samantha.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

bob.make_deposit(50).make_deposit(1000).make_withdrawal(500).make_withdrawal(100).display_user_balance()

lily.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()
