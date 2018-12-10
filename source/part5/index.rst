.. _part5:

************************************************************************************************
Partie 5 | Files de priorités, union-find et compression de données
************************************************************************************************


Objectifs
=========

À l'issue de cette partie, chaque étudiant sera capable de:

* de décrire avec exactitude et précision les concepts présentés dans le livre de référence et qui traitent de *structures union-find*,  *files de priorité* et  de manipulation/compression de données textuelles,
* de *mettre en oeuvre* un algorithme de compression de texte basé sur un codage de Huffman,
* *évaluer* et *mettre en oeuvre* une représentation efficace  d'une file de priorité sur base d'un *tas* (Heap, en anglais),
* de *concevoir* et *implémenter* un programme de compression/décompression de texte.


A lire
=======================================

Livre de référence:

* chapitre 1.5 (union find), 2.4 (heap), 5.5 (Huffman compression).


Slides (keynote)

* `Introduction <https://www.icloud.com/keynote/0kZvMH6djI5t45YFxQ2xzSfog#part5-intro>`_ 
* `Séance Intermédiaire <https://www.icloud.com/keynote/0CjZEjoEFtp6VH7XyVSlWLXGQ#part5-exerises>`_ 
* `Restructuration <https://www.icloud.com/keynote/0TR23WOD7cI2jGI9oH3KVOocQ#part5-bilan>`_ 


Exercices théoriques: première partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S11.

Exercice 5.1.1
""""""""""""""

Donnez le tableau `id[]` qui résulte de la séquence suivante de 6 opérations d'union sur un ensemble de départ de 10 items avec l'algorithme quick-find.
`3-8, 1-7, 1-8, 9-4, 6-4, 2-0`. 
Votre réponse doit être une séquence de 10 entiers. 
Rappel: la convention quick-find pour l'union `p-q` est de changer `id[p]` (et éventuellement d'autres entrées) mais pas `id[q]`.


Exercice 5.1.2
""""""""""""""

Donnez le tableau id[] qui résulte de la séquence suivante de 9 opérations d'union sur un ensemble de 10 items en utilisant l'algorithme weighted quick-union:
	`4-6, 3-6, 8-9, 7-0, 1-2, 8-4, 6-5, 1-7, 6-0.` 
Votre réponse doit être une séquence de 10 entiers. Rappel: Lors de la fusion de deux arbres de même taille, l'algorithme weighted quick-union utilise la convention
de faire pointer la racine du second arbre vers la racine du premier arbre. 
Notre algorithme utilise l'union par la taille (nombre de noeuds) et pas l'union par la hauteur, ni la technique de compression de chemin.

Exercice 5.1.3
""""""""""""""

Le(s)quel(s) tableau(x) id[] suivant(s) pourrai(en)t résulter de l'application de l'algorithme weighted quick-union sur un ensemble de 10 items au départ?
Rappel: nous utilisons l'union par la taille (nombre de noeuds) et pas l'union par la hauteur.

* 0 8 2 3 4 7 6 8 8 9
* 4 2 6 6 2 6 6 2 4 2
* 7 0 0 0 0 1 0 5 1 0
* 3 3 0 3 0 3 3 3 5 2
* 1 3 3 6 4 1 6 0 6 8

Exercice 5.1.4
""""""""""""""

Donnez la séquence des clefs dans le tableau qui résulte de l'insertion de la séquence des 3 clefs 48, 30 et 84 
dans la heap suivante (orientée vers le maximum) de taille 10:
	`97 , 93 , 89 , 83 , 38 , 32 , 40 , 12 , 26 , 24`.
Votre réponse devrait être une séquence de 13 entiers.

Exercice 5.1.5
""""""""""""""

Donnez la séquence des clefs dans le tableau qui résulte de l'ajout de 3 opérations successives de suppression du maximum dans la heap suivante (orientée vers le maximum)
de taille 10: 
	`98 , 96 , 84 , 34 , 62 , 31 , 72 , 13 , 27 , 33`.
Votre réponse devrait être une séquence de 7 entiers.


Exercice 5.1.6
""""""""""""""""

Quels sont les avantages et inconvénients éventuels d'implémenter une file de
priorité par un heap plutôt que par une liste ?


Exercice 5.1.7
""""""""""""""

Existe-t-il un tas T mémorisant 7 éléments distincts tel qu'un parcours 
infixe du tas renvoie les éléments de T en ordre décroissant ? 
Qu'en est-il avec un parcours préfixe ou post-fixe ?


Exercice 5.1.8
""""""""""""""

Quelles déclarations suivantes sont vraies à propos d'une file de priorité implémentée par une heap? Par défaut les heaps sont orientées maximum et utilisent une base d'indice commençant à 1.

* Dans le pire cas, l'insertion d'une clef dans une heap binaire contenant N clefs nécessite :math:`\sim lg N` comparaisons.
* Soit :math:`a[]` un tableau tel que :math:`a[1] > a[2] > \ldots > a[N]` (et :math:`a[0]` est vide). Alors :math:`a[]` satisfait les propriétés d'une heap binaire.
* Le tableau d'une heap est toujours un tableau trié dans l'ordre décroissant.
* Étant donné une heap binaire de N clefs distinctes, supprimer la clef maximum et ensuite l'insérer directement laisse le tableau de la heap inchangé (on ignore les redimensionnements possibles du tableau) .


Exercice 5.1.9
""""""""""""""

Exercise 2.4.20 Prouver que la construction bottom-up "sink" d'une heap pour le Heapsort (p323) se fait en :math:`O(N)`. 
Indice: comptez le nombre de noeuds au niveau :math:`h` de la heap. 
Quelle est la complexité d'un sink à ce niveau. Faites la somme pour tous les niveaux. Formule utile: :math:`\sum_{k=0}^\infty k x^k = x/(1-x)^2` pour 
:math:`|x| < 1`.


Exercice 5.1.10
""""""""""""""""

L'utilisation d'une file de priorité est-elle indispensable 
pour pouvoir construire un code de Huffman ? Pouvez-vous imaginer
une autre solution en utilisant un algorithme de tri ? Sa complexité calculatoire serait-elle meilleure que l'algorithme original ? Pourquoi ?


Exercice 5.1.11
""""""""""""""""

* Quelles sont les différentes étapes d'un algorithme de compression de texte qui prend en entrée un texte et fournit en sortie une version comprimée de ce texte à l'aide d'un codage de Huffman ? Soyez précis dans votre description en isolant chaque étape du problème. Précisez notamment pour chaque étape les structures de données utiles et la complexité temporelle des opérations menées.  
* Quelles sont les différentes étapes d'un algorithme de décompression de texte qui prend en entrée une version comprimée d'un texte à l'aide d'un codage de Huffman et fournit en sortie le texte original ? Soyez précis dans votre description en isolant chaque étape du problème. Précisez notamment pour chaque étape les structures de données utiles et la complexité temporelle des opérations menées.  




Exercices d'implémentation sur Inginious
==========================================

.. note::
   Vous devez faire ces exercices pour le lundi de S12.


1. `Exercices sur les heap <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part5Heap>`_
2. `Exercices sur le UnionFind <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part5UnionFind>`_ 
3. `Implem Huffman <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part5Huffman>`_
4. `Implem UnionFind appliqué <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part5GlobalWarming>`_
5. `Implem Heap push <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/PART5BinaryHeapPush>`_



Exercices théoriques: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S12.

Exercice 5.2.1
""""""""""""""
Dans la technique de compression par un codage de Huffman, il s'avère utile
d'inclure dans le fichier comprimé une entête contenant l'information nécessaire au décodage
de ce fichier. Dans votre implémentation, l'entête est probablement une version sérialisée 
de l'arbre (résultat d'un parcourt préfixe) tel que proposé dans le livre.
Pensez-vous qu'il serait plus ou moins intéressant d'un point de vue mémoire de stoker pour chaque symbole, son codage binaire
plutôt que l'arbre sérialisé ? 

Exercice 5.2.2
""""""""""""""

Peut-on gagner encore en taux de compression si l'on réapplique
l'algorithme de compression de Huffman sur un fichier déjà comprimé une première fois ?
Que se passe-t-il dans ce cas ?
Cela ouvre-t-il la porte vers un algorithme de compression récursif et optimal ? 

Exercice 5.2.3
""""""""""""""

Quel est, approximativement, le taux de compression obtenu si l'on applique l'algorithme 
de compression de Huffman sur un un fichier comportant une seule chaîne composée du caractère 'a' répété un million (:math:`\approx 2^{20}`) de fois, suivi du caractère `b` présent une seule fois ? 
Le taux de compression obtenu varie-t-il avec la longueur du fichier  (par exemple, si le caractère `a` est répété deux millions de fois) ? 
A votre avis, quel est le nombre minimal de bits nécessaires pour représenter sous forme comprimée  ce fichier ?
Peut-on adapter la technique de compression par un codage de Huffman en mesurant 
la fréquence d'autre chose que les caractères présents ? Peut-on utiliser une autre technique
de compression qui serait plus efficace dans ce cas particulier ?


Exercice 5.2.4
""""""""""""""

maginez une implémentation d'une file de priorité par un tas (heap, en anglais) à l'aide d'une structure chaînée pour représenter l'arbre binaire essentiellement complet correspondant au tas. 
Combien de liens sont nécessaires dans chaque noeud ?
Écrivez le code des méthodes *insert*, *delMax*. Quelle en est la complexité ? Est-il utile de donner la taille *max N* dans le constructeur ?
Comment faites-vous pour ajouter un nouveau noeuds dans la heap ou retirer le prochain noeud ? Est-ce que cela peut être fait au départ de la taille courante de la heap ?


Exercice 5.2.5
""""""""""""""

Proposez une structure de données qui supporterait les opérations suivantes en temps logarithmique: *insertion*, *supprimer le maximum*, *supprimer le minimum*; 
et les opérations suivantes en temps constant: *trouver le maximum et le minimum*.
Pour cela, nous vous proposons d'étudier la propriété suivante appelée min-max heap.
Les niveaux pairs sont: 0 (racine), 2, 4, etc. 
Ces niveaux pairs sont aussi appelés les niveau :math:`min`.
Les niveaux impairs sont 1, 3, 5, etc. 
Les niveaux impairs sont aussi appelés les niveaux :math:`max`.
Pour n'importe quel élément :math:`x` dans la min-max heap on a la propriété suivante:

*  Si :math:`x` est à un niveau  :math:`min`, tous les descendants de :math:`x` sont supérieurs à :math:`x`.
*  Si :math:`x` est à un niveau :math:`max`, tous les descendants de :math:`x` sont inférieurs à :math:`x`.


Questions:

* D'après cette propriété déterminez quel est le plus petit élement de la heap ?
* Quel est le plus grand élément de la heap ?
* Dessinez une min-max heap qui contient les éléments suivants: 10,8,71,31,41,46,51,31,21,11,16,13.
* Décrivez l'opération d'insertion dans une min-max heap? Donnez le pseudo-code.

Exercice 5.2.6
""""""""""""""

Imaginez une structure de données qui supporte 

1. l'*insertion* en temps logarithmique
2. l'opération *trouver la médiane* en temps constant 
3. *supprimer la médiane* en temps logarithmique.
