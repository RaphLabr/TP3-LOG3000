# Readme: module "tests"

Le module "tests" rassemble les tests couvrant les opérateurs, la fonction calculate

## Fichiers du module
test_operators.py
Le fichier test_operators.py permet de tester le fonctionnement des 4 opérateurs (add, subtract, multiply et divide)

test_calculate.py
Le fichier test_calculate.py permet de tester le fonctionnement de la fonction calculate utilisée dans app.py

## Exécution des tests
Pour exécuter les tests d'un fichier spécifique, utilisez la commande suivante depuis la racine du projet :

python -m pytest tests/[nom_du_fichier_de_test] -v

Pour exécuter tous les tests du module tests, utilisez :
python -m pytest tests/ -v
L'option -v affiche le résultat détaillé de chaque test.

## Résultats des tests
Les tests permettent de vérifier que chaque opérateur retourne le résultat attendu et de détecter les erreurs de calcul.

Les échecs des tests sont utilisés pour identifier et documenter les bogues dans des Issues GitHub.