#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Example applying Dependency Inversion Principle (DIP)

# --- Abstraction ---
class ILogger:
    """Interface de base pour les loggers"""
    def log(self, message):
        raise NotImplementedError("Subclasses must implement log()")


# --- Implémentation concrète 1 ---
class FileLogger(ILogger):
    """Logger vers un fichier"""
    def log(self, message):
        print(f"Logging to file: {message}")


# --- Implémentation concrète 2 ---
class DatabaseLogger(ILogger):
    """Logger vers une base de données"""
    def log(self, message):
        print(f"Logging to database: {message}")


# --- Application (haut niveau) ---
class Application:
    """Classe principale qui dépend d'une abstraction ILogger"""
    def __init__(self, logger: ILogger):
        self.logger = logger  # dépend d'une interface, pas d'une implémentation

    def start(self):
        self.logger.log("Application started")


# --- Point d’entrée ---
def main():
    """Fonction principale"""
    print("=== Choisissez le type de logger ===")
    print("1. File Logger")
    print("2. Database Logger")

    choice = input("Votre choix (1 ou 2) : ")

    # Sélection du logger selon le choix utilisateur
    if choice == "1":
        logger = FileLogger()
    elif choice == "2":
        logger = DatabaseLogger()
    else:
        print("Choix invalide, utilisation par défaut du FileLogger.")
        logger = FileLogger()

    # Création de l'application avec le logger choisi
    app = Application(logger)
    app.start()


# --- Exécution directe du script ---
if __name__ == "__main__":
    main()
