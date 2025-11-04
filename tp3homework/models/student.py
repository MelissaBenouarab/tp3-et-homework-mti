from models.member import member

class student(member):
    """Classe représentant un étudiant."""

    def __init__(self, student_id, full_name, email, phone, address, join_date, skills, interests, group, subscription_status):
        super().__init__(full_name, email, phone, address, join_date, skills, interests)
        self.student_id = student_id
        self.group = group
        self.subscription_status = subscription_status  # paid / unpaid

    def register_member(self, member_name):
        print(f"🎓 L'étudiant '{member_name}' est inscrit dans le groupe {self.group}.")
