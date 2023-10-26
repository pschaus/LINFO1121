.. _part5_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W10.



Exercise 5.1.1
""""""""""""""

Give the array ``id[]`` that results from the following sequence of 6 union operations on a starting set of 10 items with the quick-find algorithm.
``3-8, 1-7, 1-8, 9-4, 6-4, 2-0``.
Your answer must be a sequence of 10 integers.
Reminder: the quick-find convention for the ``p-q`` union is to change ``id[p]`` (and possibly other inputs) but not ``id[q]``.

.. answer::

    ``0 8 0 8 4 5 4 8 8 4``



Exercise 5.1.2
""""""""""""""

Give the array id[] that results from the following sequence of 9 union operations on a set of 10 items using the weighted quick-union algorithm:

``4-6, 3-6, 8-9, 7-0, 1-2, 8-4, 6-5, 1-7, 6-0.``

Your answer must be a sequence of 10 integers. Reminder: When merging two trees of the same size, the weighted quick-union algorithm uses the convention
to point the root of the second tree to the root of the first tree.
Our algorithm uses union by size (number of nodes) and not union by height, nor the path compression technique.

.. answer::

    7 4 1 4 4 4 4 1 4 8

Exercise 5.1.3
""""""""""""""

Which of the following id[] array(s) could result from applying the weighted quick-union algorithm on a set of 10 items at the beginning?
Reminder: we use union by size (number of nodes) and not union by height.


* ``0 8 2 3 4 7 6 8 8 9``
* ``4 2 6 6 2 6 6 2 4 2``
* ``7 0 0 0 0 1 0 5 1 0``
* ``3 3 0 3 0 3 3 3 5 2``
* ``1 3 3 6 4 1 6 0 6 8``

.. answer::

    * correct
    * ko Size of tree rooted at parent of 2 < twice the size of tree rooted at 2
    * ko
    * correct: sequence ``0-4 3-1 5-8 3-6 5-6 2-9 0-2 9-8 5-7``
    * ko Height of forest :math:`= 4 > \log N = \log(10)`

Exercise 5.1.4
""""""""""""""

Give the sequence of keys in the table that results from inserting the sequence of the 3 keys 48, 30 and 84
in the following heap (oriented to the maximum) of size 10:

``97 , 93 , 89 , 83 , 38 , 32 , 40 , 12 , 26 , 24``.

Your answer should be a sequence of 13 integers.

.. answer::

    The correct answer is: 97 93 89 83 48 84 40 12 26 24 38 30 32
    Here is the sequence of keys in the array after each insertion:

    ========  ==========================================
    start     ``97 93 89 83 38 32 40 12 26 24``
    after 48  ``97 93 89 83 48 32 40 12 26 24 38``
    after 30  ``97 93 89 83 48 32 40 12 26 24 38 30``
    after 84  ``97 93 89 83 48 84 40 12 26 24 38 30 32``
    ========  ==========================================

Exercise 5.1.5
""""""""""""""

Give the sequence of keys in the array that results from adding 3 successive deletion operations from the maximum in the following heap (oriented to the maximum)
of size 10:

``98 , 96 , 84 , 34 , 62 , 31 , 72 , 13 , 27 , 33``.

Your answer should be a sequence of 7 integers.

.. answer::

    The correct answer is: 72 62 31 34 33 13 27
    Here is the sequence of keys in the array after each deletion:

    ==========  ========================================
    start       ``98 96 84 34 62 31 72 13 27 33``
    98 deleted  ``96 62 84 34 33 31 72 13 27``
    96 deleted  ``84 62 72 34 33 31 27 13``
    84 deleted  ``72 62 31 34 33 13 27``
    ==========  ========================================

Exercise 5.1.6
""""""""""""""""

What are the possible advantages and disadvantages of implementing a priority queue with
a heap rather than a list?

.. answer::

    On en profite pour rappeler qu'on peut implémenter des ADT (ici une PQ) par plusieurs manières
    (ici, une heap, ou une liste, ou ...) et toutes ne se valent pas.

    Une implémentation par une liste maintenant simplement l'ordre est en :math:`\mathcal{O}(n)` en insertion,
    mais :math:`\mathcal{O}(1)` en deletion. Au contraire du :math:`\mathcal{O}(\log n)` offert par les deux opérations
    d'une heap.

    Existe-t-il des cas où une implémentation basée sur une liste est utile?
    Probablement pas; on veut souvent retirer tout les élements qu'on insére dans une PQ.

Exercise 5.1.7
""""""""""""""

Can you find an example of a valid heap T storing 7 distinct elements such that 
an infix traversal of T visists the elements in decreasing order?
What about an prefix or postfix traversal?


.. answer::

    Soit le heap suivant:

    .. image:: heap7.png

    Les ordres sont les suivants:

    * infixe: :math:`D<B<E<A<F<C<G`
    * préfixe: :math:`A<B<D<E<C<F<G`
    * postfixe: :math:`D<E<B<F<G<C<A`

    La propriété de min-heap implique que :math:`A < B, A < C, B < D, \ldots`.

    Le postfixe est donc le seul qui fonctionne (il y des contradictions dans les autres cas).
    Avec un max-heap, vous avez seulement le préfixe qui fonctionne.


Exercise 5.1.8
""""""""""""""

Which of the following statements are true about a priority queue implemented by a heap? 
By default heaps are maximum oriented and use an index base starting at 1.

* In the worst case, inserting a key into a binary heap containing N keys requires :math:`\sim \log N` comparisons.

  .. answer::

    true: each swim operation compares the inserted key only to keys on a path from the new leaf to the root

* Let :math:`a[]` be an array such that :math:`a[1] > a[2] > a[N]` (and :math:`a[0]` is empty). Then :math:`a[]` satisfies the properties of a binary heap.

  .. answer::

    true: A reverse-sorted array obeys heap order.

* The inernal array of a binary (max-)heap is always an array sorted in non increasing order.

  .. answer::

    faux. [-,3,1,2] est correct et n'est pas décroissant.

* Given a binary heap of N distinct keys, deleting the maximum key and then inserting it directly leaves the array of the heap unchanged (we ignore the possible resizing of the array).

  .. answer::

    False, Consider the binary heap Key[] = [ -, 3, 2, 1 ]. After the deletion of max key, it will be [ -, 2, 1 ]. After the insertion, it will be [ -, 3, 1, 2 ].

Exercise 5.1.9
""""""""""""""

Prove that the bottom-up "sink" construction of a heap for the Heapsort (p323) is done in :math:`\mathcal{O}(n)`.
Hint: count the number of nodes at the :math:`h` level of the heap.
What is the complexity of a sink at this level. Do the sum for all levels. Useful formula: :math:`\sum_{k=0}^\infty k x^k = x/(1-x)^2` for
:math:`|x| < 1`.

.. answer::

    from the bottom, at level :math:`j` there are :math:`2^{h-j}` nodes, and each might shift down :math:`j` levels. So, if we count from bottom to top, level-by-level, we see that the total time is proportional to

    .. math::

        T(N) = \sum_{j=0}^h j \frac{2^h}{2^j} = 2^h \sum_{j=0}^h  \frac{j}{2^j}  \le 2^h \sum_{j=0}^{+\infty}  \frac{j}{2^j} \le 2^h \cdot 2 = 2^{\log n} = n

Exercise 5.1.10
""""""""""""""""

Is the use of a priority queue essential to be able to build a Huffman code? 
Can you imagine another solution using a sorting algorithm? 
Would the computational complexity be better than the original algorithm? Why or why not?

.. answer::

    Oui indispensable. Un insertion sort coûterait du :math:`\mathcal{O}(n)` à chaque fois donc ça serait du :math:`\mathcal{O}(n^2)` pour construire le tree au départ du tableau des fréquences.

Exercise 5.1.11
""""""""""""""""

* What are the different steps in a text *compression* algorithm that takes a text as input and provides a compressed version of that text as output using Huffman coding? Be specific in your description by isolating each step of the problem. Specify for each step the useful data structures and the time complexity of the operations performed.
* What are the different steps of a text *decompression* algorithm that takes as input a compressed version of a text using Huffman coding and provides as output the original text? Be precise in your description by isolating each step of the problem. Specify for each step the useful data structures and the time complexity of the operations performed.


.. answer::

    bullet point p835.


Exercise 5.1.12 (Inginious, heap)
""""""""""""""""""""""""""""""""""

Implement the `Push of a binary Heap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_BinaryHeap>`_



Exercise 5.1.13 (Inginious, Global Warming)
""""""""""""""""""""""""""""""""""""""""""""""


Implement the Global Warming to compute the number of islands using union-find `GlobalWarmming <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarming>`_


Exercise 5.1.14 (Inginious, Huffman)
""""""""""""""""""""""""""""""""""""""""""""""

Implement the Huffman tree reconstruction `Huffman <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_Huffman>`_


Exercise 5.1.15 (Inginious, manual exercise on UnionFind)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Small manual exercise on `UnionFind <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part5UnionFind>`_


Exercise 5.1.16 (Inginious, manual exercise on Heaps)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Small manual exercise on `Heaps <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part5Heap>`_
