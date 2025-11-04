from models.member import member

class teacher(member):
    """Classe représentant un enseignant."""

    def __init__(self, teacher_id, full_name, email, phone, address, join_date, skills, interests):
        super().__init__(full_name, email, phone, address, join_date, skills, interests)
        self.teacher_id = teacher_id

    def register_member(self, member_name):
        print(f"👨‍🏫 L'enseignant '{member_name}' a été ajouté à la base de données.")
