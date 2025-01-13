#!/usr/bin/python3
import sys

# Description de la fonction :
# Cette fonction calcule le factoriel d'un nombre n donné.
# Le factoriel d'un nombre n (noté n!) est le produit de tous les entiers de 1 à n.
# Par exemple : 5! = 5 * 4 * 3 * 2 * 1 = 120.

# Paramètres :
# n (int) : Le nombre pour lequel on souhaite calculer le factoriel.

# Retour :
# int : Le résultat du factoriel de n.
def factorial(n):
    if n == 0:
        return 1  # Le factoriel de 0 est défini comme étant égal à 1.
    else:
        return n * factorial(n-1)  # Appel récursif pour calculer le factoriel.

# Récupère le premier argument passé en ligne de commande
# et le convertit en entier. Puis, on appelle la fonction factorial.
f = factorial(int(sys.argv[1]))

# Affiche le résultat du calcul du factoriel.
print(f)