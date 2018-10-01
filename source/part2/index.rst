.. _part2:

************************************************************************************************
Partie 2 | Tri et propriétés des ensembles triés
************************************************************************************************

Objectifs
=========

A l'issue de cette partie chaque étudiant sera capable de:

* décrire avec exactitude et précision les concepts présents
  dans le chapitre du livre de référence traitant des *algorithmes de tri*
* mettre en oeuvre et évaluer des algorithmes de tris classiques,
  connaitre leurs avantages, inconvénients et propriétés.

A lire
=======================================

Livre de référence:

* Chapitre 1, section 1: quelques rappels de Java et la programmation en général (partie sur le Binary Search)
* Chapitre 2, section 1: Tris élémentaires
* Chapitre 2, section 2: Tri fusion
* Chapitre 2, section 3: Tri rapide
* Chapitre 2, section 5: Application des tris

Exercices théoriques: première partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S4.

Exercice 2.1.1
""""""""""""""

Etant donné un tableau contenant :math:`n` entiers triés, et un nombre :math:`x` a insérer dans le tableau, pouvez-vous
indiquer un algorithme permettant de trouver la position ou insérer :math:`x` tout en gardant le tableau trié?

Quelle est la complexité de cet algorithme?

Exercice 2.1.2
""""""""""""""

Nous considérons le problème très général où l'on a :math:`n` jobs à accomplir pour des clients
et chaque job :math:`j` demande :math:`t_j` secondes pour l'accomplir.
Un seul job peut être effectué à la fois.

L'objectif est de terminer tous les jobs tout en maximisant la satisfaction des clients.
Maximiser la satisfaction des clients revient à construire un planning qui minimise
le temps de complétion moyen des jobs.

Par exemple, si la durée des jobs est de 5,8,3,4 et que l'on effectue les jobs dans cet ordre,
les temps de fin seront de 5,13,16,20 et donc le temps de fin moyen sera de
:math:`\frac{5+13+16+20}{4}=13.5`.

Prouvez (avec une preuve écrite!) que trier les :math:`n` jobs dans l'ordre croissant des :math:`t_j` génère une solution
optimale au problème.

Exercice 2.1.3
""""""""""""""

Qu'entend-t-on par un algorithme de tri stable et en place (in place)?
Pour tout les algorithmes présentés dans le livre de référence,
indiquez s'ils sont en place (ou pas) ou stable (ou pas).

Exercice 2.1.4
""""""""""""""

Comment trieriez vous un tas de cartes avec la restriction que les
seules opérations permises sont:

1. comparer les deux premières cartes,
2. échanger les deux premières cartes,
3. bouger la première carte à l'arrière du tas?

.. tip::

    Le "Bubble-Sort" est un algorithme de tri qui consiste à comparer de manière
    répétée les éléments consécutifs d'un tableau, et à les permuter lorsqu'ils sont mal
    triés. Cette opération est répétée jusqu'à ce que la liste soit triée.
    Cet algorithme peut éventuellement vous inspirer.

Écrivez le pseudo code de votre algorithme et donnez-en la complexité.

Exercice 2.1.5
""""""""""""""

Comment trier une liste doublement chaînée (qui ne permet donc pas d’accéder
à une position par son indice) efficacement? Quelle est la complexité de votre
algorithme?

Exercice 2.1.6
""""""""""""""

Imaginez un algorithme efficace pour compter le nombre de paires de valeurs désordonnées.
Par exemple dans la séquence :math:`1,3,2,5,6,4,8` il y a les paires :math:`(3,2),(5,4),(6,4)`
qui sont non ordonnées. Justifiez la complexité de votre algorithme et donnez son pseudo code.

.. tip::

    Supposons deux tableaux :math:`A` et :math:`B`, soit :math:`A.B` le tableau résultat de la
    concaténation de :math:`A` et :math:`B`. Soit :math:`nUnsorted(A)` le nombre de paires désordonnées
    dans un tableau :math:`A`.

    Nous avons la propriété suivante que vous pouvez prouvez:

    .. math::

        nUnsorted(A.B) = nUnsorted(A)+ nUnsorted(B)+|\{(i,j) : A[i]>B[j]\}|


    Quelle est la complexité pour calculer :math:`|\{(i,j) : A[i]>B[j]\}|` ?
    Est-ce que cette complexité peut être améliorée si :math:`A` et :math:`B` sont triés?
    Ne pouvez-vous pas calculer :math:`nUnsorted` sur base d'une variante d'un algorithme de tri bien
    connu qui s'exécute en :math:`\mathcal{O}(n \cdot \log(n))`?

Exercice 2.1.7
""""""""""""""

Imaginons que nous souhaitons trier des objets `Person` de manière lexicographique par leur (poids, age, taille)
mais aussi des objets `Student` par leur (age, note, année), comment faire pour ne pas dupliquer l'algorithme de tri
spécifiquement pour ces classes?

Expliquez pourquoi les notions de `Comparable` et `Comparator` de Java sont utiles pour cela?
Expliquez comment vous implémenteriez un `Comparator` efficace pour des `String`.

Exercice 2.1.8
""""""""""""""

Est-il possible d'obtenir un tri stable au départ d'un algorithme de tri non stable? Comment?

Exercice 2.1.9
""""""""""""""

Comment feriez-vous pour obtenir la 3e plus petite valeur dans un tableau d'un millions de int?
Quelle est la complexité de votre algorithme?

Exercice 2.1.10
"""""""""""""""

Comment feriez-vous pour obtenir la médiane d'un tableau de valeur (donc la :math:`\frac{n}{2}` ième valeur) ?
Quelle est la complexité de votre algorithme?

.. tip::

    Que pouvez-vous déduire concernant la position de la médiane après l'opération de partitionnement
    autour d'une valeur :math:`v` dans l'algorithme Quick-Sort?

Exercice 2.1.11
"""""""""""""""

Qu'est-ce que le Autoboxing and Unboxing en Java?
En quoi est-ce que cela peut impacter les performance d'un algorithme de tri?

Comparer les performance de `java.util.Sort` sur un tableau de 10000000 entrées composé de `int` et
le même tableau avec des `Integer`.

Exercice 2.1.12
"""""""""""""""

Qu'est-ce qu'un *profiler* de code?
Quelles informations fournies par un profiler pourriez-vous utiliser pour améliorer les
performances de votre algorithmes et structures de données de manière générale (vitesse, mémoire, GC)?

Un bon profiler gratuit est VisualVM.

Utilisez VisualVM sur votre code pour la question précédente.

Exercices d'implémentation sur Inginious
==========================================

.. note::
   Vous devez faire ces exercices pour le lundi de S5.

Les exercices seront publiés le lundi de S4.

Exercices théorique: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le lundi de S5.

Les exercices seront publiés le lundi de S4.