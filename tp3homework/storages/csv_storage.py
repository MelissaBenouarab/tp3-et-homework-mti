import csv
from interfaces.istorage import istorage

class csv_storage(istorage):
    """Classe de stockage pour sauvegarder et charger des données en CSV."""

    def save_data(self, data, filename):
        """Sauvegarde une liste de dictionnaires dans un fichier CSV."""
        if not data:
            print("⚠️ Aucune donnée à sauvegarder.")
            return

        keys = data[0].keys()
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Données sauvegardées dans {filename} (CSV).")

    def load_data(self, filename):
        """Charge des données depuis un fichier CSV."""
        try:
            with open(filename, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = list(reader)
            print(f"📂 Données chargées depuis {filename} (CSV).")
            return data
        except FileNotFoundError:
            print(f"⚠️ Fichier {filename} introuvable.")
            return []
