from interfaces.registrable import registrable

class member(registrable):
    """Classe représentant un membre de base."""

    def __init__(self, full_name, email, phone, address, join_date, skills, interests):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills = skills
        self.interests = interests

    def register_member(self, member_name):
        print(f"👤 Le membre '{member_name}' a été enregistré avec succès.")
