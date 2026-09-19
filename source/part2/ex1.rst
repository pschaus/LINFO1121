.. _part2_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W4.



Exercise 2.1.1
""""""""""""""

Given an array containing :math:`n` sorted integers, and a number :math:`x` to insert into the array, can you
describe an algorithm to find the position where :math:`x` should be inserted while keeping the array sorted?

What is the time complexity of this algorithm?
Does your algorithm also work for a sorted linked list? With what complexity?



.. answer::

    Deux méthodes pour le tableau:

    * Soit faire une simple recherche, de gauche à droite, dans le tableau: :math:`\mathcal{O}(n)`.
    * Soit faire une recherche dichotomique: :math:`\mathcal{O}(\log n)`.

    Une métaphore qui marche bien est celle du dictionnaire: "comment faites-vous pour chercher dans un dictionnaire
    papier?"

    Pour la liste, la recherche dichotomique ne fonctionne pas car pas d'accès en O(1) à une position donnée. Donc il faut obligatoirement scanner.


Exercise 2.1.2
""""""""""""""

We consider the very general problem where we have :math:`n` jobs to perform for clients
and each job :math:`j` takes :math:`t_j` seconds to complete.
Only one job can be performed at a time.

The goal is to complete all jobs while maximizing customer satisfaction.
Maximizing customer satisfaction means building a schedule that minimizes
the average job completion time.

For example, if the durations of the jobs are 5, 8, 3, 4 and the jobs are carried out in this order,
the completion times will be 5, 13, 16, 20 and therefore the average completion time will be
:math:`\frac{5+13+16+20}{4}=13.5`.

Prove (with a written proof!) that sorting the :math:`n` jobs in ascending order of :math:`t_j` generates an optimal
solution to the problem.

.. answer::
    Par l'absurde. Soit une solution optimale au problème, qui ne respecte pas la propriété ci-dessus.
    Numérotons les éléments de la solution dans leur ordre de terminaison, de 0 à :math:`n-1`.

    La valeur de la solution est donc

    .. math::

        \sum_{i=0}^{n-1} \sum_{j=0}^i t_j

    Il existe :math:`a` tel que :math:`t_a > t_{a+1}`, sinon, la solution serait triée et la propriété respectée.

    Si on inverse :math:`a` et :math:`a+1` dans la solution, on obtient une nouvelle solution de valeur

    .. math::

        (\sum_{i=0}^{a-1} \sum_{j=0}^i t_j) + (\sum_{j=0}^{a-1} t_j + t_{a+1})
        + (\sum_{j=0}^{a-1} t_j + t_{a+1} + t_a) + (\sum_{i=a+2}^{n-1} \sum_{j=0}^i t_j)

    A comparer avec l'ancienne valeur:

    .. math::

        (\sum_{i=0}^{a-1} \sum_{j=0}^i t_j) + (\sum_{j=0}^{a-1} t_j + t_{a})
        + (\sum_{j=0}^{a-1} t_j + t_{a} + t_{a+1}) + (\sum_{i=a+2}^{n-1} \sum_{j=0}^i t_j)

    La différence entre la nouvelle et l'ancienne valeur est

    .. math::

        t_{a+1} + t_{a+1} + t_a - t_a - t_a - t_{a+1} = t_{a+1} - t_{a} < 0

    Autrement dit, la nouvelle solution a un coût plus petit que la précédente, qui n'était donc pas optimale.
    Contradiction.


Exercise 2.1.3
""""""""""""""

What is meant by a stable and an in-place sorting algorithm?
For all the algorithms presented in the reference book,
indicate whether they are in-place (or not) and whether they are stable (or not).


Answer the short `INGInious MCQ <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/sorting_property>`_.



.. answer::

    Stable: si la clé de tri associée à deux valeurs différentes est la même, ces deux valeurs resteront
    dans le même ordre relatif après tri.

    In-place: n'utilise pas de mémoire supplémentaire. (du moins, pas plus que :math:`\mathcal{O}(1)`).

Exercise 2.1.4 (INGInious: Card Sorter)
""""""""""""""""""""""""""""""""""""""""

How would you sort a pile of cards in ascending order with the restriction that
the only permitted operations are:

1. compare the first two cards,
2. exchange the first two cards,
3. move the first card to the back of the pile?

.. tip::

     Try to maintain the invariant that the `last i elements of the pile are sorted and are the i largest ones`.
     Then at each iteration try to make this invariant true for one more card (i+1).


Write the pseudocode of your algorithm on paper and give its time complexity.


Once it is done, implement your solution on the INGInious `task <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_CardSorter>`_.

Exercise 2.1.5
""""""""""""""

How can you sort a doubly linked list (which does not allow access
to a position by index) efficiently? What is the time complexity of your
algorithm?


Which algorithm is used by the `sort` method of the `List` interface below?


.. code-block::

        LinkedList<Integer> list = new LinkedList<Integer>();
        for (int i = n; i >= 0; i++) {
            list.add(i);
        }
        list.sort(Integer::compare);


.. answer::

    Il y a moyen d'adapter le quick sort ou le merge sort à des listes, mais c'est pas très naturel pour quicksort.
    Java copie la liste dans un tableau et utilise ensuite l'algorithme Timsort https://en.wikipedia.org/wiki/Timsort
    Notez que la question à l'examen sera peut-être "trier cette liste doublement chainée..."
    et qu'il faudra le coder.

Exercise 2.1.6
""""""""""""""

Design an efficient algorithm for counting the number of inverted (out-of-order) pairs of values.
For example, in the sequence :math:`1,3,2,5,6,4,8`, there are the pairs :math:`(3,2), (5,4), (6,4)`
which are unordered. Justify the complexity of your algorithm and give its pseudocode.

.. tip::

    Assume two arrays :math:`A` and :math:`B`, let :math:`A.B` be the array resulting from the
    concatenation of :math:`A` and :math:`B`. Let :math:`nUnsorted(A)` be the number of unsorted pairs
    in an array :math:`A`.

    We have the following property that you can prove:

    .. math::

        nUnsorted(A.B) = nUnsorted(A)+ nUnsorted(B)+|\{(i,j) : A[i]>B[j]\}|


    What is the complexity of calculating :math:`|\{(i,j) : A[i]>B[j]\}|`?
    Can this complexity be improved if :math:`A` and :math:`B` are sorted?
    Could you compute :math:`nUnsorted` based on some adaptation of a well-known sorting algorithm
    that runs in :math:`\mathcal{O}(n \cdot \log(n))`?


.. answer::

    L'algorithme demandé est en fait basé sur le même principe que le merge sort.

    L'idée est que calculer :math:`|\{(i,j) : A[i]>B[j]\}|` "bètement" est en :math:`\mathcal{O}(n^2)`.
    Remarquez que si on trie A et B, cela ne change pas le résultat.
    Il existe un algorithme en :math:`\mathcal{O}(n)` si A et B sont triés:

    .. code-block:: java

        int wrongOrder(int[] A, int [] B) {
            // A et B sont des tableaux triés dans l'ordre croissant
            int posB = B.length;
            int count = 0;
            for (int i = A.length - 1; i >= 0; i--) {
                while(posB != 0 && B[posB-1] >= A[i])
                    posB--;
                count += posB;
            }
            return count;
        }

    Faites un dessin au tableau avec un exemple de deux tableaux triés et des nombres aléatoires (1, 3, 4, 7 et 2, 5, 6, 8 font le job).
    L'idée est donc de faire un merge-sort. On peux coder la fonction comme suit:

    * Appeler la fonction récursivement sur la première moitié du tableau (cela trie la première moitié et retourne ``nUnsorted(A)``)
    * idem sur la seconde moitié (cela trie + calcule ``nUnsorted(B)``)
    * calculer `wrongOrder(A, B)`
    * effectuer le merge du merge sort, ce qui trie le tableau complet.    

Exercise 2.1.7
""""""""""""""

Imagine that we want to sort a collection of `Person` objects lexicographically by their (weight, age, height)
and also `Student` objects by their (age, grade, year). How can you avoid duplicating the sorting algorithm
specifically for these classes?

Explain why the `Comparable` and `Comparator` interfaces in Java are useful for this.
Explain how you would implement an efficient `Comparator` for `String`.


.. answer::

    La méthode `Collections.sort` permet de donner un comparator, suffit de faire un comparator custom pour l'ordre lexicographique spécifié.


Exercise 2.1.8
""""""""""""""

Is it possible to get a stable sort starting from an unstable sorting algorithm? How?


.. answer::

    On peut englober la valeur à trier dans un objet qui contient sa "position", et faire un tie-break dans
    la fonction de comparaison.

Exercise 2.1.9
""""""""""""""

How would you find the 3rd smallest value in an array of one million `int` values?
What is the time complexity of your algorithm?


.. answer::

    Les étudiants doivent tomber sur un algorithme linéaire qui maintien les 3 plus petits nombres, de la même manière
    que l'on calcule un minimum.

    Quid de trouver la 5ième plus petite?
    Et la 10ième?
    Et la 100ième?




Exercise 2.1.10 (INGInious: Median)
"""""""""""""""""""""""""""""""""""

How would you get the median of an array of values (i.e., the :math:`\frac{n}{2}`-th value)?
What is the time complexity of your algorithm?

Solve the related INGInious task `Median <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Median>`_.

.. tip::

    What can you infer regarding the position of the median after the partitioning operation
    around a pivot value :math:`v` in the QuickSort algorithm?



.. answer::

    Clairement, l'algorithme présenté à la question 2.1.9 n'est pas linéaire si la position à trouver est dépendente
    de la taille du tableau, mais quadratique.

    Une solution simple, auquelle les étudiants doivent penser, est de simplement trier le tableau. :math:`\mathcal{O}(n\log n)`.

    L'astuce ci-dessus propose une autre algorithme, qui s'appelle quick-select.
    L'idée est qu'une fois un pivot de quicksort est effectué, le pivot est placé à l'endroit correct.
    Si :math:`n/2` est > que la position du pivot, alors continuer uniquement à droite, sinon uniquement à gauche.

    Comme quick-sort, quick-select est :math:`\Theta(n^2)` dans le pire cas, mais en moyenne, il est en :math:`\mathcal{O}(n)`.


Exercise 2.1.11
"""""""""""""""

What is Autoboxing and Unboxing in Java?
How can this impact the performance of a sorting algorithm?

Compare the performance of ``Arrays.sort`` on an array of 10,000,000 entries consisting of ``int`` and
the same array with ``Integer``.


Exercise 2.1.12
"""""""""""""""

What is a code *profiler*?
What information provided by a profiler could you use to improve
the performance of your algorithms and data structures in general (speed, memory, GC)?

A good free profiler is VisualVM.

Use VisualVM on your code for the previous question.

.. answer::

    Si les étudiants ont leur ordinateur sur eux, vérifiez qu'ils ont installé visualvm et savent s'en servir.



Exercise 2.1.13 (INGInious: Merge Sort)
"""""""""""""""""""""""""""""""""""""""

Complete (without reading the book since you won't have it during the exam) the implementation of `Merge Sort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MergeSort>`_.

Exercise 2.1.14 (INGInious: A Photographer problem)
"""""""""""""""""""""""""""""""""""""""""""""""""""

Help the photographer arrange players of two soccer teams so that everybody is visible in the picture (exam 2022): `Photo <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Photo>`_.

Exercise 2.1.15 (INGInious: An Olympic Problem)
"""""""""""""""""""""""""""""""""""""""""""""""

Help the Olympic Games organizers compute the number of training rooms (exam 2024): `TrainingSessions <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_TrainingSessions>`_.


Exercise 2.1.16 (INGInious: Fix QuickSort)
""""""""""""""""""""""""""""""""""""""""""
It seems that this QuickSort implementation does not always have the expected time complexity.
Help us improve it: `FixQuickSort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_FixQuickSort>`_.



