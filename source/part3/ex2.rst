.. _part2_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W7.


Exercice 3.2.1
"""""""""""""""

Vrai ou faux ?

Remarque: BST s'entend ici comme l'implémentation du livre, c'est-à-dire un arbre qui n'est pas nécessairement équilibré.
Les 2-3/red-black BST s'entendent également comme étant celles du livre de référence.


Nous recommandons de vous familiariser préalablement avec les notions de `parcours d'arbres <https://fr.wikipedia.org/wiki/Arbre_binaire#Parcours_préfixe>`_: infixe, préfixe et postfixe.

* Dans le meilleur des cas, le nombre de comparaisons entre clefs pour une recherche binaire d'une clef particulière dans un tableau trié de N clefs distinctes est :math:`\sim \log N`.

  .. answer::

    Faux c'est :math:`\mathcal{O}(1)`, si on a de la chance on tombe directement dessus.

* Étant donné un parcours infixe d'un BST contenant N clefs distinctes. Est-il possible de reconstruire la forme du BST sur base du résultat du parcours ? Si oui, écrivez le pseudo-code d'un algorithme pour le faire, si non, donnez un contre-exemple qui justifie votre réponse.

  .. answer::

    Invitez les étudiants à avoir un regard critique, comment prouver que c'est vrai ou faux?
    Non, on peut facilement trouver deux BST différents pour l'input 5,10,15,20.

* Étant donné un parcours préfixe d'un BST contenant :math:`N` clefs distinctes. Est-il possible de reconstruire la forme du BST sur base du résultat du parcours ? Si oui, écrivez le pseudo-code d'un algorithme pour le faire, si non, donnez un contre-exemple qui justifie votre réponse.

  .. answer::

    Demandez aux étudiants de concevoir l'algo (un dessin au tableau suffit).

    .. code-block:: java

        private static Node readBSTFromPreorder(int [] input) {
            return readBSTFromPreorder(input,0,
                Integer.MIN_VALUE, Integer.MAX_VALUE);
        }

        private static Node readBSTFromPreorder(int [] input,
                 int i, int min, int max) {
          if (i < input.length && input[i] > min && input [i] < max) {
            Node left = readBSTFromPreorder(input,i+1,min,input[i]);
            Node right = readBSTFromPreorder(input,i+left.size+1,input[i],max);
            return new Node(input[i],left,right,left.size+right.size+1);
          } else {
            return EMPTY;
          }
        }

    Est-ce que cela marche avec un parcours postfixe? Et avec un parcours infixe?

* Étant donné un arbre ordonné de :math:`N` clefs distinctes et une clef :math:`x`, est-il possible de trouver la plus petite clef strictement plus grande que :math:`x` en temps logarithmique dans le pire cas?

  .. answer::

    faux, rien ne dit que l'arbre est équilibré. Cela peut donc prendre :math:`\mathcal{O}(N)` dans le pire cas. Demandez aux étudiants de dessiner un arbre correspondant à ce scénario.

* La hauteur attendue d'un BST résultant de l'insertion de N clefs distinctes dans un ordre aléatoire dans un arbre initialement vide est en moyenne logarithmique.

  .. answer::

    C'est vrai. Et le meilleur cas? (:math:`\mathcal{O}(\log n)`) Et le pire cas? (:math:`\mathcal{O}(n)`)

* Soit :math:`x` un noeud dans un BST. Le successeur de :math:`x` (le noeud contenant la clef suivante dans l'ordre croissant) est le noeud le plus à gauche dans l'arbre de droite de :math:`x`.

  .. answer::

    Non, le noeud :math:`x` peut être une feuille ...

* La hauteur maximum d'un 2-3 tree avec N clefs est :math:`\sim \log_3 N`

  .. answer::

    faux, c’est :math:`\text{ceil}(\log_2 N)` (voir proposition F page 429) (le mot important de l'énoncé est *maximum*).

* Pour l'insertion de N clefs dans l'ordre croissant dans un red-black BST initialement vide. Le nombre de changements de couleur de la dernière insertion est au plus 3.
  Le nombre de changements s'entend comme la somme des différences en valeur absolue entre le nombre de rouges après insertion moins le nombre de rouges avant insertion.

  .. answer::

    C'est faux. Si vous insérez 1,2,3,4,5,etc vous allez commencer à saturer toute la branche la plus à droite de l'arbre.
    A moment donné le nombre de changements de la dernière insertion sera égale à la hauteur, situation qui arrive lorsque tous
    les noeuds de la branche de droite sont des 3-noeuds
    car la "bulle" (transormation de 3 noeuds en 2 noeuds) doit remonter jusqu'à la racine.

* Un red-black BST obtenu après insertion de :math:`N > 1` clefs dans un arbre initialement vide possède au moins un lien rouge ? Si non, donnez un contre-exemple.

  .. answer::

    faux. le nombre de lien rouge peut descendre si ça remonte à la racine. On peut trouver un arbre avec zero lien rouge: (v=2,left=1,right=3).

* Dans un red-black BST de N noeuds, la hauteur noire (i.e. le nombre de liens noirs de chaque chemin depuis la racine vers un lien null) est maximum :math:`\log N`.

  .. answer::

    oui, pour s'en convaincre il faut garder le mapping vers les arbres 2-3.

Exercice 3.2.2
""""""""""""""""

Imaginez un algorithme de tri utilisant un BST. A quoi ressemblerait cet algorithme ?
Quelle serait la complexité de votre algorithme si le BST est remplacé par un red-black BST ?

.. answer::

    :math:`\mathcal{O}(n^2)` pour la construction du BST car l'insertion prends :math:`\mathcal{O}(n)`, :math:`\mathcal{O}(n \log(n))` pour la construction du red-black car l'insertion prend :math:`\mathcal{O}(\log(n))`. Ensuite :math:`\mathcal{O}(n)` pour faire le parcours infixe dans les deux cas.

Exercice 3.2.3
""""""""""""""""

Est-ce que l'opération de suppression dans un BST est "commutative" ?
C'est à dire que supprimer :math:`x` et ensuite directement :math:`y` d'un BST (tel qu'implémenté dans le livre)
laisse l'arbre dans même état que si on avait d'abord supprimé :math:`y`  et puis :math:`x` ?
Donner un contre-exemple ou argumenter pourquoi c'est effectivement toujours le cas.
Pour vous aider, considérez l'arbre suivant et les opérations de suppression de 5 et 10.

.. code-block::

      10
     / \
    5   15
       /
      11

.. answer::

    faux, delete 10 puis 5 donne (11,right:15), delete 5 puis 10 donne (15,left:11)
