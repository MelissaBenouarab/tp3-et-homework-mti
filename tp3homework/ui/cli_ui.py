from interfaces.iui import iui

class cli_ui(iui):
    """Interface utilisateur en console"""
    
    def display_message(self, message):
        print(f"[CLI] {message}")

    def get_input(self, prompt):
        return input(f"[CLI] {prompt}: ")
