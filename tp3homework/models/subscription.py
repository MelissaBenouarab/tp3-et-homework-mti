from interfaces.payable import payable

class subscription(payable):
    """Classe de paiement d’abonnement."""

    def __init__(self, student_id, amount, date, status):
        self.student_id = student_id
        self.amount = amount
        self.date = date
        self.status = status  # paid / unpaid

    def process_payment(self):
        print(f"💳 Paiement de {self.amount} DA traité pour l'étudiant {self.student_id} le {self.date}.")
