from interfaces.organizable import organizable

class event(organizable):
    """Classe de base pour un événement."""

    def __init__(self, event_name, description, event_date, organizer, participants):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = participants  # liste de noms

    def schedule(self):
        print(f"📅 L'événement '{self.event_name}' est prévu pour le {self.event_date}.")

    def describe(self):
        """Description générique de l'événement."""
        return f"🕌 Event: {self.event_name} — organisé par {self.organizer}"
