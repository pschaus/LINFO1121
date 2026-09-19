.. _part2_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W5.


Exercise 2.2.1 (INGInious: Union of Intervals)
""""""""""""""""""""""""""""""""""""""""""""""

Write a method that takes an array of intervals as input and returns the union of those intervals as an array of disjoint intervals. 
What is the time complexity of your method?


Solve the corresponding task on INGInious: `Union intervals <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Union>`_.

.. answer::

    This problem can be elegantly solved
    with a sweep-line algorithm.
    Create a sequence composed of (a,b) pairs:
    ``S=(min[0],+1),(max[0]+1,-1),...,(min[n-1],+1),(max[n-1]+1,-1),(+inf,0)``.
    Sort the sequence lexicographically:

    - increasingly in 'a',
    - decreasingly in 'b'

    Then use this code:

    .. code-block::

        int start = S[0].min
        overlap = S[0].b // always +1
        union = {}
        int i = 1
        while (i < 2n) {
          overlap += S[i].b
          if (overlap == 0) {
            // closed interval
            union.append([start..S[i].a])
            start = S[i+1].a // fine because we have a dummy element at 2n
          }
          i += 1
         }
        }

    Les étudiants ne trouvent généralement pas cet algorithme (qui est tout de même intéressant de leur montrer).
    Voici l'algorithme trouvé par les étudiants:

    - trier les intervalles (a,b) sur base du start (a).
    - considérer chaque intervalle en maintenant la fermeture candidate maximum (b)

    Si on rencontre un start plus grand que cette fermeture candidate la plus loin, on ferme l'intervalle courant.

Exercise 2.2.2
""""""""""""""

You need to sort a large array containing only values in the set ``{0, 1, 2}``.
What sorting algorithm do you suggest? Write the code.
What is the time complexity to sort the array? Discuss this complexity with respect to the lower bound for comparison-based sorting algorithms (Proposition 1, pages 280-281).

.. answer::

    Il s'agit d'un bucket-sort. Pourquoi est-il en :math:`\mathcal{O}(n)` et pas en :math:`\mathcal{O}(n\log n)`?
    N'y a t'il pas une preuve dans le livre disant que tout tri est en :math:`\mathcal{O}(n\log n)` pourtant?

Exercise 2.2.3
""""""""""""""

The mode of an array of numbers is the number that appears most frequently in the array. For example, [4, 6, 2, 4, 3, 1] has mode 4. Give an efficient algorithm to calculate the mode of an array of :math:`n` numbers. What if we know that the array only contains values from 0 to :math:`k`?

.. answer::

    Solution1: two steps a) Sort all the elements then 2) find the repeating value with the largest span in the sorted array.
    Solution2 (advanced): You can embed the discovery of the mode in a quick-sort. During the pivoting step, we count the number of elements equal to the pivot value and keep track of the current best candidate mode (and its frequency of course). This information can be used to avoid some recursive calls: we only process (recursive quick-sort call) a partition if is it larger than the count of the best candidate mode found so far.

    The students probably won't think about this solution, but you can give them some hints: Can we count the frequency of one value during the pivoting? Can we keep track of the current best mode such that at the end of the quicksort we have the mode and don't need to scan again the sorted elements? Assume that the current best mode has a count of 10, is it worth searching for a mode in a partition of size 5?

    If we know that the range of values is between 0 to k, we can use a counting array and simply return the index with the max counter.

Exercise 2.2.4
""""""""""""""

Given two sets :math:`S_1` and :math:`S_2` (each of size :math:`n`), and a target number :math:`x`. Describe an efficient algorithm to find if there is a pair :math:`(a,b)` with :math:`a \in S_1, b \in S_2` such that :math:`a+b=x`.
What is the time complexity of your algorithm? What if the sets are already given in sorted arrays?

.. answer::

    Sort one of the sets (which takes :math:`\mathcal{O}(n \log n)`).
    Then for each value :math:`v` in the first (unsorted) set,
    search for the value :math:`x-v` in the second sorted array using binary search.
    This overall complexity is :math:`\mathcal{O}(n\log n)`.

    If both arrays are sorted, we can be a bit smarter.
    Instead of iterating over each element in the first array,
    we can use two pointers from both ends in :math:`\mathcal{O}(n)`.

Exercise 2.2.5
""""""""""""""

Same question as above, but for a single set. What if the set is already given in a sorted array?

.. answer::

    If the array is sorted, you can use two pointers :math:`i, j` starting from both ends of the array: :math:`i=0, j=n-1`.
    For each position :math:`i`, find :math:`j` such that :math:`a[i]+a[j]\ge x` and :math:`a[i]+a[j-1] < x`, then increment :math:`i`.
    Since you can advance :math:`j` monotonically, the time complexity is :math:`\mathcal{O}(n)`.

Exercise 2.2.6
""""""""""""""

Give an algorithm to compute the union of two sets :math:`A` and :math:`B`. 
Suppose next that the already sorted set :math:`A` has size :math:`n` and the already sorted set :math:`B` has size :math:`n^2`. What would be the time complexity of your algorithm? Would your algorithm change?

.. answer::

    Let :math:`m` and :math:`n` be the sizes of the sets.
    Solution 1: Put all the elements in a large array then sort it => :math:`\mathcal{O}((m+n)\log(m+n))`.
    Solution 2 (faster): Sort each set separately then merge while avoiding duplicates: :math:`\mathcal{O}(m\log m + n\log n)`.
    For sizes :math:`n` and :math:`n^2`:
    For each element of the small set, do a binary search on the large set. The time complexity is thus :math:`n \log(n^2) = 2n \log n`.
    This is better than the alternative, which would be :math:`n^2 \log n`.


Exercise 2.2.7
""""""""""""""

Given an :math:`n \times m` matrix of integers where rows and columns are sorted, how do you find a given number in the matrix efficiently?
Hint: There is an :math:`\mathcal{O}(n+m)` time algorithm. To do this, start in the upper-right corner and compare the element with the target number. Which parts of the matrix can you prune from your search based on the result?

.. answer::

    Let :math:`(i,j)` initialized as :math:`(0,m-1)` be the current row/column position and :math:`v` the target value.
    If :math:`T[i,j-1] < v` increment :math:`i`, else decrement :math:`j`. Complexity is :math:`\mathcal{O}(n+m)` since in the worst case
    we traverse until :math:`i=n, j=0` if the element is not found.




Exercise 2.2.8 (INGInious: Global Warming)
""""""""""""""""""""""""""""""""""""""""""

Design an algorithm to compute the number of entries greater than or equal to a given value :math:`v_1` in an :math:`n \times n` matrix of integers. 
What if you need to recompute it for a different value :math:`v_2`? 
Do you need to redo the computation from scratch, or can some precomputation be done to answer queries more efficiently?

INGInious task: `Global Warming <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_GlobalWarmingImpl>`_.


.. answer::

    Il faut stocker chaque entrée de la matrice dans un grand tableau de taille n^2 qu'on trie (preprocessing en O(n^2 \log n)).
    Ensuite il est très facile de retrouver le nombre d'éléments >= à une valeur v donnée par simple recherche dichotomique dans ce tableau.


Exercise 2.2.9 (INGInious: Radix Sort)
""""""""""""""""""""""""""""""""""""""

Every integer is encoded using 32 bits in Java.
An integer can thus be seen as a string of 32 bits.
The radix sort algorithm is a version of string sort that starts with the least significant bit rather than the most significant bit (unlike MSD sort, page 710).

Complete the partial implementation for sorting an array of integers using radix sort.

INGInious task: `Radix Sort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_RadixSort>`_.


While implementing this algorithm, answer the following questions:

1. What is the time complexity of this algorithm?
2. Would the radix sort algorithm as implemented also work by starting from the most significant bit rather than from the least significant bit?
3. What stable sorting algorithm did you choose in your implementation? What is its time complexity? Do you know another algorithm that could be used without requiring an auxiliary array?
4. How would you adapt the radix sort implementation to sort numbers that may be positive or negative (be careful about the way negative numbers are represented bitwise)? 



.. answer::

   The algorithm runs in :math:`\mathcal{O}(n\cdot k)` where :math:`n` is the size of the array and :math:`k` is the index of the most significant bit used among all numbers.
   We could use insertion sort or bubble sort instead of counting sort as an alternative that does not use auxiliary arrays, but the worst-case time complexity is then :math:`\mathcal{O}(k\cdot n^2)`.
   No, we cannot simply use the same outer loop starting from the most significant bit without recursive partitioning (as in MSD), because we need to preserve the relative order of sub-buckets.
   



Exercise 2.2.10 (INGInious: Aggregate, January 2023)
""""""""""""""""""""""""""""""""""""""""""""""""""""

INGInious task: `Aggregate <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Aggregate>`_.




