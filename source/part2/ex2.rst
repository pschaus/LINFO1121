.. _part2_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W5.


Union of Intervals
""""""""""""""""""

Write a method that takes an array of intervals as input and returns the union of those intervals as an array of disjoint intervals.
What is the time complexity of your method?

Solve the corresponding task on INGInious: `Union intervals <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Union>`_.

.. answer::

    There are two classic :math:`\Theta(n \log n)` approaches:

    * **Method 1 (Interval Sorting & Greedy Merge)**:

      1. Sort the intervals in ascending order of their start point ``min`` (and ascending ``max`` on ties) in :math:`\mathcal{O}(n \log n)` time.
      2. Maintain the current merged interval ``[curMin, curMax]`` initialized to the first interval.
      3. Iterate through each subsequent interval ``[a, b]``:

         * If ``a <= curMax`` (overlapping or adjacent), extend the current interval: ``curMax = Math.max(curMax, b)``.
         * Otherwise (``a > curMax``), emit ``[curMin, curMax]`` to the result list and start a new active interval ``[curMin, curMax] = [a, b]``.
      4. Emit the final active interval at the end of the loop (:math:`\Theta(n)` scan).

    * **Method 2 (Sweep-Line Events)**:
      Create :math:`2n` events: ``(min[i], +1)`` for each interval opening and ``(max[i], -1)`` for each closing. Sort events by coordinate (breaking ties by placing ``+1`` before ``-1``) and sweep left-to-right while maintaining a counter ``overlap`` of currently open intervals. A merged interval begins when ``overlap`` transitions from ``0`` to ``1`` and ends when ``overlap`` returns to ``0``.


Three-Value Array Sorting
"""""""""""""""""""""""""

You need to sort a large array containing only values in the set ``{0, 1, 2}``.
What sorting algorithm do you suggest? Write the code.
What is the time complexity to sort the array? Discuss this complexity with respect to the lower bound for comparison-based sorting algorithms (Proposition I, pages 280-281).

.. answer::

    We can use either **Counting Sort** (two passes: count the frequencies of ``0``, ``1``, and ``2``, then overwrite the array) or **Dijkstra's 3-way partitioning (Dutch National Flag)** in a single pass with :math:`\Theta(1)` extra memory:

    .. code-block:: java

        public static void sort012(int[] a) {
            int lo = 0, i = 0, hi = a.length - 1;
            while (i <= hi) {
                if (a[i] == 0) {
                    int tmp = a[lo]; a[lo] = a[i]; a[i] = tmp;
                    lo++; i++;
                } else if (a[i] == 2) {
                    int tmp = a[i]; a[i] = a[hi]; a[hi] = tmp;
                    hi--;
                } else {
                    i++;
                }
            }
        }

    * **Time complexity**: :math:`\Theta(n)` time and :math:`\Theta(1)` space.
    * **Why doesn't this violate the :math:`\Omega(n \log n)` comparison-based sorting lower bound?**
      Proposition I in the textbook states that sorting :math:`n` arbitrary **distinct** keys requires :math:`\ge \log_2(n!) \sim n \log_2 n` comparisons because there are :math:`n!` possible permutations to distinguish. Here, the values come from a fixed universe of size :math:`k = 3`, so there are at most :math:`3^n` inputs and the decision tree needs only :math:`\mathcal{O}(n)` branches (or in Counting Sort, we use key values directly as array indices rather than purely pairwise comparisons).


Finding the Mode of an Array
""""""""""""""""""""""""""""

The mode of an array of numbers is the number that appears most frequently in the array. For example, ``[4, 6, 2, 4, 3, 1]`` has mode 4. Give an efficient algorithm to calculate the mode of an array of :math:`n` numbers. What if we know that the array only contains values from 0 to :math:`k`?

.. answer::

    * **General case**:

      1. **Sort then scan** (:math:`\Theta(n \log n)` time, :math:`\mathcal{O}(1)` extra space): Sort the array so identical values are contiguous, then perform a single linear scan tracking the length of the longest run of identical elements.
      2. **3-way QuickSort with pruning**: During 3-way partitioning around a pivot :math:`v`, all occurrences of :math:`v` are grouped together in :math:`[\text{lt} \dots \text{gt}]`, giving the exact frequency :math:`\text{gt} - \text{lt} + 1` of :math:`v`. We update the best candidate mode found so far, and only recurse on the left or right partition if its size strictly exceeds the frequency of the current best mode.

    * **Bounded values in** :math:`\{0, \dots, k\}`:
      Use a frequency array ``int[] count = new int[k + 1]`` (as in Counting Sort), increment ``count[a[i]]`` for each element, and return the index with the maximum count in :math:`\Theta(n + k)` time and :math:`\Theta(k)` space.


Two-Sum Across Two Sets
"""""""""""""""""""""""

Given two sets :math:`S_1` and :math:`S_2` (each of size :math:`n`), and a target number :math:`x`. Describe an efficient algorithm to find if there is a pair :math:`(a,b)` with :math:`a \in S_1, b \in S_2` such that :math:`a+b=x`.
What is the time complexity of your algorithm? What if the sets are already given in sorted arrays?

.. answer::

    * **Unsorted arrays**: Sort :math:`S_2` in :math:`\mathcal{O}(n \log n)` time. Then for each :math:`a \in S_1`, search for :math:`b = x - a` in :math:`S_2` using binary search in :math:`\mathcal{O}(\log n)` time. Total time complexity: :math:`\mathcal{O}(n \log n)`.
    * **Already sorted arrays**: Use a **two-pointer** scan in :math:`\mathcal{O}(n)` time: start with :math:`i = 0` (smallest element of :math:`S_1`) and :math:`j = n - 1` (largest element of :math:`S_2`). While :math:`i < n` and :math:`j \ge 0`:

      * If :math:`S_1[i] + S_2[j] == x`, return ``true``.
      * If :math:`S_1[i] + S_2[j] < x`, increment :math:`i`.
      * If :math:`S_1[i] + S_2[j] > x`, decrement :math:`j`.


Two-Sum in a Single Set
"""""""""""""""""""""""

Same question as above, but for a single set. What if the set is already given in a sorted array?

.. answer::

    * **If the array is already sorted**: Use two pointers :math:`i = 0` and :math:`j = n - 1` moving toward each other. At each step, compare :math:`a[i] + a[j]` with :math:`x`: if equal, return ``true``; if smaller, increment :math:`i`; if larger, decrement :math:`j`. Because :math:`i` only increases and :math:`j` only decreases, this runs in :math:`\mathcal{O}(n)` time and :math:`\mathcal{O}(1)` space.
    * **If the array is unsorted**: First sort the array in :math:`\mathcal{O}(n \log n)` time, then apply the :math:`\mathcal{O}(n)` two-pointer scan, for an overall complexity of :math:`\mathcal{O}(n \log n)`.


Union of Two Sorted Sets
""""""""""""""""""""""""

Give an algorithm to compute the union of two sets :math:`A` and :math:`B`.
Suppose next that the already sorted set :math:`A` has size :math:`n` and the already sorted set :math:`B` has size :math:`n^2`. What would be the time complexity of your algorithm? Would your algorithm change?

.. answer::

    * **General unsorted sets of sizes** :math:`m` **and** :math:`n`: Sort both sets (:math:`\mathcal{O}(m \log m + n \log n)`) and then merge them using two pointers while skipping duplicates in :math:`\mathcal{O}(m + n)` time.
    * **Already sorted sets with** :math:`|A| = n` **and** :math:`|B| = n^2`:

      * Explicitly outputting all elements of :math:`A \cup B` into a new array requires at least :math:`\Omega(n^2)` time simply to copy the :math:`n^2` elements of :math:`B`, which a linear two-pointer merge achieves in :math:`\Theta(n + n^2) = \Theta(n^2)` time.
      * However, if we only want to find which elements of :math:`A` are not already in :math:`B` (or represent the union implicitly / append missing elements to :math:`B`), we can run a **binary search** in :math:`B` for each of the :math:`n` elements of :math:`A`, which takes only :math:`\mathcal{O}(n \log(n^2)) = \mathcal{O}(n \log n)` comparisons instead of :math:`\Theta(n^2)`.


Searching in a Sorted Matrix
""""""""""""""""""""""""""""

Given an :math:`n \times m` matrix of integers where rows and columns are sorted, how do you find a given number in the matrix efficiently?
Hint: There is an :math:`\mathcal{O}(n+m)` time algorithm. To do this, start in the upper-right corner and compare the element with the target number. Which parts of the matrix can you prune from your search based on the result?

.. answer::

    Start at the **top-right corner** :math:`(i, j) = (0, m - 1)` and compare :math:`T[i][j]` with the target value :math:`v`:

    * If :math:`T[i][j] == v`, the element is found.
    * If :math:`T[i][j] < v`, then since row :math:`i` is sorted in ascending order, all elements to the left in row :math:`i` are also :math:`< v`; we can eliminate row :math:`i` and move down: ``i++``.
    * If :math:`T[i][j] > v`, then since column :math:`j` is sorted in ascending order, all elements below in column :math:`j` are also :math:`> v`; we can eliminate column :math:`j` and move left: ``j--``.

    Each comparison eliminates either an entire row or an entire column, so the algorithm performs at most :math:`n + m` steps and runs in :math:`\mathcal{O}(n + m)` time.


Global Warming
""""""""""""""

Design an algorithm to compute the number of entries greater than or equal to a given value :math:`v_1` in an :math:`n \times n` matrix of integers.
What if you need to recompute it for a different value :math:`v_2`?
Do you need to redo the computation from scratch, or can some precomputation be done to answer queries more efficiently?

INGInious task: `Global Warming <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_GlobalWarmingImpl>`_.

.. answer::

    * **For a single query**: Scanning all :math:`n^2` entries of the matrix takes :math:`\Theta(n^2)` time.
    * **For multiple queries (with precomputation)**: Flatten the :math:`n \times n` matrix into a 1D array of size :math:`N = n^2` and sort it once in the constructor in :math:`\mathcal{O}(n^2 \log n)` time. Then, each query for a water level :math:`v` can find the first index :math:`idx` where :math:`\text{array}[idx] \ge v` using **binary search** in :math:`\mathcal{O}(\log(n^2)) = \mathcal{O}(\log n)` time, returning :math:`n^2 - idx`.


Radix Sort
""""""""""

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

    1. **Time complexity**: :math:`\Theta(w \cdot n)` where :math:`n` is the number of elements and :math:`w \le 32` is the number of bits inspected.
    2. **Starting from the MSB**: No, a flat loop from MSB to LSB would overwrite the ordering established by more significant bits! Sorting from MSB to LSB requires recursively partitioning each sub-bucket independently (MSD Radix Sort). LSB-to-MSB (LSD Radix Sort) works precisely because each pass uses a **stable** sort, preserving the relative order established by all lower-order bits.
    3. **Stable sort per bit**: Key-indexed counting (Counting Sort with radix :math:`R = 2`), which runs in :math:`\Theta(n)` time using an auxiliary array of size :math:`n`. An in-place stable alternative such as Insertion Sort or Bubble Sort would avoid the auxiliary array but degrade the time complexity to :math:`\mathcal{O}(w \cdot n^2)`.
    4. **Handling negative numbers**: In 32-bit two's complement representation, the most significant bit (bit 31) is the sign bit: ``1`` for negative numbers and ``0`` for non-negative numbers, and negative numbers are ordered from ``100...0`` (``Integer.MIN_VALUE``) to ``111...1`` (``-1``). Thus, on the 31st bit pass (the sign bit), you simply place numbers with bit ``1`` **before** numbers with bit ``0`` (or flip the sign bit ``x ^ 0x80000000`` before and after sorting).


Aggregate, January 2023
"""""""""""""""""""""""

INGInious task: `Aggregate <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Aggregate>`_.
