from models.subscription import subscription

class annual_subscription(subscription):
    """Abonnement annuel avec réduction."""

    def __init__(self, student_id, amount, date, status, discount=0.10):
        super().__init__(student_id, amount, date, status)
        self.period = "Annuel"
        self.discount = discount

    def process_payment(self):
        discounted_amount = self.amount * (1 - self.discount)
        print(f"💳 Abonnement annuel : paiement de {discounted_amount:.2f} DA (réduction {self.discount*100:.0f}%) pour l'étudiant {self.student_id} le {self.date}.")
