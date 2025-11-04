from models.subscription import subscription
from models.monthly_subscription import monthly_subscription
from models.annual_subscription import annual_subscription
from models.donation import donation

class finance_manager:
    """Gère les opérations financières : paiements, dons, abonnements."""

    def __init__(self):
        self.transactions = []

    def process_subscription(self, sub: subscription):
        """Traite un abonnement (mensuel ou annuel)."""
        sub.process_payment()
        self.transactions.append(sub.__dict__)

    def add_donation(self, donor_name, amount, date, message=""):
        """Ajoute un don et enregistre la transaction."""
        don = donation(donor_name, amount, date, message)
        don.process_payment()
        self.transactions.append(don.__dict__)

    def show_all_transactions(self):
        """Affiche toutes les transactions traitées."""
        print("\n💰 Liste des transactions :")
        for t in self.transactions:
            print(t)
