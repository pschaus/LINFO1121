.. _part4:

************************************************************************************************
Partie 4 | Dictionnaires: tables de hachages et autres implémentations
************************************************************************************************

Objectifs
=========

À l'issue de cette partie, chaque étudiant sera capable de:

* décrire avec exactitude et précision les concepts présents dans le chapitre du livre de référence, qui traite de tables de hachage
* mettre en oeuvre des algorithmes basés sur les tables de hachage, 
* concevoir des fonctions de hachage adéquates pour différents types d'objets,
* de résoudre des problèmes simples sur la mémorisation d'informations et leur accès dans des tables de hachage,
* d'évaluer et mettre en oeuvre des représentations classiques de tables de hachage,
* décrire et mettre en oeuvre avec précision l'algorithme de Rabin-Karp pour rechercher un texte dans un corpus.


A lire
=======================================

Livre de référence:

* chapitre 3.4, 3.5, 5.3 (Rabin-Karp fingerprint search only). 


Slides (keynote)

* `Introduction <Nope>`_ 
* `Séance Intermédiaire <Nope>`_ 
* `Restructuration <Nope>`_ 

Exercices théoriques: première partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S9.

Exercice 4.1.1
""""""""""""""

Souvenez vous de la question suivante proposée en bilan sur la mission sur les tris: Étant donné un ensemble :math:`S` de taille :math:`n`, et un nombre :math:`x`. Décrivez un algorithme efficace utilisant une HashTable pour trouver s'il existe une paire :math:`(a,b)` avec :math:`a \in S,b \in S` telle que :math:`a+b=x`. Quelle est la complexité de votre algorithme? Est-elle meilleure que votre solution qui utilisait un tri?

Exercice 4.1.2
""""""""""""""

Démontrez que :math:`(a + b) \% M` est équivalent à :math:`((a \% M) + b) \% M`. En quoi cette propriété peut être utile pour construire une fonction de hachage sur les String. 
Expliquez comment Java calcule une fonction de hachage sur les String? 
Quelle est la complexité pour calculer 1 fois et :math:`N` fois le hashcode d'un String. 


Exercice 4.1.3
""""""""""""""

Expliquez pourquoi la méthode `hash()` p461 du livre retourne `(x.hashCode() \& 0x7FFFFFFF) \% M` et pas simplement `x.hashCode() \% M`?  
Quel nombre représente `0x7FFFFFFF`? 
Quelle est sa représentation binaire? 
Montrer l'impact au niveau binaire sur un exemple où `x.hashCode()` retourne un nombre négatif. H
int: utilisez `Integer.toBinaryString(int)` pour vérifier votre réponse. 


Exercice 4.1.4
""""""""""""""

Java fournit la classe `java.util.Hashtable` comme implémentation de l'interface `java.util.Map`. 
Pouvez-vous déterminer précisément de quelle variante de table de hachage il s'agit ? 
Java fournit-il d'autres implémentations de l'interface `Map` ? 
Faites un diagramme qui représente  les interfaces et les classes qui se rapportent à `Map` et précisez ce qui, dans chaque cas, les caractérise. 
Qu'est-ce qui peut servir de clef pour une `Hashtable` en Java ? Soyez précis.

Exercice 4.1.5
""""""""""""""

Qu'entend-on par la notion de "collision" dans une table de hachage ? 
Les collisions ont-elles une influence sur la complexité des opérations ? 
Si oui, quelle(s) opération(s) avec quelle(s) complexité(s), sinon précisez pourquoi.

Exercice 4.1.6
""""""""""""""

Qu'est-ce que le facteur de charge d'une table de hachage. 
Est-ce que le contrôle du facteur de charge est nécessaire/optionnel pour le bon fonctionnement d'une table de hachage avec Linear Probing ou Separate Chaining?
Quelle est la stratégie utilisé par `java.util.Hashtable` pour contrôler le facteur de charge ? 
En quoi est-elle différente de celle proposée dans`LinearProbinHashST`?
Quel est le lien entre le facteur de charge et collision ?

Exercice 4.1.7
""""""""""""""

Imaginez une nouvelle méthode `iterator()` qui retourne un itérateur sur les clefs de `LinearProbingHashST`. 
Votre itérateur ne devrait pas accepter de modification de la table de hashage alors qu'il est utilisé: une `ConcurrentModificationException()` doit être lancée si c'est le cas. 
Que suggérez vous pour ce faire? Hint: Inspirez vous de la stratégie de `java.util.Hashtable`.


Exercice 4.1.8
""""""""""""""

Décrivez l'implémentation  de la méthode `put(key)` dans une table de hachage qui utilise la technique du "linear probing" pour gérer les collisions qui utiliserait un marqueur spécial pour représenter les entrées supprimées à l'aide de la méthode "delete(key)". 
En d'autres termes la méthode "delete(key)" au lieu de réarranger le contenu de la table de hachage de telle sorte qu'elle soit comme si l'entrée supprimée n'avait jamais été insérée, va simplement marquer l'entrée avec le marqueur spécial.
Quel est l'avantage ou l'inconvénient de cette approche par rapport à celle de "LinearProbingHashST" du livre ?


Exercice 4.1.9 (Rabin-Karp)
""""""""""""""""""""""""""""

Imaginez une fonction de hachage pour un string :math:`s` telle que connaître sa valeur pour le sous string :math:`s[i,...,i+n-1]` permettrait de calculer la fonction de hachage du string :math:`s[i+1,...,i+n]` en temps constant (de manière incrémentale). 

Exercice 4.1.10 (Rabin-Karp)
""""""""""""""""""""""""""""

Expliquez comment rechercher un sous string de taille :math:`M` dans un long string de taille :math:`N` en :math:`O(N)` à l'aide d'une fonction de hachage incrémentale. 
Comment feriez-vous si vous avez :math:`k` strings de taille :math:`M` à rechercher dans le long string de taille :math:`N` ? 
Quelle serait la complexité de votre méthode ? est-elle plus avantageuse que lancer k fois l'algorithme de Rabin-Karp ? 




Exercices d'implémentation sur Inginious
==========================================

.. note::
   Vous devez faire ces exercices pour le lundi de S10.

Les exercices seront publiés le lundi de S9.

Exercices théorique: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S10.

Les exercices seront publiés le lundi de S9.