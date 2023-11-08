.. _part3_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W7.


    Faux c'est :math:`\mathcal{O}(1)`, si on a de la chance on tombe directement dessus.


Exercice 3.2.1 (True/False BinarySearch)
""""""""""""""""""""""""""""""""""""""""

* In the best case, the number of key comparisons for a binary search for a particular key in a sorted array of N distinct keys is :math:`\sim \log N`.


  .. answer::



Exercice 3.2.2 (True/False BST)
""""""""""""""""""""""""""""""""


Note: BST is understood here as the implementation of the book, i.e. a tree that is not necessarily balanced.
The 2-3/red-black BST is also understood to be the one in the reference book.


We recommend that you first become familiar with the notions of `tree traversals <https://en.wikipedia.org/wiki/Tree_traversal>`_: infix, prefix and postfix.



* Given the output of an infix traversal of a BST containing N distinct keys. Is it possible to reconstruct the shape of the BST based on the result of the traversal? If so, write the pseudo-code of an algorithm to do so, if not, give a counterexample that justifies your answer.

  .. answer::

    Invitez les étudiants à avoir un regard critique, comment prouver que c'est vrai ou faux?
    Non, on peut facilement trouver deux BST différents pour l'input 5,10,15,20.

* Given a the output of a prefix traversal of a BST containing :math:`N` distinct keys. Is it possible to reconstruct the shape of the BST based on the result of the walk? If so, write the pseudo-code of an algorithm to do so, if not, give a counterexample that justifies your answer.

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

* Given an ordered tree of :math:`N` distinct keys and a :math:`x` key, is it possible to find the smallest key strictly larger than :math:`x` in logarithmic time in the worst case?

  .. answer::

    faux, rien ne dit que l'arbre est équilibré. Cela peut donc prendre :math:`\mathcal{O}(N)` dans le pire cas. Demandez aux étudiants de dessiner un arbre correspondant à ce scénario.

* The expected height of a BST resulting from inserting N distinct keys in a random order into an initially empty tree is on average logarithmic.

  .. answer::

    C'est vrai. Et le meilleur cas? (:math:`\mathcal{O}(\log n)`) Et le pire cas? (:math:`\mathcal{O}(n)`)

* Let :math:`x` be a node in a BST. The successor of :math:`x` (the node containing the next key in ascending order) is the leftmost node in the tree on the right of :math:`x`.

  .. answer::

    Non, le noeud :math:`x` peut être une feuille ...



Exercice 3.2.3 (True/False Redblack Trees)
"""""""""""""""""""""""""""""""""""""""""""

For the statements related to red-black trees, we advise you to first translate it into a statement into 2-3 trees
as there is a one-to-one mapping between the two representation.
In most cases, it is easier to answer on the validity of the statement for 2-3 trees.


* The maximum height of a 2-3 tree with N keys is :math:`\sim \log_3 N`

  .. answer::

    faux, c’est :math:`\text{ceil}(\log_2 N)` (voir proposition F page 429) (le mot important de l'énoncé est *maximum*).

* For the insertion of N keys in ascending order into an initially empty red-black BST. The number of color changes of the last insertion is at most 3. The number of changes is understood to be the sum of the absolute value differences between the number of reds after insertion minus the number of reds before insertion.

  .. answer::

    C'est faux. Si vous insérez 1,2,3,4,5,etc vous allez commencer à saturer toute la branche la plus à droite de l'arbre.
    A moment donné le nombre de changements de la dernière insertion sera égale à la hauteur, situation qui arrive lorsque tous
    les noeuds de la branche de droite sont des 3-noeuds
    car la "bulle" (transormation de 3 noeuds en 2 noeuds) doit remonter jusqu'à la racine.

* A red-black BST obtained after inserting :math:`N > 1` keys into an initially empty tree has at least one red link? If not, give a counterexample.

  .. answer::

    faux. le nombre de lien rouge peut descendre si ça remonte à la racine. On peut trouver un arbre avec zero lien rouge: (v=2,left=1,right=3).

* In a red-black BST of N nodes, the black height (i.e. the number of black links in each path from the root to a null link) is maximum :math:`log N`.

  .. answer::

    oui, pour s'en convaincre il faut garder le mapping vers les arbres 2-3.


Exercise 3.2.2 (Sorting with BST)
"""""""""""""""""""""""""""""""""""""

Imagine a sorting algorithm using a BST. What would this algorithm look like?
What would be the complexity of your algorithm if the BST is replaced by a red-black BST?

.. answer::

    :math:`\mathcal{O}(n^2)` pour la construction du BST car l'insertion prends :math:`\mathcal{O}(n)`, :math:`\mathcal{O}(n \log(n))` pour la construction du red-black car l'insertion prend :math:`\mathcal{O}(\log(n))`. Ensuite :math:`\mathcal{O}(n)` pour faire le parcours infixe dans les deux cas.


Exercise 3.2.3 (Delete Complexity)
"""""""""""""""""""""""""""""""""""

What is the time complexity for deleting the key 5 from the BST depitected below with the implementation of the text book?

.. code-block::

      15
        \
         x
        / \
       /   \
      /     \ 
     /n nodes\ 
    /         \
    -----------

.. answer::

    :math:`\mathcal{O}(1)` since the book has an optimization in the case the left or right node is null, it simply returns the other child node in O(1).

Exercise 3.2.4 (Delete Commutativity)
""""""""""""""""""""""""""""""""""""""


Is the delete operation (as implemented in the book) in a BST "commutative"?
That is, deleting :math:`x` and then directly :math:`y` from a BST
leaves the tree in the same state as if we had first deleted :math:`y` and then :math:`x`?
Give a counterexample or argue why this is indeed always the case.
To help you, consider the following tree and the deletion operations of 5 and 10.

.. code-block::

      10
     / \
    5   15
       /
      11

.. answer::

    faux, delete 10 puis 5 donne (11,right:15), delete 5 puis 10 donne (15,left:11)


Exercise 3.2.5 (Inginious)
"""""""""""""""""""""""""""""

Impement a method which returns the least key strictly greater than a given key:
`Higher key <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_BinarySearchTreeHigher>`_

Exercise 3.2.6 (Inginious)
"""""""""""""""""""""""""""""

Implement the reconstruction of a BST from the preorder traversal:
`Preorder reconstruction <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_PreorderToBST>`_


Exercise 3.2.7 (Inginious)
"""""""""""""""""""""""""""""

Implement the get/put operations of a BST with an array-based data-structure instead of linked nodes:
`ArrayBST <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_ArrayBST>`_


Exercise 3.2.8 (Inginious)
"""""""""""""""""""""""""""""""""

An easy one to query efficiently persons by their Birthday (exam 2023) `BirthdayMap <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_BirthdayMap>`_

Exercise 3.2.9 (Inginious)
"""""""""""""""""""""""""""""""""

Design an efficient algorithm to compute the `Skyline <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_Skyline>`_ form the set of building shapes (rectangles) that can overlap.


