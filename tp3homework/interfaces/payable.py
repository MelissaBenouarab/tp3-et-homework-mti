from abc import ABC, abstractmethod

class payable(ABC):
    """Interface pour les paiements et abonnements"""

    @abstractmethod
    def process_payment(self):
        """Traite le paiement"""
        pass
