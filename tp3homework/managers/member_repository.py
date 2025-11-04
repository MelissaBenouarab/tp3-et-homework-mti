import json
from pathlib import Path

class member_repository:
    """Gère la sauvegarde et le chargement des membres."""

    def __init__(self, filename="data/members.json"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)

    def save_members(self, members):
        """Sauvegarde les membres dans un fichier JSON."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([m.__dict__ for m in members], f, ensure_ascii=False, indent=4)
        print(f"✅ Membres sauvegardés dans {self.filename}.")

    def load_members(self):
        """Charge les membres depuis un fichier JSON."""
        if not self.filename.exists():
            print(f"⚠️ Aucun fichier trouvé à {self.filename}.")
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"📂 Membres chargés depuis {self.filename}.")
        return data
