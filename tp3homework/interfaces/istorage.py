from abc import ABC, abstractmethod

class istorage(ABC):
    """Interface pour différents types de stockage"""

    @abstractmethod
    def save_data(self, data, filename):
        """Sauvegarde les données dans un format spécifique"""
        pass

    @abstractmethod
    def load_data(self, filename):
        """Charge les données depuis un fichier"""
        pass
