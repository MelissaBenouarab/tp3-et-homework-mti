from abc import ABC, abstractmethod

class registrable(ABC):
    """Interface pour l'enregistrement des membres ou participants"""

    @abstractmethod
    def register_member(self, member_name):
        """Inscrit un membre ou participant"""
        pass
