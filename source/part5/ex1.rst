.. _part5_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W10.


Quick-Find Trace
""""""""""""""""

Give the array ``id[]`` that results from the following sequence of 6 union operations on an initial set of 10 items using the quick-find algorithm:
``3-8, 1-7, 1-8, 9-4, 6-4, 2-0``.
Your answer must be a sequence of 10 integers.
Reminder: the quick-find convention for the union operation ``p-q`` is to change ``id[p]`` (and all other entries with value ``id[p]``) to ``id[q]``.

.. answer::

    ``0 8 0 8 4 5 4 8 8 4``


Weighted Quick-Union Trace
""""""""""""""""""""""""""

Give the array ``id[]`` that results from the following sequence of 9 union operations on an initial set of 10 items using the weighted quick-union algorithm:

``4-6, 3-6, 8-9, 7-0, 1-2, 8-4, 6-5, 1-7, 6-0.``

Your answer must be a sequence of 10 integers. Reminder: When merging two trees of the same size, the weighted quick-union algorithm uses the convention
to point the root of the second tree to the root of the first tree.
Our algorithm uses union by size (number of nodes) and not union by height, nor the path compression technique.

.. answer::

    ``7 4 1 4 4 4 4 1 4 8``


Valid Weighted Quick-Union Trees
""""""""""""""""""""""""""""""""

Which of the following ``id[]`` array(s) could result from applying the weighted quick-union algorithm on an initial set of 10 items?
Reminder: we use union by size (number of nodes), not union by height.

* ``0 8 2 3 4 7 6 8 8 9``
* ``4 2 6 6 2 6 6 2 4 2``
* ``7 0 0 0 0 1 0 5 1 0``
* ``3 3 0 3 0 3 3 3 5 2``
* ``1 3 3 6 4 1 6 0 6 8``

.. answer::

    * ``0 8 2 3 4 7 6 8 8 9`` — **Valid** (only two unions performed: ``1-8`` and ``7-8``).
    * ``4 2 6 6 2 6 6 2 4 2`` — **Invalid**: In weighted quick-union, whenever a node :math:`x` is linked as a child of parent :math:`p`, the size of the tree rooted at :math:`p` must be at least **twice** the size of the subtree rooted at :math:`x`. Here, node ``2`` has subtree size 6 (``{1, 2, 4, 7, 8, 9}``) while its parent ``6`` leads a tree of total size 10 (:math:`10 < 2 \times 6 = 12`), which is impossible.
    * ``7 0 0 0 0 1 0 5 1 0`` — **Invalid**: Contains a cycle ``0 -> 7 -> 5 -> 1 -> 0`` (not a forest of rooted trees).
    * ``3 3 0 3 0 3 3 3 5 2`` — **Valid** (can be obtained by the sequence ``0-4, 3-1, 5-8, 3-6, 5-6, 2-9, 0-2, 9-8, 5-7``).
    * ``1 3 3 6 4 1 6 0 6 8`` — **Invalid**: The maximum tree height in weighted quick-union on :math:`N = 10` elements is :math:`\lfloor \log_2 10 \rfloor = 3`, whereas node ``7`` has depth 4 (``7 -> 0 -> 1 -> 3 -> 6``).


Binary Max-Heap Insertions
""""""""""""""""""""""""""

Give the sequence of keys in the array that results from inserting the sequence of 3 keys 48, 30, and 84
into the following max-oriented heap of size 10:

``97, 93, 89, 83, 38, 32, 40, 12, 26, 24``.

Your answer should be a sequence of 13 integers.

.. answer::

    The final array is: ``97 93 89 83 48 84 40 12 26 24 38 30 32``

    Step-by-step trace after each insertion:

    ========  ==========================================
    start     ``97 93 89 83 38 32 40 12 26 24``
    after 48  ``97 93 89 83 48 32 40 12 26 24 38``
    after 30  ``97 93 89 83 48 32 40 12 26 24 38 30``
    after 84  ``97 93 89 83 48 84 40 12 26 24 38 30 32``
    ========  ==========================================


Binary Max-Heap Deletions
"""""""""""""""""""""""""

Give the sequence of keys in the array that results from performing 3 successive delete-the-maximum operations on the following max-oriented heap of size 10:

``98, 96, 84, 34, 62, 31, 72, 13, 27, 33``.

Your answer should be a sequence of 7 integers.

.. answer::

    The final array is: ``72 62 31 34 33 13 27``

    Step-by-step trace after each ``delMax()``:

    ==========  ========================================
    start       ``98 96 84 34 62 31 72 13 27 33``
    98 deleted  ``96 62 84 34 33 31 72 13 27``
    96 deleted  ``84 62 72 34 33 31 27 13``
    84 deleted  ``72 62 31 34 33 13 27``
    ==========  ========================================


Priority Queue: Binary Heap vs. Sorted List
"""""""""""""""""""""""""""""""""""""""""""

What are the possible advantages and disadvantages of implementing a priority queue with
a heap rather than a list?

.. answer::

    A Priority Queue (PQ) is an ADT that can be implemented with several underlying data structures:

    .. list-table:: Priority Queue Implementations Comparison
       :header-rows: 1

       * - Implementation
         - ``insert``
         - ``delMax``
         - ``max`` (peek)
       * - Unordered List / Array
         - :math:`\Theta(1)`
         - :math:`\Theta(N)`
         - :math:`\Theta(N)`
       * - Ordered List / Array
         - :math:`\Theta(N)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
       * - Binary Heap
         - :math:`\mathcal{O}(\log N)`
         - :math:`\mathcal{O}(\log N)`
         - :math:`\Theta(1)`

    In typical applications where we insert :math:`N` elements and remove :math:`N` elements, both list-based implementations require :math:`\Theta(N^2)` total time, whereas a **binary heap** performs both ``insert`` and ``delMax`` in :math:`\mathcal{O}(\log N)` time, yielding :math:`\mathcal{O}(N \log N)` total time (and compact array storage without node overhead).


Heap Tree Traversals
""""""""""""""""""""

Can you find an example of a valid heap :math:`T` storing 7 distinct elements such that
an inorder traversal of :math:`T` visits the elements in decreasing order?
What about a preorder or postorder traversal?

.. answer::

    Consider a tree of 7 nodes labeled :math:`A` (root), :math:`B, C` (children of :math:`A`), :math:`D, E` (children of :math:`B`), and :math:`F, G` (children of :math:`C`):

    .. image:: heap7.png

    For the elements to be visited in **decreasing** order, the traversal sequence must be strictly decreasing:

    * **Inorder** (:math:`D > B > E > A > F > C > G`): **Impossible** for both a min-heap and a max-heap, because :math:`D > B > E` requires the left child :math:`D` to be larger than parent :math:`B` while the right child :math:`E` is smaller than parent :math:`B`, violating the heap property!
    * **Preorder** (:math:`A > B > D > E > C > F > G`): **Possible for a Max-Heap** (e.g., :math:`A=7, B=6, D=5, E=4, C=3, F=2, G=1`), because every parent is visited before its children and is strictly greater than its children. Impossible for a Min-Heap.
    * **Postorder** (:math:`D > E > B > F > G > C > A`): **Possible for a Min-Heap** (e.g., :math:`D=7, E=6, B=5, F=4, G=3, C=2, A=1`), because every parent is visited after its children and is strictly smaller than its children. Impossible for a Max-Heap.


True/False: Binary Heaps
""""""""""""""""""""""""

Which of the following statements are true for a priority queue implemented as a binary heap?
Assume heaps are max-oriented and 1-indexed.

* In the worst case, inserting a key into a binary heap containing :math:`N` keys requires :math:`\sim \log_2 N` comparisons.

  .. answer::

    **True.** The ``swim`` operation only compares the newly inserted key with its ancestors along the path from leaf :math:`N+1` to the root, which has length :math:`\lfloor \log_2(N+1) \rfloor \sim \log_2 N`.

* Let :math:`a[]` be an array such that :math:`a[1] > a[2] > \dots > a[N]` (and :math:`a[0]` is empty). Then :math:`a[]` satisfies the properties of a binary heap.

  .. answer::

    **True.** Since :math:`2k > k` and :math:`2k + 1 > k` for all :math:`k \ge 1`, a strictly decreasing array always satisfies :math:`a[k] > a[2k]` and :math:`a[k] > a[2k+1]`.

* The internal array of a binary (max-)heap is always sorted in non-increasing order.

  .. answer::

    **False.** A max-heap only constrains parent-child pairs, not siblings or cousins. For example, ``[-, 3, 1, 2]`` is a valid max-heap (:math:`3 > 1` and :math:`3 > 2`), but the array is not sorted in non-increasing order.

* Given a binary heap of :math:`N` distinct keys, deleting the maximum key and then immediately re-inserting it leaves the heap array unchanged (ignoring any array resizing).

  .. answer::

    **False.** Consider the max-heap ``[-, 3, 2, 1]``. Deleting the maximum ``3`` moves ``1`` to the root and sinks it, yielding ``[-, 2, 1]``. Immediately re-inserting ``3`` appends it at index 3 and swims it to the root, yielding ``[-, 3, 1, 2]``, which differs from the original array ``[-, 3, 2, 1]``.


Linear-Time Bottom-Up Heap Construction
"""""""""""""""""""""""""""""""""""""""

Prove that the bottom-up "sink-based" heap construction for heapsort (page 323) runs in :math:`\mathcal{O}(n)` time.
Hint: Count the number of nodes at level :math:`h` of the heap.
What is the cost of a ``sink`` operation at this level? Sum the costs over all levels. Useful formula: :math:`\sum_{k=0}^\infty k x^k = \frac{x}{(1-x)^2}` for
:math:`|x| < 1`.

.. answer::

    Let :math:`h = \lfloor \log_2 N \rfloor` be the height of the heap. Counting levels :math:`j = 0, 1, \dots, h` from the bottom (leaves at :math:`j = 0`, root at :math:`j = h`), there are at most :math:`\frac{2^h}{2^j}` nodes at height :math:`j`, and each node at height :math:`j` can ``sink`` down at most :math:`j` levels (:math:`2j` comparisons).
    Summing the maximum number of steps across all levels gives:

    .. math::

        T(N) \le \sum_{j=0}^h j \cdot \frac{2^h}{2^j} = 2^h \sum_{j=0}^h j \left(\frac{1}{2}\right)^j < 2^h \sum_{j=0}^{\infty} j \left(\frac{1}{2}\right)^j = 2^h \cdot \frac{1/2}{(1 - 1/2)^2} = 2^h \cdot 2 \le 2N \in \mathcal{O}(N)

    Thus, bottom-up heap construction runs in linear time :math:`\Theta(N)` (at most :math:`2N` comparisons and :math:`N` exchanges).


Building a Huffman Tree: Priority Queue vs. Sorting
"""""""""""""""""""""""""""""""""""""""""""""""""""

Is using a priority queue essential to build a Huffman code?
Can you design an alternative solution that uses a sorting algorithm?
Would its time complexity be better than the original algorithm? Why or why not?

.. answer::

    Let :math:`R` be the number of distinct symbols in the alphabet:

    * **Standard Min-Heap approach**: Inserting :math:`R` leaf nodes and performing :math:`R - 1` extract-min/insert steps takes :math:`\Theta(R \log R)` time.
    * **Naive re-sorting approach**: Re-sorting the list or inserting the merged parent node into a sorted array at each of the :math:`R - 1` steps takes :math:`\Theta(R)` per step, i.e., :math:`\Theta(R^2)` total time (worse than a priority queue).
    * **Two-Queue + Initial Sort approach**: If you first sort the :math:`R` leaf nodes by frequency in :math:`\Theta(R \log R)` time into a FIFO queue :math:`Q_1`, and push each newly merged internal node onto a second FIFO queue :math:`Q_2` (since merged frequencies are monotonically non-decreasing, :math:`Q_2` is automatically sorted!), you can extract the two smallest nodes at each step in :math:`\Theta(1)` time by comparing the fronts of :math:`Q_1` and :math:`Q_2`. This builds the tree in :math:`\Theta(R)` time after the initial :math:`\Theta(R \log R)` sort!


Huffman Compression and Decompression Pipeline
""""""""""""""""""""""""""""""""""""""""""""""

* What are the different steps in a text *compression* algorithm that takes a text as input and provides a compressed version of that text as output using Huffman coding? Be specific in your description by isolating each step of the problem. Specify for each step the useful data structures and the time complexity of the operations performed.
* What are the different steps of a text *decompression* algorithm that takes as input a compressed version of a text using Huffman coding and provides as output the original text? Be precise in your description by isolating each step of the problem. Specify for each step the useful data structures and the time complexity of the operations performed.

.. answer::

    Let :math:`N` be the length of the input text and :math:`R` be the alphabet size (e.g., :math:`R = 256` for extended ASCII):

    **Compression Pipeline** (page 835 of the textbook):

    1. **Read the input** of :math:`N` characters into memory: :math:`\Theta(N)`.
    2. **Tabulate character frequencies** using an array ``int[] freq = new int[R]``: :math:`\Theta(N + R)`.
    3. **Build the Huffman encoding trie** using a ``MinPQ<Node>`` of size at most :math:`R`: :math:`\Theta(R \log R)`.
    4. **Build the lookup table (codeword table)** ``String[] st = new String[R]`` by recursively traversing the trie: :math:`\Theta(R)`.
    5. **Write the trie** encoded as a bitstring via a preorder traversal, followed by the character count :math:`N`: :math:`\Theta(R)`.
    6. **Encode the input text** by looking up ``st[input[i]]`` for each character and writing its bits: :math:`\Theta(N)`.

    *Total compression time*: :math:`\Theta(N + R \log R)`.

    **Decompression Pipeline**:

    1. **Read the serialized Huffman trie** from the bit-stream header using a recursive preorder reader ``readTrie()``: :math:`\Theta(R)`.
    2. **Read the number of characters** :math:`N` to decode: :math:`\Theta(1)`.
    3. **Decode the bit stream**: For each of the :math:`N` characters, start at the root of the Huffman trie and follow left (``0``) or right (``1``) links according to the incoming bits until reaching a leaf node, output its character, and return to the root: :math:`\Theta(\text{number of compressed bits}) = \mathcal{O}(N)`.


Binary Heap Push
""""""""""""""""

Implement the `push operation of a binary heap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_BinaryHeap>`_.


Global Warming with Union-Find
""""""""""""""""""""""""""""""

Implement the Global Warming exercise to compute the number of islands using union-find: `GlobalWarming <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarming>`_


Huffman Tree
""""""""""""

Implement the Huffman tree reconstruction: `Huffman <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_Huffman>`_


Manual Exercise on Union-Find
"""""""""""""""""""""""""""""

Small manual exercise on `Union-Find <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part5UnionFind>`_


Manual Exercise on Heaps
""""""""""""""""""""""""

Small manual exercise on `Heaps <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part5Heap>`_
