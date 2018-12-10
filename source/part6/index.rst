.. _part6:

************************************************************************************************
Partie 6 | Graphes: parcours, arbres sous-tendants, et plus courts chemins
************************************************************************************************

Objectifs
=========

À l'issue de cette partie, chaque étudiant sera capable de:

* de *décrire* avec exactitude et précision les concepts présents au chapitre du livre de référence qui traite de *graphes*,
* d'*évaluer* et *mettre en oeuvre* des représentations classiques de graphes,
* de *choisir* une représentation adéquate d'un graphe en fonction des opérations à effectuer sur ce graphe,
* de *mettre* en oeuvre des algorithmes de parcours et manipulation de graphes, en particulier
    * depth et breadth first search:
        * calcul de composantes connexes (le calcul des composantes fortement connexes ne fait pas partie de la matière)
        * détection de cycle
        * tri topologique
    * calcul d'arbres sous tendant de poids minimum (Kruskal et Prim)
    *  calcul de plus courts chemins (Dijkstra, Bellman-Ford)


A lire
=======================================

Livre de référence:

* chapitres 4.1, 4.2, 4.3, 4.4



Slides (keynote)

* `Introduction <https://www.icloud.com/keynote/0ICOAb5mCaM2Uexx64Vc5Vpaw#part6-intro>`_ 
* `Séance Intermédiaire <Nope>`_ 
* `Restructuration <Nope>`_ 


Exercices théoriques: première partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S13.

Exercice 6.1.1
""""""""""""""

Donnez plusieurs structures de données pouvant être utilisées pour représenter un graphe :math:`G` non dirigé
comportant :math:`n` noeuds (vertex) et :math:`m` arcs (edges).

Quelles sont les complexités des opérations élémentaires `Iterable<Integer> adj(int v)` et `addEdge(int v, int w)`?

Exercice 6.1.2
""""""""""""""

Un graphe est biparti si ses noeuds peuvent être divisés en deux ensembles disjoints de sorte qu'il n'existe pas d'arc
entre deux noeuds du même ensemble.

Proposez une méthode pour tester si un graphe est biparti et si oui qui trouverait une telle partition.
Quelle est la complexité de votre algorithme? Hint: utilisez un DFS.

Exercice 6.1.3
""""""""""""""

Prouvez que tout graphe connecté a un noeud dont le retrait (y compris des arcs incidents) ne déconnecterait pas le graphe.
Ecrivez une méthode qui trouve un tel noeud. Hint: utilisez un DFS et le marquage des noeuds.

Exercice 6.1.4
""""""""""""""

Soit un graphe :math:`G` non dirigé et sans poids dont les arcs représentent les déplacements élémentaires possibles d'un robot dans un labyrinthe au départ de toutes les positions possibles (noeuds). Etant donné la position courante et un noeud qui représente la sortie. Proposez une méthode pour trouver un chemin vers la sortie et qui minimise le nombre de déplacements élémentaires.
Quelle est la complexité de votre méthode? Est-ce que cela dépend de l'implémentation du graphe (par exemple si c'est une matrice d'adjacence?)

Exercice 6.1.5
""""""""""""""

Le programme des cours de l'EPL donne pour chaque cours la liste des pré-requis de ces cours.
Vous souhaitez vous assurer que tous les cours peuvent être pris c'est à dire qu'il n'existe pas de dépendance
cyclique entre les cours.

Quelle méthode proposez-vous pour réaliser ce test?
Quelle en est la complexité?

Exercice 6.1.6
""""""""""""""

Développez un algorithme de tri topologique (écrivez le code) qui maintient un tableau de la taille du nombre de
noeud dont chaque entrée correspond au degré entrant de chaque noeud (in-degree).
Votre algorithme maintient également une queue des *sources* (noeuds avec un in-degree de 0).
Initialisez ces deux structures en une seule passe sur toutes les edges.
Ensuite réalisez les opérations suivantes jusqu'à ce que la queue des sources devienne vide:

* retirez une source de la queue et marquez la.
* décrémentez les in-degree des destinations adjacentes du noeud marqué à l'étape précédente.
* si le in-degree d'un noeud devient 0, il faut l'insérer dans la queue des sources.

Est-il-possible au passage de détecter si le tri topologique est unique? Quelle est la complexité de votre algorithme?

Exercice 6.1.7
""""""""""""""

Soit :math:`G(V,E)` un graphe non dirigé avec poids sur lequel a été calculé un minimum spanning tree.
Ensuite :math:`k` arcs ont été retirés aléatoirement de ce MST.
Écrivez une méthode pour retrouver un MST au départ du MST partiel.
Le MST final ne doit pas nécessairement être identique à l'original, seuls les :math:`V-1-k` arcs restants doivent
au minimum s'y trouver.

Sur quelle(s) propriété(s) importante(s) des MST se base votre algorithme?
Quelle est la complexité de votre méthode?

Exercice 6.1.8
""""""""""""""

Soit :math:`G(V,E)` un graphe non dirigé avec poids sur lequel a été calculé un minimum spanning tree.
L'edge :math:`e \in E` de poids :math:`w` ne fait pas partie de ce MST.
Pouvez-vous recalculer un MST qui inclurait :math:`e` en adaptant le MST de départ? Décrivez votre algorithme (code).
Quelle en est la complexité? Hint: DFS sur le MST de départ.

Exercice 6.1.9
""""""""""""""

Est-ce que `java.util.PriorityQueue` pourrait être utilisée pour implémenter efficacement Dijkstra?
Si-non pourquoi? Que serait la complexité si on souhait utiliser cette file de priorité?

Exercice 6.1.10
"""""""""""""""

Expliquez pourquoi DijkstraSP ne permet pas de gérer les arcs avec un poids négatif?
Est-ce que le résultat serait faux ou est-ce que la complexité ne serait plus garantie?
Montrez un exemple d'input qui illustre le problème.

Hint: est-qu'un noeud peut être ajouté plusieurs fois dans la priority queue durant une relaxation?

Exercice 6.1.11
"""""""""""""""

Soit :math:`G` un graphe avec des poids potentiellement négatif mais il n'y a pas de cycle négatif.
Je cherche le chemin le plus court entre un noeud :math:`u` et un noeuds :math:`v`.
J'ai à ma disposition une implémentation de Dijkstra qui ne permet pas de gérer les poids négatifs.
Il me suffit dès lors d'augmenter tous les poids d'une même quantité correspondant a la valeur absolue du plus petit
poids et d'appliquer Dijkstra sur ce graphe.
Cette méthode est-elle valable?
Si oui, prouvez le.
Si non, montrez un contre exemple.

Exercice 6.1.12
"""""""""""""""

Soit :math:`G` un graphe avec des poids positifs. Je cherche le chemin le plus long entre un noeud :math:`u` et un noeuds :math:`v`. J'ai à ma disposition l'implémentation de Bellman-Ford (qui supporte les poids négatifs). Il me suffit dès lors de calculer le plus court chemin sur le même graphe avec l'opposé des poids. Est-ce que cette méthode est valable? Si non pouvez-vous proposer une méthode pour le calcul de plus long chemin? Votre méthode s'applique-t-elle à tous les graphes? Si non quels-types particuliers de graphes peut-elle gérer?

Exercices d'implémentation sur Inginious
==========================================

.. note::
   Vous devez faire ces exercices pour le lundi de S14.

Les exercices seront publiés le lundi de S13.

Exercices théoriques: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S14.


Exercice 6.2.1 (Labyrinthe.)
"""""""""""""""""""""""""""""""""""""""""""""

On s'intéresse à la résolution d'un labyrinthe représenté sous la forme d'une matrice binaire :math:`n \times m`.
Cette matrice n'est rien d'autre q'un tableau à deux dimensions de booleans.
Une position égale à *true* signifie que celle-ci est disponible, alors que *false* 
indique qu'il y a un mur et que vous ne pouvez transiter par cette position.
Ecrivez un fragment de code Java (classes, méthodes, etc.) pour trouver **le plus court chemin**
entre deux coordonnées *(x1,y1)* et *(x2,y2)* supposées disponibles, 
Les déplacements ne peuvent se faire qu'horizontalement ou verticalement et d'une seule position à la fois.
Votre résultat doit être retourné sous la forme d'un iterable de coordonnées depuis l'origine vers la destination.
Les coordonnées sont représentées par des entiers compris entre :math:`0` et :math:`n\cdot m-1`.
L'entier :math:`a` représente la coordonnée :math:`(a/m,$a \% m)`.
La signature de votre méthode est donc:

.. code-block:: java

	Iterable<Integer> shortestPath(boolean[][] maze, int x1, int y1, int x2, int y2);




Questions préliminaires:


* Quel algorithme permet de trouver le plus court chemin entre deux noeuds sur un graphe sans poids ?
* Est-ce qu'une structure de données de type Graph est nécessaire pour implémenter votre algorithme ? Si oui laquelle ? Si non pourquoi ?
* Quelle est la complexité de votre algorithme worst/best case ?


Exercice 6.2.2 (Dijkstra revisité)
"""""""""""""""""""""""""""""""""""""""""""""

On s’intéresse à l’implémentation de l’algorithme de Dijkstra p655. 


* Quelle est la complexité de cet algorithme. 
* Réécrivez cet algorithme en utilisant uniquement des collections auxiliaires issues de *java.util*.  Il faut donc se débarrasser de *IndexMinPQ* et remplacer cette structure par autre chose issu de *java.util*.


Exercice 6.2.3 (La Guirlande de Noël INGI)
"""""""""""""""""""""""""""""""""""""""""""""

Le département INGI s’est doté d’une très jolie guirlande de Noël pour décorer le Réaumur.
Celle-ci a la structure d’un graphe avec une lampe sur chaque noeud.
Lorsqu’on allume la guirlande, une lampe s’allume au hasard et puis chaque seconde, toutes les lampes directement reliées (sur les noeuds adjacents) s’allument à leur tour. 
Implémentez la méthode « minTime » répondant à la question suivante:
*Au bout de combien de secondes* **au minimum** *notre guirlande pourrait-elle être complètement allumée ?*

Voici la signature de la méthode:

.. code-block:: java

	public int minTime(Graph G); 


Vous pouvez supposer que vous disposez de l’API de la structure Graph telle que décrite dans le livre.
On suppose que le graph G est connexe.

* Quelle est la complexité temporelle de votre algorithme ?
 


