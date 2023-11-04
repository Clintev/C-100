class atm:
    def __init__(self, atm_number , atm_card):
        self.atm_number = atm_number
        self.atm_card = atm_card

    def Cash_Withdrawal(self):
        print(self.atm_number)
    def Balance_Enquiry(self):
        print(self.atm_card)

obj = atm(1, 28894)
obj.Cash_Withdrawal()
obj.Balance_Enquiry()

