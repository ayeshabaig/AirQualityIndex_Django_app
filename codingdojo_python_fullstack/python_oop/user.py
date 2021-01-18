 Create a file with the User class, including the __init__ and make_deposit methods  Add a make_withdrawal method to the User class  Add a display_user_balance method to the User class  Create 3 instances of the User class  Have the first user make 3 deposits and 1 withdrawal and then display their balance  Have the second user make 2 deposits and 2 withdrawals and then display their balance  Have the third user make 1 deposits and 3 withdrawals and then display their balance


class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount): # takes an argument that is the amount of the deposit
    self.account_balance += amount # the specific user's account increases by the amount of the value received
   
    def make_withdrawal(self, amount):
        self.account_balance -= amount
   
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
   

samantha = User("Samantha", "ayesha@fakemail.com")
bob = User("Bob", "bob@fakemail.com")
lily = User("Lily", "lily@john.com")

samantha.make_deposit(100)
samantha.make_deposit(100)
samantha.make_deposit(100)
samantha.make_withdrawal(50)
samantha.display_user_balance()

bob.make_deposit(50)
bob.make_deposit(1000)
bob.make_withdrawal(500)
bob.make_withdrawal(100)
bob.display_user_balance()

lily.make_deposit(100)
lily.make_withdrawal(25)
lily.make_withdrawal(25)
lily.make_withdrawal(25)
lily.display_user_balance()

	
