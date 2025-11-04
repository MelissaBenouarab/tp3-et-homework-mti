from abc import ABC, abstractmethod

class iui(ABC):
    """Interface pour les interfaces utilisateur (Console, Web, etc.)"""

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass
