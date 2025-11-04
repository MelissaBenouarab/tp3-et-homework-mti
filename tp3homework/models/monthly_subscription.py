from models.subscription import subscription

class monthly_subscription(subscription):
    """Abonnement mensuel."""

    def __init__(self, student_id, amount, date, status):
        super().__init__(student_id, amount, date, status)
        self.period = "Mensuel"

    def process_payment(self):
        print(f"💳 Abonnement mensuel : paiement de {self.amount} DA pour l'étudiant {self.student_id} le {self.date}.")
