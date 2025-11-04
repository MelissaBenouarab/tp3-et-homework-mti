class event_manager:
    """Gère la planification et l'affichage des événements."""

    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Ajoute un nouvel événement."""
        self.events.append(event)
        print(f"✅ Événement '{event.event_name}' ajouté.")

    def show_events(self):
        """Affiche tous les événements programmés."""
        if not self.events:
            print("⚠️ Aucun événement enregistré.")
        for ev in self.events:
            ev.schedule()
