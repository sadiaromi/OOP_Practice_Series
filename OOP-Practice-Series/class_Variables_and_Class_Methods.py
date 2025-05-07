class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def show_bank(self):
        print("Bank Name:", self.bank_name)

account1 = Bank()
account2 = Bank()

print("Before changing bank name:")
account1.show_bank()
account2.show_bank()

Bank.change_bank_name("National Bank")

print("\nAfter changing bank name:")
account1.show_bank()
account2.show_bank()
