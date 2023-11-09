#TO RETRIVE BANK DETAILS
class BankAccount:
  
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("YOU DEPOSITED ₹{}.new balance:₹{}".format(amount,self.__account_balance))
      
    else:
      print("INVALID DEPOSIT AMOUNT!")
      
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance  -= amount
      print("WITHDRAW ₹{}. NEW BALANCE: ₹{}".format(amount,self.__account_balance))
          
    else:
          print("INVAILD WITHDRAWL AMOUNT* OR INSUFFICIANT BALANCE!")
          
  def display_balance(self):
    print("Account Balance for {} (Account #{}): ₹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))
  
  #create an instance of the bank account class
account = BankAccount(account_number= "180924052",
                        account_holder_name= "PRAGADHEES",
                        initial_balance= 500.0)
  
  #test deposit and withdrawl functionlity
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
