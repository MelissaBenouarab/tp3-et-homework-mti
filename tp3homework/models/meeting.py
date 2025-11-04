from models.event import event

class meeting(event):
    """Événement de type réunion."""

    def __init__(self, event_name, description, event_date, organizer, participants):
        super().__init__(event_name, description, event_date, organizer, participants)
        self.type = "Meeting"

    def describe(self):
        return f"💬 Meeting: {self.event_name} — organisé par {self.organizer} le {self.event_date}"

    def schedule(self):
        print(f"📅 Réunion '{self.event_name}' prévue pour le {self.event_date}.")

    def register_member(self, member):
        self.participants.append(member)
        print(f"✅ {member.full_name} inscrit à la réunion '{self.event_name}'.")
