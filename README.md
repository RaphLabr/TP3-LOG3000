# TP3-LOG3000
Équipe #45

Objectif:
Le but de ce projet est d'implémenter une calculatrice web afin de permettre aux utilisateurs d'avoir accès à une calculatrice simple à partir de leur ordinateur. La calculatrice est capable de supporter l'addition, la soustraction, la multiplication et la division de nombres et de chiffres

Prérequis:
Avoir Python 3.13.5 installé sur son ordinateur
Avoir pip 26.2.1 installé sur son ordinateur

Guide d'installation:
1) Cloner le repertoire git du projet dans votre IDE de choix supportant python

2) Créer un environnement virtuel avec la commande: python -m venv .venv

3) Activer l'environnement virtuel avec la commande ci-dessous approprié à votre système d'exploitation:
   -Windows(Powershell): .\venv\Scripts\Activate
   -MacOS/Linux(Bash): source path/to/venv/bin/activate
   Pour plus d'aider pour la configuration de l'environnement virtuel, veuillez-vous référer à la page suivante: https://www.geeksforgeeks.org/python/create-virtual-environment-using-venv-python/

4) Installer les requis avec la commande: pip install -r requirements.txt

5) Rouler la commande python app.py

6) Pour accéder à la calculatrice il suffit d'ouvrir un navigateur web et se connecter au port indiqué dans le terminal (qui devrait être http://127.0.0.1:5000)



Instructions d'utilisation:
1) Prérequis: avoir ouvert la calculatrice  

2) Appuyer sur le bouton C pour effacer les chiffres et nombres existant

3) Entrez le premier chiffre ou nombre en utilisant les boutons de la calculatrice

4) Sélectionner l'opérateur désiré à partir des boutons oranges de la colonne droite

5) Entrez le deuxième chiffre ou nombre en utilisant les boutons de la calculatrice

6) Appuyer sur le bouton = pour obtenir le résultat de l'opération

7) (Optionnel) Pour effectuer une opération avec le résultat, retourner à l'étape 

Instruction de Tests:
Pour exécuter un test individuel:
python -m pytest tests/[nom_du_fichier_de_test] -v
Pour exécuter la suite de test en entier
python -m pytest tests/ -v
L'option -v affiche le résultat détaillé de chaque test.

Flux de contribution:
Pour les contributions, les normes suivantes sont en vigeur sur le projet:
Branches:
1) Nom de branche représentatif en français en kebab-case

Pull requests:
1) Il est obligatoire de faire une pull-request pour mettre des modifications sur la branche "main".
2) Le nom de la pull request doit être representatif de la tâche à faire.
3) La pull request doit contenir une description qui explique ce qui a été accompli dans la branche.
4) La pull request doit être liée à un issue.
4) La pull request doit être approuvée par Alexis, par Anaïs ou par Raphaël pour être mergé sur main.
5) La personne qui s'occupe de la revue de la pull-request est celle qui merge une pull-request.

Issues:
1) Le nom du issue doit être representatif de la tâche à faire.
2) Le issue doit contenir une description qui explique ce qui a été accompli dans la branche.
3) Une personne qui travaille sur un issue doit s'assigner dessus.
4) Si un issue contient du code, il nécessaire de faire une pull request pour intégrer le nouveau code

