from interfaces.iui import iui

class web_ui(iui):
    """Interface utilisateur simulée pour le Web"""
    
    def display_message(self, message):
        print(f"[WEB] {message}")

    def get_input(self, prompt):
        # Simule une saisie web
        fake_input = "Simulation Web Input"
        print(f"[WEB] {prompt}: {fake_input}")
        return fake_input
