from models.event import event

class trip(event):
    """Événement de type voyage (hérite de event)."""

    def __init__(self, event_name, description, event_date, organizer, participants):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.type = "Trip"

    def describe(self):
        return f"🚌 Trip: {self.event_name} — organisé par {self.organizer} le {self.event_date}"

    def schedule(self):
        print(f"📅 Le voyage '{self.event_name}' est prévu pour le {self.event_date}.")

    def register_member(self, member):
        self.participants.append(member)
        print(f"✅ {member.full_name} inscrit au voyage '{self.event_name}'.")
