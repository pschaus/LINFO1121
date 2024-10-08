.. _part2_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W5.


Exercise 2.2.1 (Inginious: Union of Intervals)
"""""""""""""""""""""""""""""""""""""""""""""""""""

Write a method that takes an array of intervals as input and returns the union of those intervals as an array of disjoint intervals. We consider that the input intervals are given in the form of two arrays `int[] min, int[] max;` where the ith interval is given by ``(min[i],max[i])`` . Example input ``min=[5,0,1,6,2]`` ``max=[7,2,2,8,3]`` would output ``min=[0,5] ,max=[3,8]``.
Write the pseudocode. How complex is your method?


Solve the corresponding taks on Inginious `Union intervals <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Union>`_

.. answer::

    This problem can be elegantly solved
    with a sweep-line approach algorithm.
    Create a sequence composed of (a,b) couples:
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

    Les étudiants ne trouvent généralement pas cet algorithmes (qui est tout de même intéressant de leur montrer).
    Voice l'algorihtme trouvé par les étudiants:

    - trier les intervalles (a,b) sur base du start (a).
    - considèrer chaque intervalle en maintenant la fermeture candidate maximum (b)

    Si on rencontre un start, plus grand que cette fermeture candidate la plus loin, on ferme l'intervalle courant.

Exercise 2.2.2
"""""""""""""""

You need to sort a large array that has the property that it only contains values in the set ``{0,1,2}``.
What sorting algorithm do you suggest? Write the code.
How complex will it be to sort the array? Discuss this complexity with respect to the lower bound of a sorting algorithm (Proposition 1 pages 280-281).

.. answer::

    Il s'agit d'un bucket-sort. Pourquoi est-il en :math:`\mathcal{O}(n)` et pas en :math:`\mathcal{O}(n\log n)`?
    N'y a t'il pas une preuve dans le livre disant que tout tri est en :math:`\mathcal{O}(n\log n)` pourtant?

Exercise 2.2.3
"""""""""""""""

The mode of a table of numbers is the number that appears most frequently in the table. For example (4,6,2,4,3,1) has mode 4. Give an efficient algorithm to calculate the mode of an array of :math:`n` numbers. What if we know that the array only contains values from 0 to :math:`k`?

.. answer::

    Solution1: two steps a) Sort all the elements then 2) find the repeating value with the largest span in the sorted array.
    Solution2 (advanced): You can embed the discovery of the mode in a quick-sort. During the pivoting step, we count the number of elements equal to the pivot value and keep track of the current best candidate mode (and its frequency of cours). This information can be used to avoid some recursive calls: we only process (recursive quick-sort call) a partition if is it larger than the count of the best candidate mode found so far.

    The students wont probably think about this solution but you can give them some hints: Can we cound the frequency of one value during the pivoting ? Can we keep track of the current best mode such that at the end of the quicksort we have the mode and don't need to scan again the sorted elements ? Assume that current best mode is has a count of 10, is it worth searching for a  mode in a partition of size 5 ?

    If we know that the range of values is between 0 to k, we can use a counting array and simply return the index with the max counter.

Exercise 2.2.4
"""""""""""""""

Given two sets :math:`S_1` and :math:`S_2` (each of size :math:`n`), and a number :math:`x`. Describe an efficient algorithm to find if there is a pair :math:`(a,b)` with :math:`a \in S_1,b \in S_2` such that :math:`a+b=x`.
What is the time complexity of your algorithm? What if the sets are in already sorted arrays?

.. answer::

    Sort one of the sets one array (already takes :math:`\mathcal{O}(n \log(n))`).
    Then for each value :math:`v` in the first (unsorted) set,
    search for the value :math:`x-v` in the second sorted array using a dichotomic search.
    Again this complexity is :math:`\mathcal{O}(n\log(n))`.

    If both array are sorted, we can be a bit smarter.
    Instead of iterating over each element in the first array
    we can also do a dichotomic seach on that one based on the minimum/maximum.
    If for a value :math:`v`, the minimum of the second array plus :math:`v` is :math:`>x`
    then we know that it is not worth considereing values :math:`>v` in the first array.
    This amounts at shrinking the bound of values in the first array.
    This doesn't change the worst-case time complexity
    but can reduce the best-case time complexity to :math:`\mathcal{O}(\log(n))`.

Exercise 2.2.5
"""""""""""""""

Same question as the previous one but for a single set. What if the set is in an already sorted array?

.. answer::

    If the array is sorted, you can use two pointers :math:`i,j` starting from both extremities the array :math:`i=0,j=n-1`.
    For each position :math:`i`, find :math:`j` such that :math:`a[i]+a[j]\ge v` and :math:`a[i]+a[j-1] < v` then increment :math:`i`.
    Since you can start the search for :math:`j` from its previous position, the complexity is :math:`\mathcal{O}(n)`.

Exercise 2.2.6
"""""""""""""""

Give an algorithm to calculate the union of two sets :math:`A` and :math:`B`. 
Suppose in a second step that the already sorted set :math:`A` has a size :math:`n` and the also sorted set :math:`B` has a size :math:`n^2` . What would be the time complexity of you algorithm, does your algorithm change?

.. answer::

    Let :math:`m` and :math:`n` be the size of the sets.
    Solution1: Put all the element in a large array then sort it => :math:`\mathcal{O}((m+n)log(m+n))`.
    Solution2 (a bit faster): Sort each set separately then collect avoiding dupplicates:  :math:`\mathcal{O}(m\log(m)+n\log(n))`.
    For the :math:`n` and :math:`n^2` size.
    For each element of the small one you do a dichotomic search on the large one. The time complexity is thus :math:`n \log(n^2) = 2n \log n`.
    This is better than the opposite which would be :math:`n^2 log(n)`.


Exercise 2.2.7
""""""""""""""""""""""""""""

Given a matrix of integers that are sorted along rows and columns, how do you find a given number in the matrix efficiently?
Hint: There is a :math:`\mathcal{O}(n+m)` time algorithm for a :math:`n\times m` matrix. To do this, start in the upper right corner and compare with the number you are looking for. Which parts of the matrix can you prune in your search based on the result?

.. answer::

    Let :math:`(i,j)` initialized as :math:`(0,m-1)` the current row/column position and :math:`v` the number we are looking for.
    If :math:`T[i,j-1] < v` increment :math:`i` else decrement :math:`j`. Complexity :math:`\mathcal{O}(n+m)` since it the worst case
    we go until :math:`i=n,j=0` if the element is not found.




Exercise 2.2.8 (Inginious: Global Warming)
"""""""""""""""""""""""""""""""""""""""""""

Design an algorihtm to compute the number of entries larger or equal to a given value :math:`v_1` in n x n matrix of integers. 
What if you need to recompte it for a different value :math:`v_2`? 
Do you need to redo the computation from scratch or some pre-computation can be done do it more efficiently?

Inginious task: `Global Warming <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_GlobalWarmingImpl>`_


.. answer::

    Il faut stocker chaque entree de la matrice dans un grand tableau de taille n^2 qu'on trie (preprocessing en O(n.log(n))).
    Ensuite il est très facile de retrouver le nombre d'élément >= à une valeur v donnée par simple recherche dichotomique dans ce tableau.


Exercise 2.2.9 (Inginious: Radix Sort)
"""""""""""""""""""""""""""""""""""""""""""

Every integer is encoded on 32 bits in Java.
An integer can thus be seen as a string of 32 bits.
The radix-sort algorithm is version of string sort that start with the least significant bit rather than the most sigfificant bit (as for MDS pp. 710).

Complete the partial implementation for sorting an array of integers using radix sort.

Inginious task: `Radix Sort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_RadixSort>`_


While implementing this algorithm try to answer the following questions:

1. What is the time-complexity of this algorithm?
2. Would the radix sort  algorithm as implemented also  work by starting from the most signficant bit rather than from the least significant bit?
3. What stable sort algorihtm did you choose in your implementation? What it its time complexity? Do you know another algorithm that could be used without requiring an auxiliary array?
4. How to adapt the radix-sort implementation to sort  number that may be positive or negative (be carefull about the way an negative number is represented bitwise)? 



.. answer::

   The algorihtm runs in :math:`O(n\cdot k)` where n is the size of the array and k is index of the most significant bit used among all the numbers.
   We could use insertion sort or bubble sort instead of couting sort as an alternative not using auxiliary arrays but the worst-case time complexity is then :math:`O(k\cdot n^2).`
   No we cannot use the same outer-loop to start from the most significant bit. If we do that like for MDS, we need a low and hi profile to keep the relative order of alrady most significant bits that are already sorted.
   



Exercise 2.2.10 (Inginious: Aggregate, january 2023)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Inginious task: `Aggregate <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Aggregate>`_




