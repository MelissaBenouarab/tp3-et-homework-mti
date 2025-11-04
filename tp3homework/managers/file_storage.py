import json
from pathlib import Path

class file_storage:
    """Service générique de sauvegarde/chargement de fichiers JSON (DIP-ready)."""

    def save(self, filename, data):
        """Sauvegarde des données dans un fichier JSON."""
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"💾 Données sauvegardées dans {filename}")

    def load(self, filename):
        """Charge des données depuis un fichier JSON."""
        path = Path(filename)
        if not path.exists():
            print(f"⚠️ Le fichier {filename} n'existe pas.")
            return []
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"📂 Données chargées depuis {filename}")
        return data
