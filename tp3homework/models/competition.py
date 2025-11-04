from models.event import event

class competition(event):
    """Événement de type compétition."""

    def __init__(self, event_name, description, event_date, organizer, participants):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.type = "Competition"

    def describe(self):
        return f"🏆 Competition: {self.event_name} — organisée par {self.organizer} le {self.event_date}"

    def schedule(self):
        print(f"📅 Compétition '{self.event_name}' prévue pour le {self.event_date}.")

    def register_member(self, member):
        self.participants.append(member)
        print(f"✅ {member.full_name} inscrit à la compétition '{self.event_name}'.")
