class BankAcount:#classe conta bancaria
    def __init__(self, person, balance):
        self._person = person
        self._balance = balance

    @property#faz com que o person possa ser acessado sem '_'
    def person(self):
        return self._person
    
    @property #faz com que o balance possa ser acessado sem '_'
    def balance(self):
        return self._balance
    
    @property
    def see_extract(self): #mostra as informaçoes da conta
        print(f'Person: {self._person}')
        print(f'Balance: {self._balance}')
    
    def deposit(self, valor):#deposita o valor
       self._balance += valor
       print(f'Balance: {self._balance}')
        
    def withdraw(self, valor):#saca o valor se o balance nao ficar negativo
        if self._balance < valor: 
            print('Invalid, not enough balance')
        else:
            self._balance -= valor
            print(f'Balance: {self._balance}')

jose = BankAcount('Jose', 10000)
jose.deposit(34000)
jose.withdraw(10000)
jose.see_extract
print(jose.balance)