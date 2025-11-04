Ce projet met en œuvre un système de gestion pour une association de jeunes à vocation coranique, conçu selon les principes de la programmation orientée objet (POO) et en respectant les principes SOLID.

Il permet de gérer :
-Les membres (étudiants, enseignants)
-Les événements (voyages, réunions, compétitions)
-Les abonnements et les dons
-La persistance des données à l’aide de classes de dépôt (repositories) et de stockage.

Principes SOLID appliqués:

1. Principe de responsabilité unique (SRP) :
Définition :
Chaque classe doit avoir une seule et unique raison de changer.

Application :
-Member : contient uniquement les données d’un membre (nom, email, etc.)
-MemberRepository : gère l’enregistrement et le chargement des membres à partir du stockage
-Subscription : gère uniquement la logique de paiement
-EventManager (si implémentée) : gère séparément les opérations liées aux événements

Problème résolu :
Auparavant, certaines classes mélangeaient la logique métier et la gestion des fichiers (par exemple, une classe Member qui s’enregistrait elle-même).
La séparation des responsabilités a rendu le système plus clair, plus testable et plus facile à maintenir.

2. Principe ouvert/fermé (OCP):
Définition :
Les classes doivent être ouvertes à l’extension mais fermées à la modification.

Application :
-Event est étendue par Trip, Meeting et Competition
-Subscription est étendue par MonthlySubscription et AnnualSubscription

Problème résolu :
Au lieu de modifier les classes existantes à chaque nouveau type d’événement ou d’abonnement,
il suffit d’ajouter de nouvelles sous-classes, évitant ainsi les duplications et les erreurs potentielles.

3. Principe de substitution de Liskov (LSP) :
Définition :
Les sous-classes doivent pouvoir remplacer leurs classes parentes sans altérer le comportement du programme.

Application :
-Trip, Meeting et Competition peuvent remplacer Event dans n’importe quel contexte
-Student et Teacher peuvent remplacer Member

Problème résolu :
Garantit le bon fonctionnement du polymorphisme — une fonction qui attend un objet Event peut recevoir une sous-classe sans problème, rendant le système souple et cohérent.

4. Principe de ségrégation des interfaces (ISP) :
Définition :
Les classes ne doivent pas dépendre d’interfaces dont elles n’ont pas besoin. Les interfaces doivent être petites et spécifiques.

Application :
-Payable : implémentée par Subscription et Donation (contient uniquement process_payment())
-Organizable : implémentée par Event et ses sous-classes (contient schedule())
-Registrable : implémentée par Member (contient register_member())

Problème résolu :
Évite la création d’une interface “géante” avec trop de méthodes.
Chaque classe implémente uniquement les fonctionnalités nécessaires, garantissant un design léger et découplé.

5. Principe d’inversion des dépendances (DIP) :
Définition :
Les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Tous deux doivent dépendre d’abstractions.

Application :
-MemberRepository dépend d’une interface abstraite Storage (par exemple JSONStorage, CSVStorage)
-Le programme principal (main.py) utilise l’injection de dépendances pour choisir le type de stockage

Problème résolu :
Permet de changer facilement le système de stockage (par exemple, passer d’un fichier JSON à une base de données)
sans modifier la logique principale du programme, rendant le système évolutif et adaptable.
Auparavant, certaines classes mélangeaient la logique métier et la gestion des fichiers (par exemple, une classe Member qui s’enregistrait elle-même).
La séparation des responsabilités a rendu le système plus clair, plus testable et plus facile à maintenir.
