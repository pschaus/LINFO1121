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

* `Introduction <https://www.icloud.com/keynote/060axAx-WvIieFjqV9nvebAoQ#part4-intro>`_ 
* `Séance Intermédiaire <https://www.icloud.com/keynote/0TixMvOD8GNdrZKROHyYUiXfw#part4-bilan>`_ 
* `Restructuration <https://www.icloud.com/keynote/0LwjcO8rozlr-a4jzmTvWMNww#part-4-bilan>`_ 

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

Expliquez pourquoi la méthode `hash()` p461 du livre retourne `(x.hashCode() \& 0x7FFFFFFF) \% M` et pas simplement `x.hashCode() \% M` ?  
Quel nombre représente `0x7FFFFFFF` ? 
Quelle est sa représentation binaire ? 
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
Est-ce que le contrôle du facteur de charge est nécessaire/optionnel pour le bon fonctionnement d'une table de hachage avec Linear Probing ou Separate Chaining ?
Quelle est la stratégie utilisé par `java.util.Hashtable` pour contrôler le facteur de charge ? 
En quoi est-elle différente de celle proposée dans`LinearProbinHashST` ?
Quel est le lien entre le facteur de charge et collision ?

Exercice 4.1.7
""""""""""""""

Imaginez une nouvelle méthode `iterator()` qui retourne un itérateur sur les clefs de `LinearProbingHashST`. 
Votre itérateur ne devrait pas accepter de modification de la table de hashage alors qu'il est utilisé: une `ConcurrentModificationException()` doit être lancée si c'est le cas. 
Que suggérez vous pour ce faire? Hint: Inspirez vous de la stratégie de `java.util.Hashtable`.


Exercice 4.1.8
""""""""""""""

Décrivez l'implémentation  de la méthode `put(key)` dans une table de hachage qui utilise la technique du "linear probing" pour gérer les collisions qui utiliserait un marqueur spécial pour représenter les entrées supprimées à l'aide de la méthode `delete(key)`. 
En d'autres termes la méthode `delete(key)` au lieu de réarranger le contenu de la table de hachage de telle sorte qu'elle soit comme si l'entrée supprimée n'avait jamais été insérée, va simplement marquer l'entrée avec le marqueur spécial.
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


1. `QCM fonction de hachage <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part4QcmHashing>`_
2. `QCM Complexité RabinKarp <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part4QcmRk>`_ 
3. `Implem Fonction de Hash incémentale <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part4IncrementalHash>`_
4. `Implem RabinKarp K patterns <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part4RabinKarp>`_

Exercices théorique: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S10.

Les exercices seront publiés le lundi de S9.

Exercice 4.2.1 (Hash des Long and Double)
"""""""""""""""""""""""""""""""""""""""""""""

Voici la formule utilisée par Java pour calculer une fonction de hachage 
sur les doubles (bits est un tableau de 64 bit représenté sous forme de long): 
`return (int) bits ^ (bits >>> 32)`

* Pourquoi ne pas simplement utiliser `(int) bits` (casting de long vers int) ? Indice: Le livre de référence suggère qu'une bonne fonction de hachage doit utiliser tous les bits pour son calcul. Pourquoi ? 
* Un double en Java est représenté en 64 bits sous la forme :math:`(-1)^s \times m \times 2^{(e - 1023)}`. Le premier bit :math:`s` est le signe, les 11 bits suivants représentent l'exposant sous forme binaire et les 52 derniers bits représentent la mantisse (partie décimale) sous forme binaire.  Est-ce qu'un nombre décimal positif et son opposé obtiennent des fonctions de hachage différentes ? 



Exercice 4.2.2 (Hash des int castés)
"""""""""""""""""""""""""""""""""""""""""""""


* Est-ce que la fonction de hachage d'un entier sur 32 bits et celle de ce même entier qui serait casté en double sont les mêmes ? 
* Est-ce que la fonction de hachage d'un entier sur 32 bits et celle de ce même entier qui serait casté en long sont les mêmes ?  Hint: `Long.toBinaryString( Double.doubleToRawLongBits(a))` permet d'afficher le tableau de bits utilisé pour la représentation d'un double.


Exercice 4.2.3 (Hash de String: le choix de M et R)
""""""""""""""""""""""""""""""""""""""""""""""""""""


La fonction de hachage pour un string donné tel que présenté dans le livre p460 est la suivante:

.. code-block:: java
   :linenos:

	int hash = 0;
	for (int i = 0; i < s.length(); i++)
		hash = (R * hash + s.charAt(i)) % M;


Dans l'implémentation du livre, la taille de :math:`M` (le tableau) est une puissance de deux.
La valeur suggérée pour :math:`R` est *un petit nombre premier tel que 31 de sorte que les bits de tous les caractères jouent un rôle.*

* Supposons que :math:`R` soit un multiple de :math:`M`. Que se passerait-il lors du calcul ? 
* Supposons que :math:`R` est un nombre pair. Que se passerait-il ?
* Dans les deux cas, combien d'entrées du string détermineront effectivement le code de hachage ? Quels sont les risques en termes de collision? Est-ce que le contrôle du facteur de charge peut résoudre le problème ? Expliquez pourquoi utiliser 31 est un choix judicieux pour des tailles de tableau qui sont des puissances de deux ? Serait-ce aussi un bon choix pour une taille de tableau qui commencerait à 31 et qui serait multipliée par deux à chaque fois qu'il faut redimensionner ?
* Dans l'implémentation du livre la taille de M (le tableau) est une puissance de deux initialisée à 16. Supposons qu'à moment donné la taille de :math:`M` soit :math:`2^8=256`. Ensuite deux clefs entières sont ajoutées dans une table de hachage implémentée avec separate chaining: respectivement :math:`2560` et :math:`3072` (on suppose que ces ajouts ne causent pas de redimensionnement de la table). Comme vous le savez, le code de hachage d'une clef entière (int) est le nombre lui-même.
Est-ce que l'ajout de ces deux valeurs va causer une collision entre elles dans la table ? Si oui pourquoi ? 
Si oui pouvez-vous proposer une troisième valeur qui va aussi entrer en collision ? 
Si collision il y a, peut-elle disparaître lors du prochain redimensionnement du tableau telle que dans l'implémentation du livre ?
* Que suggérez-vous pour éviter ce problème ? Quelle a la politique d'initialisation de :math:`M` et de redimensionnement utilisée dans `java.util.HashMap` ? Est-ce que cela résout le problème sur notre exemple ?


Exercice 4.2.4 (Création de Hash: Véhicules)
"""""""""""""""""""""""""""""""""""""""""""""

* Que suggèreriez-vous comme fonction de hachage pour l'identification de véhicules qui sont des strings de nombres et de lettres de la forme: "9X9XX99X9XX999999" où un 9 représente un chiffre et un "X" une lettre de A à Z. 
* Est-ce que votre fonction de hachage a la propriété que pour une taille de tableau N hypothétique de :math:`10^{11} \cdot 26^6` je n'ai jamais de collision 


Exercice 4.2.5 (Création de Hash: Citoyens)
"""""""""""""""""""""""""""""""""""""""""""""

Imaginons que l'on cherche à construire un répertoire des citoyens belges
et que l'on veuille pouvoir accéder à chaque citoyen par son numéro de carte d'identité
(12 chiffres). 
On peut donc considérer ce numéro comme la clé unique identifiant
chaque citoyen et utiliser cette clé comme l'indice dans un tableau (array en Java).
A chaque indice correspondrait une référence vers une instance de la classe 
`Citoyen` dont les champs constituent les informations que l'on désire mémoriser pour chacun.
Quelle est la complexité temporelle des opérations suivantes ?

* rechercher les informations relatives à un citoyen à partir de son numéro de carte
  d'identité.
* ajouter un nouveau citoyen.

Cette implémentation d'un dictionnaire n'est-elle pas encore meilleure qu'une table de hachage ? 
Peut-on avoir un problème de collision dans ce cas ? Justifiez.