'''
4. Account nomli klass yarating. Unda quyidagi rasmda ko’rsatilgan atribut va metodlarni yarating.

Atributlar:

-id: String
-name: String
-balance: int = 0
Konstruktorlar:

+Account(id: String, name: String)
+Account(id: String, name: String, balance: int)
Metodlar:

+getID(): String
+getName(): String
+getBalance(): int
+credit(amount: int): int
Balansga miqdorni qo'shadi, balansni qaytaradi
+debit(amount: int): int
Agar miqdor <= balans bo'lsa, balansdan miqdorni kamaytiradi
Aks holda "Amount exceeded balance" deb chop etadi
Balansni qaytaradi
+transferTo(another: Account, amount: int): int
Agar miqdor <= balans bo'lsa, ko'rsatilgan hisobga miqdorni o'tkazadi
Aks holda "Amount exceeded balance" deb chop etadi
Balansni qaytaradi
+toString(): String
"Account[id=?,name=?,balance=?]" formatida qaytaradi

'''

class Account:
    def __init__(self, id, name, balance = 0):
        self.id = id
        self.name = name
        self.balance = balance
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_balance(self):
        return self.balance
    def credit(self, amount):
        self.balance += amount
        return self.balance
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -=amount
        else:
            print("Balans yetmaydi")
        return self.balance
    def transferTo(self, another, amount):
        if amount <= self.balance:
            self.balance -= amount
            another.balance += amount
        else:
            print("Balans yetmaydi1")
        return self.balance
    def toString(self):
        return f"Account[id={self.id}, name={self.name}, balance={self.balance}]"
    
    
ac1 = Account("hello", "Travis")
ac2 = Account("world", "IKO", 50000)


print(ac1.toString())
print(ac2.toString())
print("\n\n")


ac1.credit(50)
print(ac1.toString())
print("\n\n")

ac1.debit(30)
print(ac1.toString())
print("\n\n")

ac2.transferTo(ac1, 50)
print(ac2.toString())
print(ac1.toString())