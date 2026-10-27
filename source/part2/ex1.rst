.. _part2_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W4.


Search and Insertion in a Sorted Sequence
"""""""""""""""""""""""""""""""""""""""""

Given an array containing :math:`n` sorted integers, and a number :math:`x` to insert into the array, can you
describe an algorithm to find the position where :math:`x` should be inserted while keeping the array sorted?

What is the time complexity of this algorithm?
Does your algorithm also work for a sorted linked list? With what complexity?

.. answer::

    * **For a sorted array**:

      * **Linear scan**: scan from left to right until finding the first element :math:`\ge x`, which takes :math:`\mathcal{O}(n)` comparisons.
      * **Binary search**: repeatedly halve the search interval :math:`[\text{lo}, \text{hi}]` by comparing :math:`x` with the middle element ``a[mid]`` in :math:`\mathcal{O}(1)` time. Finding the insertion index takes :math:`\Theta(\log n)` comparisons in the worst case (note: actually shifting the subsequent array elements to insert :math:`x` still takes :math:`\mathcal{O}(n)` array writes).

    * **For a sorted linked list**:

      * Binary search **does not improve the complexity** on a linked list because accessing the middle element requires traversing :math:`\Theta(n)` links (there is no :math:`\mathcal{O}(1)` random access by index). Therefore, you must perform a sequential scan from the head of the list in :math:`\mathcal{O}(n)` time (once the position is found, splicing the new node in takes :math:`\Theta(1)` time).


Optimal Job Scheduling
""""""""""""""""""""""

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

    **Proof by contradiction (Exchange Argument)**:
    Minimizing the average completion time is equivalent to minimizing the total completion time:

    .. math::

        C = \sum_{i=0}^{n-1} \left( \sum_{j=0}^i t_j \right)

    Suppose for the sake of contradiction that an optimal schedule :math:`S` is **not** sorted in non-decreasing order of durations. Then there must exist at least one adjacent pair of jobs at positions :math:`a` and :math:`a+1` such that :math:`t_a > t_{a+1}`.

    Consider the new schedule :math:`S'` obtained by swapping jobs :math:`a` and :math:`a+1`:

    * The completion time of every job before position :math:`a` is unchanged.
    * The completion time of every job after position :math:`a+1` is unchanged (since the sum :math:`t_a + t_{a+1}` is unchanged).
    * In :math:`S`, the sum of completion times for positions :math:`a` and :math:`a+1` is :math:`\left(\sum_{j=0}^{a-1} t_j + t_a\right) + \left(\sum_{j=0}^{a-1} t_j + t_a + t_{a+1}\right)`.
    * In :math:`S'`, the sum of completion times for positions :math:`a` and :math:`a+1` is :math:`\left(\sum_{j=0}^{a-1} t_j + t_{a+1}\right) + \left(\sum_{j=0}^{a-1} t_j + t_{a+1} + t_a\right)`.

    The difference in total completion time between :math:`S'` and :math:`S` is therefore:

    .. math::

        C(S') - C(S) = (2 t_{a+1} + t_a) - (2 t_a + t_{a+1}) = t_{a+1} - t_a < 0

    Thus :math:`C(S') < C(S)`, which contradicts the optimality of :math:`S`. Therefore, any optimal schedule must process jobs in non-decreasing order of :math:`t_j` (Shortest Processing Time first).


Stability and In-Place Sorting
""""""""""""""""""""""""""""""

What is meant by a stable and an in-place sorting algorithm?
For all the algorithms presented in the reference book,
indicate whether they are in-place (or not) and whether they are stable (or not).

Answer the short `INGInious MCQ <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/sorting_property>`_.

.. answer::

    * **Stable**: A sorting algorithm is *stable* if it preserves the relative order of elements that have equal sort keys.
    * **In-place**: A sorting algorithm is *in-place* if it uses only a constant :math:`\mathcal{O}(1)` amount of extra memory (or :math:`\mathcal{O}(\log n)` implicit call-stack space for recursive algorithms like QuickSort) beyond the input array itself.

    .. list-table:: Properties of Classical Sorting Algorithms
       :header-rows: 1

       * - Algorithm
         - In-Place?
         - Stable?
         - Time Complexity (Worst / Average / Best)
       * - Selection Sort
         - Yes (:math:`\mathcal{O}(1)`)
         - No (long-range swaps)
         - :math:`\Theta(n^2)` / :math:`\Theta(n^2)` / :math:`\Theta(n^2)`
       * - Insertion Sort
         - Yes (:math:`\mathcal{O}(1)`)
         - Yes
         - :math:`\Theta(n^2)` / :math:`\Theta(n^2)` / :math:`\Theta(n)`
       * - ShellSort
         - Yes (:math:`\mathcal{O}(1)`)
         - No (:math:`h`-sorts across long distances)
         - :math:`\mathcal{O}(n^{3/2})` (with :math:`3x+1` increments)
       * - Merge Sort
         - No (:math:`\Theta(n)` auxiliary array)
         - Yes
         - :math:`\Theta(n \log n)` / :math:`\Theta(n \log n)` / :math:`\Theta(n \log n)`
       * - QuickSort
         - Yes (:math:`\mathcal{O}(\log n)` stack)
         - No (partitioning swaps non-adjacent keys)
         - :math:`\Theta(n^2)` / :math:`\Theta(n \log n)` / :math:`\Theta(n \log n)`
       * - HeapSort
         - Yes (:math:`\mathcal{O}(1)`)
         - No
         - :math:`\Theta(n \log n)` / :math:`\Theta(n \log n)` / :math:`\Theta(n)` (all equal keys)


Card Sorter
"""""""""""

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

.. answer::

    We can simulate a Bubble Sort / Selection Sort pass over the circular deck of size :math:`n`:
    In round :math:`i` (for :math:`i = 0 \dots n-1`), we want to bubble the largest among the first :math:`n - i` unsorted cards to the back of the unsorted section, and then rotate the :math:`i` already-sorted cards from the front to the back so the entire deck returns to its aligned state:

    .. code-block:: java

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (first > second) {
                    swapFirstTwo();
                }
                moveFirstToBack();
            }
            for (int j = 0; j <= i; j++) {
                moveFirstToBack();
            }
        }

    Each of the :math:`n` outer iterations performs :math:`n` rotations around the deck, so the total time complexity is :math:`\Theta(n^2)`.


Sort Linked List
""""""""""""""""

How can you sort a singly linked list (which does not allow access
to a position by index) efficiently? What is the time complexity of your
algorithm?

Solve the related INGInious task `SortLinkedList <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_SortLinkedList>`_.

Which algorithm is used by the ``sort`` method of the ``List`` interface below?

.. code-block:: java

        LinkedList<Integer> list = new LinkedList<Integer>();
        for (int i = n; i >= 0; i--) {
            list.add(i);
        }
        list.sort(Integer::compare);

.. answer::

    * **Sorting a linked list directly**: **Merge Sort** (either top-down using slow/fast pointers to split the list in half, or bottom-up merging sublists of size :math:`1, 2, 4, 8, \dots`) is the most natural and efficient choice for linked lists. Merging two sorted linked lists requires no auxiliary array (only pointer rewiring in :math:`\mathcal{O}(1)` extra space), and the total time complexity is :math:`\Theta(n \log n)`.
    * **What ``list.sort(...)`` does in Java**: ``List.sort`` copies the elements of the linked list into an Object array (``toArray()``), sorts the array using **TimSort** (an adaptive, stable hybrid of Merge Sort and Insertion Sort running in :math:`\mathcal{O}(n \log n)` worst-case and :math:`\mathcal{O}(n)` best-case time), and then iterates over the list to write the sorted elements back in place.


Counting Inversions
"""""""""""""""""""

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

    This problem can be solved in :math:`\Theta(n \log n)` time by piggybacking on **Merge Sort**.

    Notice that sorting :math:`A` and :math:`B` individually does not change the number of cross-inversions :math:`|\{(i, j) : A[i] > B[j]\}|` between :math:`A` and :math:`B`.
    When :math:`A` and :math:`B` are both sorted in ascending order, we can count all cross-inversions in :math:`\Theta(|A| + |B|)` time during the ``merge`` step: whenever the next element picked comes from the right subarray :math:`B[j]` because :math:`A[i] > B[j]`, then **all** remaining elements :math:`A[i \dots \text{mid}]` in the left subarray are also strictly greater than :math:`B[j]`, contributing :math:`(\text{mid} - i + 1)` inversions at once!

    .. code-block:: java

        public static long countInversions(int[] a, int[] aux, int lo, int hi) {
            if (lo >= hi) return 0;
            int mid = lo + (hi - lo) / 2;
            long count = 0;
            count += countInversions(a, aux, lo, mid);
            count += countInversions(a, aux, mid + 1, hi);
            count += mergeAndCount(a, aux, lo, mid, hi);
            return count;
        }

        private static long mergeAndCount(int[] a, int[] aux, int lo, int mid, int hi) {
            for (int k = lo; k <= hi; k++) aux[k] = a[k];
            int i = lo, j = mid + 1;
            long inversions = 0;
            for (int k = lo; k <= hi; k++) {
                if (i > mid)                   a[k] = aux[j++];
                else if (j > hi)               a[k] = aux[i++];
                else if (aux[j] < aux[i]) {
                    a[k] = aux[j++];
                    inversions += (mid - i + 1); // all aux[i..mid] are > aux[j]
                } else {
                    a[k] = aux[i++];
                }
            }
            return inversions;
        }

    By the Master Theorem, :math:`T(n) = 2T(n/2) + \Theta(n) \implies T(n) \in \Theta(n \log n)`.


Lexicographical Sorting with Comparable and Comparator
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Imagine that we want to sort a collection of ``Person`` objects lexicographically by their (weight, age, height)
and also ``Student`` objects by their (age, grade, year). How can you avoid duplicating the sorting algorithm
specifically for these classes?

Explain why the ``Comparable`` and ``Comparator`` interfaces in Java are useful for this.
Explain how you would implement an efficient ``Comparator`` for ``String``.

.. answer::

    * **Avoiding code duplication**: Sorting algorithms in Java (``Arrays.sort``, ``Collections.sort``) are implemented polymorphically using callbacks via the ``Comparable<T>`` interface (which defines the *natural ordering* of a class via ``compareTo(T other)``) or the ``Comparator<T>`` interface (which defines one or more *custom external orderings* via ``compare(T a, T b)``).
    * **Lexicographical comparator**: In Java 8+, you can chain comparators cleanly:

      .. code-block:: java

          Comparator<Person> byWeightAgeHeight = Comparator
              .comparingDouble(Person::getWeight)
              .thenComparingInt(Person::getAge)
              .thenComparingDouble(Person::getHeight);

    * **Comparator for ``String``**: Compare characters from left to right at index :math:`k = 0 \dots \min(s_1.\text{length}(), s_2.\text{length}()) - 1`. At the first index :math:`k` where :math:`s_1.\text{charAt}(k) \ne s_2.\text{charAt}(k)`, return :math:`s_1.\text{charAt}(k) - s_2.\text{charAt}(k)`. If all compared characters match, return :math:`s_1.\text{length}() - s_2.\text{length}()`. This runs in :math:`\mathcal{O}(\text{LCP}(s_1, s_2) + 1)` time, inspecting only the longest common prefix.


Making Any Sorting Algorithm Stable
"""""""""""""""""""""""""""""""""""

Is it possible to get a stable sort starting from an unstable sorting algorithm? How?

.. answer::

    **Yes.** Before sorting, wrap each element :math:`x_i` in a pair/wrapper object ``(value, originalIndex)`` storing its initial position :math:`i \in \{0, \dots, n-1\}` in the input array.
    Then define the comparison function to break ties on ``value`` by comparing ``originalIndex`` in ascending order:

    .. code-block:: java

        int cmp = a.value.compareTo(b.value);
        if (cmp != 0) return cmp;
        return Integer.compare(a.originalIndex, b.originalIndex);

    Since all ``originalIndex`` values are strictly distinct, no two wrapped elements are ever considered equal by the sorting algorithm, forcing equal values to appear in their original relative order at the cost of :math:`\Theta(n)` extra space.


Finding the 3rd Smallest Element
""""""""""""""""""""""""""""""""

How would you find the 3rd smallest value in an array of one million ``int`` values?
What is the time complexity of your algorithm?

.. answer::

    Maintain the three smallest values seen so far (:math:`\text{min}_1 \le \text{min}_2 \le \text{min}_3`, initialized to ``Integer.MAX_VALUE``) in a **single linear pass** over the array, updating them in :math:`\mathcal{O}(1)` per element.
    This runs in :math:`\Theta(n)` time and :math:`\Theta(1)` extra space.

    *Generalization to the :math:`k`-th smallest element*:

    * For small :math:`k`, maintaining a **Max-Heap** of size :math:`k` containing the :math:`k` smallest elements seen so far takes :math:`\mathcal{O}(n \log k)` time and :math:`\mathcal{O}(k)` space.
    * When :math:`k` is proportional to :math:`n` (such as the median :math:`k = n/2`), **QuickSelect** solves the problem in :math:`\mathcal{O}(n)` average time and :math:`\mathcal{O}(1)` extra space (see the *Median* exercise below).


Median
""""""""""

How would you get the median of an array of values (i.e., the :math:`\frac{n}{2}`-th value)?
What is the time complexity of your algorithm?

Solve the related INGInious task `Median <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Median>`_.

.. tip::

    What can you infer regarding the position of the median after the partitioning operation
    around a pivot value :math:`v` in the QuickSort algorithm?

.. answer::

    1. **Sorting approach**: Sort the array in :math:`\mathcal{O}(n \log n)` time and return the element at index :math:`n/2`.
    2. **QuickSelect (Hoare's selection algorithm)**: Partition the array around a pivot as in QuickSort, placing the pivot at its final sorted index :math:`j`.

       * If :math:`j == n/2`, the pivot is the median: return it immediately.
       * If :math:`j > n/2`, recursively partition **only the left subarray** :math:`[\text{lo}, j-1]`.
       * If :math:`j < n/2`, recursively partition **only the right subarray** :math:`[j+1, \text{hi}]`.

       Because QuickSelect recurses on only one side instead of both, its average-case work is :math:`n + \frac{n}{2} + \frac{n}{4} + \dots \le 2n \in \Theta(n)` time, though its worst-case time complexity remains :math:`\Theta(n^2)` if bad pivots are consistently chosen.


Autoboxing, Unboxing, and Sorting Performance
"""""""""""""""""""""""""""""""""""""""""""""

What is Autoboxing and Unboxing in Java?
How can this impact the performance of a sorting algorithm?

Compare the performance of ``Arrays.sort`` on an array of 10,000,000 entries consisting of ``int`` and
the same array with ``Integer``.

.. answer::

    * **Autoboxing and Unboxing**: Autoboxing is the automatic conversion performed by the Java compiler between primitive types (e.g., ``int``, ``double``) and their corresponding object wrapper classes (e.g., ``Integer``, ``Double``). Unboxing is the reverse conversion.
    * **Performance impact on sorting**:
      Sorting ``Integer[]`` is typically **5x to 10x slower** and uses **4x to 6x more memory** than sorting ``int[]`` for three reasons:

      1. **Memory overhead**: An ``int[N]`` uses :math:`4N` bytes in a single contiguous block. An ``Integer[N]`` stores :math:`N` object references (:math:`4N` or :math:`8N` bytes) plus :math:`N` separate ``Integer`` objects on the heap (each costing 16 bytes due to object headers and padding, i.e., :math:`\ge 20N` bytes total).
      2. **Pointer indirection and cache misses**: Comparing two ``int`` values reads contiguous memory inside CPU cache lines. Comparing two ``Integer`` references requires dereferencing pointers to potentially scattered heap locations, causing frequent CPU cache misses.
      3. **Algorithmic difference**: ``Arrays.sort(int[])`` uses an in-place **Dual-Pivot Quicksort** with raw ``<`` comparisons, whereas ``Arrays.sort(Object[])`` uses **TimSort** (which requires auxiliary array allocations and virtual method calls to ``compareTo``).


Code Profiling with VisualVM
""""""""""""""""""""""""""""

What is a code *profiler*?
What information provided by a profiler could you use to improve
the performance of your algorithms and data structures in general (speed, memory, GC)?

A good free profiler is VisualVM.

Use VisualVM on your code for the previous question.

.. answer::

    A **profiler** (such as VisualVM, Java Flight Recorder, or Async-Profiler) is a dynamic analysis tool that monitors a running program to measure where CPU time and memory are spent.
    It provides:

    * **CPU profiling (Hotspots & Call Trees)**: Identifies which methods consume the most execution time (self-time vs. total time) and how often they are invoked, allowing you to focus optimization efforts on the actual bottleneck.
    * **Memory / Heap profiling**: Shows how many instances of each class are allocated on the heap (e.g., revealing millions of ``Integer`` or ``Node`` allocations) and helps detect memory leaks.
    * **Garbage Collection & Thread monitoring**: Displays GC pause frequency, heap usage sawtooth patterns, and thread contention.


Merge Sort
""""""""""

Complete (without reading the book since you won't have it during the exam) the implementation of `Merge Sort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MergeSort>`_.


A Photographer Problem
""""""""""""""""""""""

Help the photographer arrange players of two soccer teams so that everybody is visible in the picture (exam 2022): `Photo <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_Photo>`_.


An Olympic Problem
""""""""""""""""""

Help the Olympic Games organizers compute the number of training rooms (exam 2024): `TrainingSessions <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_TrainingSessions>`_.


Fix QuickSort
"""""""""""""

It seems that this QuickSort implementation does not always have the expected time complexity.
Help us improve it: `FixQuickSort <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_FixQuickSort>`_.
