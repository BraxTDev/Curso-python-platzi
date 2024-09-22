class BankAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance
    self.is_active = True

#realizar deposito
  def deposit (self, amount):
    if self.is_active:
        self.balance += amount