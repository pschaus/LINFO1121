.. _part1complexity:


*************************************************************************************************
Complexités
*************************************************************************************************

Veuillez noter que toutes les définitions sont ici pour des fonctions positives à un argument entier, mais sont quasiment identiques
pour les fonctions à plusieurs variables venant d'autres ensembles.

Notation Big-Oh (:math:`\mathcal{O}`)
=====================================

.. math::

    f(n) \in \mathcal{O}(g(n)) \quad \Longleftrightarrow \quad
        \exists k \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ t.q. } \quad
        f(n) \leq k \cdot g(n) \quad
        \forall n \geq n_0

On dit qu'une fonction :math:`f(n)` appartient à :math:`\mathcal{O}(g(n))` si il existe une constante :math:`k`,
telle que :math:`k\cdot g(n)` est systématiquement plus grand que :math:`f(n)` pour tout :math:`n` suffisament grand
(autrement dit, il existe un :math:`n_0` à partir de laquelle la règle est respectée).

:math:`g(n)` fonctionne donc comme une borne supérieure à la fonction à une constante près.

Exemple
-------

Soit :math:`f(n) = 2n^2+3n`. On a que :math:`f(n)\in \mathcal{O}(n^2)` (autrement dit, on choisi :math:`g(n)=n^2`).
En effet, avec :math:`k=3`, la règle est respectée à partir de :math:`n=3`.

De manière similaire, la même fonction :math:`f(n) = 2n^2+3n` appartient à d'autres ensembles:

* :math:`f(n) \in \mathcal{O}(n^3)`
* :math:`f(n) \in \mathcal{O}(n^4)`
* ...
* :math:`f(n) \in \mathcal{O}(2^n)`
* ...

car toutes ces fonctions sont bien des bornes supérieures à :math:`n^2` quand :math:`n` est grand.

Dans la majorité des cas, on va vouloir choisir la fonction :math:`g(n)` la plus petite possible qui respecte la
propriété, étant donné que cela va nous apporter le plus d'information.

Notation Big-Omega (:math:`\mathcal{\Omega}`)
=============================================

La définition est similaire à celle de Big-Oh. En gras les différences:

.. math::

    f(n) \in \mathbf{\mathcal{\Omega}}(g(n)) \quad \Longleftrightarrow \quad
        \exists k \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ t.q. } \quad
        \mathbf{k \cdot f(n) \geq g(n)} \quad
        \forall n \geq n_0

Pour de grandes valeurs de :math:`n`, :math:`f(n)` est toujours plus grande que :math:`g(n)` à une constante
près. Concrètement, cela signifie que la fonction :math:`g(n)` place une borne
inférieure sur la complexité de :math:`f(n)`. En d’autres mots, :math:`g(n)` caractérise le
"meilleur cas" possible pour le calcul de f(n) (ceci est un abus de language: voir plus bas).

Exemple
-------

Dans le cas général, Insertion sort :math:`\in \mathcal{\Omega}(n)`.

Notation Big-Theta (:math:`\mathcal{\Theta}`)
=============================================

.. math::

    f(n) \in \mathbf{\mathcal{\Theta}}(g(n)) \quad \Longleftrightarrow \quad
        \exists k_0,k_1 \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ t.q. } \quad
        \mathbf{k_0 \cdot g(n) \leq f(n) \leq k_1 \cdot g(n)} \quad
        \forall n \geq n_0

Autrement dit, pour de grandes valeurs de :math:`n`, :math:`f(n)` se comporte comme :math:`g(n)` à une constante
multiplicative près. :math:`g(n)` agit donc à la fois comme une borne inférieure et supérieure.

On peut voir aisément que (démonstration laissée en exercice)

.. math::

    f(n) \in \mathbf{\mathcal{\Theta}}(g(n)) \quad \Longleftrightarrow \quad f(n) \in \mathbf{\mathcal{O}}(g(n)) \quad\wedge\quad f(n) \in \mathbf{\mathcal{\Omega}}(g(n))

Remarques
---------

Il n'est pas possible de trouver une fonction :math:`g(n)` telle que :math:`f(n) \in \mathcal{\Theta}(g(n))` pour toute fonction :math:`f(n)`.
Par exemple, pour Insertion sort, Vu qu'il est en :math:`\mathcal{O}(n^2)` mais en :math:`\mathcal{\Omega}(n)`, et que ces deux bornes sont atteintes,
il n'est pas possible de dire que Insertion est en :math:`\mathcal{\Theta}(g(n))`.

Exemple
-------

Merge sort est en :math:`\mathcal{\Theta}(n\log_2 n)`.

Notation Tilde (:math:`\mathcal{\sim}`)
=======================================

La définition de la notation tilde se base sur des principes différents:

.. math::

    f(n) \sim g(n) \quad \quad \Longleftrightarrow \quad \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 1

Cette définition à priori plus compliquée nous permet simplement de voir que
pour de grandes valeurs de :math:`n`, :math:`f(n)` et :math:`g(n)` se comportent de la même façon:
l’intuition est donc un peu la même que pour :math:`\mathcal{O}`. D’ailleurs, on a aussi:

.. math::

    f(n) \sim g(n) \quad \quad \Longrightarrow \quad f(n) \in \mathcal{O}(g(n))

Mais la relation inverse n’est pas vraie. En effet, si on prend l’exemple de d’un
algorithme avec un temps d'exécution A qui nécessite de parcourir une liste deux fois, on a:

.. math::

    A(n) \not\sim n \quad \text{car} \quad  \lim_{n\rightarrow\infty} \frac{A(n)}{n} = 2

Cet exemple nous montre la principale différence entre :math:`\mathcal{O}` et :math:`\sim`: tilde conserve le facteur
multiplicatif.

Il existe une autre différence: tilde fournit une borne *atteinte*. Par exemple: selon la définition de :math:`\mathcal{O}`, on a que

* :math:`n \in \mathcal{O}(n)`
* :math:`n \in \mathcal{O}(n^2)`
* :math:`n \in \mathcal{O}(2^n)`

car :math:`n`, :math:`n^2` et :math:`2^n` deviennent toute à terme "plus grands" que :math:`n`. Or, nous avons que

* :math:`n \sim n` (évidemment)
* :math:`n \not\sim n^2`
* :math:`n \not\sim 2^n`

car la limite de ces deux dernières fonctions tends vers 0, et non pas 1!

Il existe d'autres différences plus subtiles, dont nous parlerons lors d'exercices.

Meilleur cas, pire cas, cas moyen
=================================

Nous entendons trop souvent dire que :math:`\mathcal{O}` est *le pire cas* et :math:`\mathcal{\Omega}` le *meilleur cas*.
Cela est **faux** en général, tout dépend de la manière dont vous définissez votre fonction.

Imaginons que nous utilisions un algorithme de Tri Rapide, que nous verrons dans la Partie 2 du cours.
Si vous définissez :math:`f(n)` comme "le nombre d'opérations de comparaison à effectuer pour un tableau de taille n", alors vous avez:

* :math:`f(n) \sim n^2` et :math:`f(n) \in \mathcal{O}(n^2)`
* :math:`f(n) \in \mathcal{\Omega}(n\log_2 n)`

Si maintenant vous définissez :math:`g(n)` comme "le nombre **moyen** (l'espérance) d'opérations de comparaison à effectuer
pour un tableau de taille n, **quand on sélectionne uniformement les tableaux**", vous obtenez:

* :math:`g(n) \sim n\log_2 n` et :math:`g(n) \in \mathcal{O}(n\log_2 n)`
* :math:`g(n) \in \mathcal{\Omega}(n\log_2 n)`
* et donc :math:`g(n) \in \mathcal{\Theta}(n\log_2 n)`

Par un (léger) abus de language, on dit que le "cas moyen" du Tri rapide est en :math:`\mathcal{\Theta}(n\log_2 n)`.
Mais le cas général ne l'est pas!

Complexité amortie
=================================

Un autre type de complexité utile est celle qui compte la complexité moyenne pour :math:`m` opérations.
    Cette complexité s'appelle la *complexité amortie*.
Par exemple, un `ArrayList <https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html>`_
en java est simplémenté avec un array qui double sa taille dès que sa capacité est atteinte.
L'opération de doublement de la taille se fait en :math:`O(n)` où :math:`n` est la taille courante du tableau
    L'insertion de :math:`n+1` opérations avec la méthode *add(E e)* lorsque le tableau a une taille courante de :math:`n`
    coûtera en moyenne :math:`\mathcal{O}(1)*n+\mathcal{O}(n)/(n+1)=\mathcal{O}(1)`.

Attention la complexité de la méthode *add(E e)* isolément est bien  :math:`\mathcal{\Omega}(1)` et :math:`\mathcal{O}(n)`
ou n est le nombre d’éléments dans l'ArrayList.

