.. _part2_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W6.



Exercise 3.1.1
""""""""""""""

Which of the two ``SequentialSearchST`` or ``BinarySearchST`` implementations would you use for an application?
which performs :math:`10^3` ``put()`` and :math:`10^6` ``get()`` in random order? Justify.

.. answer::

    For ``SequentialSearchST``

    - Search: :math:`N` (Worst-case), :math:`N/2` (Average-case)
    - Insert: :math:`N` (Worst-case), :math:`N` (Average-case)


    For ``BinarySearchST``

    - Search: :math:`\log(N)` (Worst-case), :math:`\log(N)` (Average-case)
    - Insert: :math:`2N+\ln(N) \in mathcal{O}(n)` (Worst-case), :math:`\ln(N)+2\cdot N/2 \in mathcal{O }(n)` (Average-case)

    (note: the book doesn't consider that the array is copied at each iteration, thus this is the amortized complexity;
    may be a good opportunity to explain what this is to students? == if we double the size of the internal array
    each time there is an overflow, the complexity per element is :math:`\mathcal{O}(1)` for the array copy)
    (the 2 factor that appears here is because there are two arrays)

    Let :math:`M` be the initial size of the array before we do the push and get operations. If :math:`M >> 10^3`, the total number of operations is

    ..math::

        \approx 10^3\cdot I(M) + 10^6\cdot S(M)

    where :math:`I(M)` and :math:`S(M)` are the cost of inserting and searching in an array of size :math:`M`.

    For ``SequentialSearchST`` it gives :math:`10^3M + 10^6M` worst case, :math:`10^3M/2 + 10^6M` average

    For ``BinarySearchST`` it gives :math:`10^3\cdot 2 \cdot M + 10^6\cdot\log(M)` worst case, :math:`10^3\cdot M + 10^6 \cdot\log(M)` average case.

    Thus ``BinarySearchST`` if :math:`M` is great enough.

Exercise 3.1.2 (Inginious)
"""""""""""""""""""""""""""

`Implement the ceil method <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_BinarySearchTree>`_ method of ``BinarySearchST``.



Implement the ``floor()`` method of ``BinarySearchST``.

.. answer::

    .. code-block:: java

        public Key floor(Key key) {
            //rank returns the position where the key
            //should be if it is added

            //i.e. if keys[loc] == key => it exists, return key
            //     else, return the key just before the location
            //           where the key should be added

            int loc = rank(key);
            if(keys[loc].compareTo(key) == 0)
                return key;
            return keys[loc-1];
        }

Exercise 3.1.3
"""""""""""""""

*Exercise 3.1.24 of the book*.

Assuming the keys are doubles or integers. Write a version of binary search that assumes
a uniform distribution of keys and will thus first look at the beginning of a dictionary for a word that begins with a letter close to the beginning of the alphabet.

More exactly, if the searched key is :math:`k_x`, the smallest key is :math:`k_{lo}` and the largest
is :math:`k_{hi}`, the interpolation-search will first test at the key at percentile :math:`\lfloor(k_x-k_{lo})/(k_{hi}-k_{lo}) \rfloor * 100` of the array
and not in the middle (50 percentile) of the table first.

Implement ``InterpolationSearchST`` and compare this on ``FrequencyCounter``.

.. answer::

    On garde tout le même code soure que BinarySearchST (pages 379, 380) et on
    remplace la fonction ``rank`` (p 380) par celle-ci:

    .. code-block:: java

        private int getPos(Integer k, int start, int end) {
            int rng = end - 1 - start;

            if(rng < 0) return start;
            if(rng == 0) return k.compareTo(keys[start]) < 0 ? start : end;

            int k_start = keys[start];
            int k_end   = keys[end-1];

            Double interpol = ( (k - k_start) / (1.0 * (k_end - k_start)));
            interpol = Math.max(0, interpol);
            interpol = Math.min(1, interpol);
            Double ddm = Math.floor(rng * interpol);
            int mid    = start+ ddm.intValue();
            Integer piv = keys[mid];

            int cmp = piv != null ? k.compareTo(piv) : 0;
            if(cmp <  0) return getPos(k, start, mid);
            if(cmp >  0) return getPos(k, mid+1,   end);
            return mid;
        }

    Pdv performances, si on reprend le FrequencyCounter (et qu'on l'adapte pour que
    l'interpolation search soit utilisable) on obtient les résultats suivants:

    - Le comptage des fréquences prend exactement le même temps pour
      BinarySearchST que pour InterpolationSearchST parce que le cout du
      décalage de tous les éléments (:math:`\mathcal{O}(n)`) qui est nécessaire lorsqu'on inclut
      une nouvelle clé dans la structure est largement supérieur au bénéfice
      potentiel de l'interpolation.
    - Même si on ne fait que des queries dans le tableau, on n'observe pas de
      différence de performance importante entre les deux algos (même si on
      pense intuitivement que l'interpolation devrait aller plus vite).


Exercise 3.1.4
"""""""""""""""

*Exercise 3.1.25 of the book*.

It is very common to first test the presence of a key before adding or modifying the corresponding entry. That
successively generates several consecutive searches for the same key.

The idea of *caching* is to memorize internally the last accessed key
and to use it opportunistically if it is still valid.
Modify ``BinarySearchST`` to incorporate this idea.

.. answer::

    Simply create the *instance variables* ``lastKey`` and ``lastI`` (for example) and in functions ``get`` and ``put`` check if ``key==lastKey`` if so use ``lastI`` if not call ``lastI=rank(key)`` and `lastKey = key`.

Exercise 3.1.5
""""""""""""""

*Exercise 3.2.31 of the book*.

Write a method ``isBST()`` method that takes a ``Node`` as an argument and returns ``true`` if the argument is the root of a BST, ``false`` otherwise (so check that the properties of a BST are satisfied).

Do you think that testing (locally) for each node the property *"the left child has a lower key and the right child an upper key"* is sufficient? If not, give a counterexample.

How complex is your algorithm?

.. answer::

    (Solution from page 420 of Alg4s)

    .. code-block:: java

        private boolean isBST()
        {
            return isBST(root, null, null);
        }

        private boolean isBST(Node x, Key min, Key max)
        {
            if (x == null) return true;
            if (min != null && x.key.compareTo(min) <= 0) return false;
            if (max != null && x.key.compareTo(max) >= 0) return false;
            return isBST(x.left, min, x.key) && isBST(x.right, x.key, max);
        }

Exercise 3.1.6
""""""""""""""

*Exercise 3.2.4 of the book*.

Suppose a certain search tree has keys between 1 and 10 and we are looking for key 5.
Which sequence(s) cannot match the sequence of the examined keys?

* 10,9,8,7,6,5
* 4,10,8,6,5
* 1,10,2,9,3,8,4,7,6,5
* 2,7,3,8,4,5
* 1,2,10,4,8,5

.. answer::

    Seul le d est impossible ca on a 8 qui apparait après 7,3. Or :math:`8 \not\in\left[7,3\right]`

Exercics 3.1.7
"""""""""""""""""

*Exercise 3.3.33 of the book*.

Write an method ``is23()`` in ``RedBlackBST`` that checks that no nodes are connected
to two red links and that there is no red link to the right.
Also write an method ``isBalanced()`` that checks that any path from the root to a null link has the
same number of black links. Finally combine ``isBST(),is23()`` and ``isBalanced()`` to implement ``isRedBlackBST()``.


.. answer::

    .. code-block:: java

        boolean is23() = return is23(root);
        boolean is23(Node h) {
           if (h == null) return true; //empty tree is 23-tree
           if (isRed(h.right)) return false; //if red at the right !is23

           // we are not the root and both node and his left node is red !is23
           if (h != root && isRed(h) && isRed(h.left)) return false;

           //if h is23 all subtree of h is23 too
           return is23(h.left) && is23(h.right);
        }

        //count the number of the black (nBlack) at the most-left path of the tree from the root. If the tree is balanced there is the same number black for all path from root to null nodes
        boolean isBalanced() {
            int nBlack = 0;
            Node h = root;
            while (h != null) {
                if (!isRed(h)) nBlack++;
                h = h.left;
            }
            return isBalanced(root, nBlack);
        }
        boolean isBalanced(Node h, int nBlack) {
            if (h == null) return nBlack == 0;
            if (!isRed(h)) nBlack--;
            return isBalanced(h.left, nBlack) && isBalanced(h.right, nBlack);
        }


        isRedBlackBST() =  isBST() && is23() && isBalanced().

Exercise 3.1.8
""""""""""""""

How to enumerate all memorized keys in ascending order
in a binary search tree? What is the time complexity of
this operation ? Justify your answer.

.. answer::

    Obviously, on fait simplement un parcours *in-order* sur l'arbre. La complexité est connue et est
    en :math:`\theta(n)`. Justification intuitive: Comme on doit toujours parcourir tous
    les noeuds de l'arbre (3 fois) on ne fait pas mieux qu':math:`\Omega(N)` mais pas pire
    que :math:`\mathcal{O}(N)` non plus.

Exercise 3.1.9
"""""""""""""""

Starting from an initially empty binary search tree, how does the tree look like
after inserting the keys 12, 5, 10, 3, 13, 14, 15, 17, 18, 15? 
For the same data how would the tree look like for a 2-3 tree?

Does this example illustrate the advantages or disadvantages of these different data structures? Why ?


.. answer::

    For a binary tree:

    .. image:: 9a.png

    For a 2-3 tree

    .. image:: 9b.png

    .. image:: 9c.png



Exercise 3.1.10
"""""""""""""""""

Which of these trees is (are) red-black? For each, draw the correspondence to a 2-3 tree
(described p432).

.. image:: rbtree.png
    :alt: Arbres

.. answer::

    Seuls les arbres iii et iv sont des red black trees: les autres ne représentent
    pas un 2-3 tree valide.

    1. Pas d'équilibre au niveau des longueurs noires
    2. Pas un 2-3 arbre balancé, et en plus F est à gauche de E (donc même pas un
    BST)
    3. C'est un RBT (obviously !)
    4. Idem

    .. image:: tree_i.png
    .. image:: tree_ii.png
    .. image:: tree_iii.png
    .. image:: tree_iv.png


Exercise 3.1.11 (Inginious)
"""""""""""""""""""""""""""""

`Implement an iterator for a BST <hhttps://inginious.info.ucl.ac.be/course/LINFO1121/searching_BinarySearchTreeIteratorr>`_


Exercise 3.1.12 (Inginious MCQ)
""""""""""""""""""""""""""""""""""

`Time complexity of binary search trees <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/PART3Qcm>`_



Exercise 3.1.13 (Inginious MCQ)
""""""""""""""""""""""""""""""""""

`Binary search tree traversals <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/PART3QcmBt>`_


Exercise 3.1.14 (Inginious manual exericse)
""""""""""""""""""""""""""""""""""""""""""""

`Red-black tree insertions <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/PART3Rbt>`_


