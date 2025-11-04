from abc import ABC, abstractmethod

class organizable(ABC):
    """Interface pour les événements organisables"""

    @abstractmethod
    def schedule(self):
        """Planifie l'événement"""
        pass
