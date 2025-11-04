import json
from interfaces.istorage import istorage

class json_storage(istorage):
    """Classe de stockage pour sauvegarder et charger des données en JSON."""

    def save_data(self, data, filename):
        """Sauvegarde des données dans un fichier JSON."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Données sauvegardées dans {filename} (JSON).")

    def load_data(self, filename):
        """Charge des données depuis un fichier JSON."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"📂 Données chargées depuis {filename} (JSON).")
            return data
        except FileNotFoundError:
            print(f"⚠️ Fichier {filename} introuvable.")
            return []
