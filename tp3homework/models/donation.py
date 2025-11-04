from interfaces.payable import payable

class donation(payable):
    """Classe représentant un don."""

    def __init__(self, donor_name, amount, date, message=""):
        self.donor_name = donor_name
        self.amount = amount
        self.date = date
        self.message = message

    def process_payment(self):
        print(f"💰 Don de {self.amount} DA reçu de {self.donor_name} le {self.date}. Message: {self.message}")
