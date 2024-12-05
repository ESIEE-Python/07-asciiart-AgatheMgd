"""
Plusieurs fonctions pour calculer le nombre d'itération d'un même caractère
à la suite dans une chaine de caractère avec une méthode récursive et itérative.
"""

#### Imports et définition des variables globales

import sys
sys.setrecursionlimit(1500)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    liste = []
    nmbr = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            nmbr +=1
        else :
            liste.append((s[i-1],nmbr))
            nmbr = 1
    liste.append((s[-1],nmbr))

    return liste

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s :
        return []

    nmbr = 1
    i = 1
    while i < len(s) and s[0] == s[i]:
        nmbr += 1
        i += 1
    return [(s[0], nmbr)] + artcode_r(s[i:])

#### Fonction principale


def main():
    """ Renvoie le nombre d'occurence de deux différentes chaines 
    de caractères avec la fonction itérative et non itérative
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

    print(artcode_i('dddddddTTTTTTT---------GGGG'))
    print(artcode_r('dddddddTTTTTTT---------GGGG'))

if __name__ == "__main__":
    main()
