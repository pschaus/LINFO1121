.. _part5_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W11.


Huffman Header: Serialized Trie vs. Codeword Table
""""""""""""""""""""""""""""""""""""""""""""""""""

In Huffman coding compression, it is necessary to include a header in the compressed file containing the information needed to decode the file.
In your implementation, the header is likely a serialized version of the trie (the result of a preorder traversal), as proposed in the textbook.
Do you think it would be more or less efficient in terms of memory to store the binary encoding of each symbol directly rather than the serialized trie?

.. answer::

    Storing the **serialized trie** via preorder traversal is significantly **more memory-efficient** (and simpler to decode) than storing an explicit table of ``(symbol, codeword)`` pairs:

    * **Serialized trie size**: A full binary tree with :math:`k` distinct leaf symbols has :math:`k - 1` internal nodes and :math:`k` leaves (:math:`2k - 1` nodes total). In the preorder bitstream, each internal node costs 1 bit (``0``) and each leaf costs 1 bit (``1``) plus 8 bits for the character, totaling exactly :math:`(2k - 1) + 8k = 10k - 1` bits.
    * **Explicit codeword table size**: Because Huffman codewords have variable lengths (from :math:`1` up to :math:`k - 1` bits), storing the binary encoding of each symbol directly requires storing the symbol (8 bits), the length of its codeword (e.g., 5–8 bits), and the codeword bits themselves (which can sum to :math:`\Theta(k^2)` bits in a skewed tree!). Furthermore, during decompression, you would still need to rebuild the trie from the codeword table to decode the bit stream bit-by-bit in :math:`\mathcal{O}(1)` per bit.


Repeated Huffman Compression
""""""""""""""""""""""""""""

Can we achieve an even better compression ratio if we reapply Huffman's compression algorithm to a file that has already been compressed once?
What happens in this case?
Does this open the door to a recursive and optimal compression algorithm?

.. answer::

    **No, reapplying Huffman coding to an already-compressed file generally increases the file size rather than shrinking it!**

    * Huffman coding exploits **skewed symbol frequencies** (some characters appear much more frequently than others, as in natural language text).
    * Once a text has been compressed with Huffman coding, the output bit stream has much higher entropy: when grouped into 8-bit bytes, the 256 possible byte values occur with a nearly uniform distribution.
    * Applying Huffman coding a second time must prepend a **second header** (serialized trie + length) while the body bit stream achieves almost zero compression (or even expands if only a small header was skewed), so recursive compression is impossible (by the Pigeonhole Principle, no lossless compression algorithm can shrink all files!).


Huffman Compression Ratio and Run-Length Encoding
"""""""""""""""""""""""""""""""""""""""""""""""""

What is, approximately, the compression ratio obtained if we apply the Huffman compression algorithm
to a file with a single string consisting of the character ``'a'`` repeated a million times (:math:`\approx 2^{20}`), followed by the character ``'b'`` occurring only once?

Does the resulting compression ratio vary with the length of the file (for example, if the ``'a'`` character is repeated two million times)?

What is the minimum number of bits needed to represent this file in compressed form?

Can we use another compression scheme that achieves higher compression than Huffman coding in this particular case?

Can the Huffman compression algorithm be used for inputs other than text files (for instance, an image)?
What would the algorithm count in this case?

.. answer::

    * **Huffman compression ratio**: Assuming the original file uses 8-bit ASCII (:math:`8 \times (10^6 + 1)` bits), the Huffman tree has only two symbols (``'a'`` and ``'b'``), so each is encoded using **1 bit** (e.g., ``0`` for ``'a'`` and ``1`` for ``'b'``). Ignoring the negligible header (:math:`\approx 19` bits + 32-bit length), the compressed file uses :math:`\approx 10^6 + 1` bits, giving a **compression ratio of** :math:`1/8 = 12.5\%`.
    * **Dependence on file length**: The asymptotic compression ratio remains **constant at** :math:`1/8` regardless of whether ``'a'`` is repeated one million or two million times, because standard Huffman coding must assign at least 1 bit per input symbol.
    * **Better compression scheme**: **Run-Length Encoding (RLE)** replaces consecutive runs of identical characters by ``(character, runLength)`` (e.g., ``(a, 1000000), (b, 1)``), which compresses the entire file into just a few bytes!
    * **Non-text inputs**: Yes, Huffman coding can compress any sequence of discrete symbols (such as pixel color intensities in an image, or quantized frequency coefficients in JPEG), by counting the frequency of each symbol value.


Linked Heap
"""""""""""

Imagine a heap implementation of a priority queue using a linked structure to represent the essentially complete binary tree corresponding to the heap.
How many links are needed in each node?
Write the code for the methods ``insert`` and ``delMax``. What are their time complexities? Is it necessary to specify a maximum capacity :math:`N` in the constructor?
How do you add a new node to the heap or remove the last node? Can this be determined from the current heap size?

Implement the min priority queue using a linked structure for representing the heap: `MinPQLinked <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MinPQLinked>`_

.. answer::

    * **Links per node**: **3 links** (``parent``, ``left``, and ``right``) are needed in each ``Node`` so we can both ``swim`` up toward the root and ``sink`` down toward the leaves.
    * **Capacity**: No maximum capacity needs to be specified in the constructor since nodes are allocated dynamically.
    * **Locating the last position from the size** :math:`n` **in** :math:`\mathcal{O}(\log n)` **time**:
      In a 1-indexed complete binary tree, the binary representation of any node index :math:`n` (after skipping the leading ``1`` bit, which represents the root) gives the exact path from the root to node :math:`n`: a ``0`` bit means go ``left`` and a ``1`` bit means go ``right``!
      For example, for :math:`n = 6 = (110)_2`, starting at the root (``1``), we follow ``1`` (right) then ``0`` (left) to reach position 6 in :math:`\lfloor \log_2 n \rfloor` steps. Thus both ``insert`` and ``delMax`` run in :math:`\Theta(\log n)` worst-case time.


Min-Max Heap
""""""""""""

Propose a data structure that supports the following operations in logarithmic time: *insert*, *remove maximum*, *remove minimum*;
and the following operations in constant time: *find maximum* and *find minimum*.
For this, we consider the min-max heap data structure.
The even levels are: 0 (root), 2, 4, etc.
These even levels are called the :math:`\min` levels.
The odd levels are 1, 3, 5, etc.
These odd levels are called the :math:`\max` levels.
For any element :math:`x` in the min-max heap, the following property holds:

* If :math:`x` is at a :math:`\min` level, all descendants of :math:`x` are greater than or equal to :math:`x`.
* If :math:`x` is at a :math:`\max` level, all descendants of :math:`x` are less than or equal to :math:`x`.

Questions related to this min-max heap:

* Where is the smallest element of the heap located?

  .. answer::

    At the **root** (index 1, level 0), which is a :math:`\min` level.

* Where is the largest element of the heap located?

  .. answer::

    At the root if :math:`N = 1`, or as the **maximum of the two children of the root** (indices 2 and 3, at level 1, which is the highest :math:`\max` level).

* Draw a min-max heap that contains the following elements: 10, 8, 71, 31, 41, 46, 51, 31, 21, 11, 16, 13.

  .. answer::

    .. image:: minmaxheap.png

* Describe the insertion operation in a min-max heap. Give the pseudocode.

  .. answer::

    1. Append the new key :math:`x` at index :math:`k = N + 1` (the next available leaf).
    2. Let :math:`p = k / 2` be its parent:

       * If :math:`k` is on a **min level**:

         * If :math:`a[k] > a[p]` (where :math:`p` is on a max level), swap :math:`a[k]` and :math:`a[p]`, and then ``swimMax(p)`` up through the **max levels** (comparing with grandparents :math:`p / 4`).
         * Otherwise, ``swimMin(k)`` up through the **min levels** (comparing with grandparents :math:`k / 4`).
       * If :math:`k` is on a **max level**:

         * If :math:`a[k] < a[p]` (where :math:`p` is on a min level), swap :math:`a[k]` and :math:`a[p]`, and then ``swimMin(p)`` up through the **min levels** (comparing with grandparents :math:`p / 4`).
         * Otherwise, ``swimMax(k)`` up through the **max levels** (comparing with grandparents :math:`k / 4`).

Implement the `MinMax Heap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MinMaxHeap>`_.


MedianHeap
""""""""""

Imagine a data structure that supports:

1. *insertion* in logarithmic time
2. *find median* in constant time
3. *deleting the median* in logarithmic time.

Hint: There is a solution that uses two internal heaps.

Before starting your implementation, think about the class invariant or property that you want
to maintain between the two heaps after each operation.

Implement the `MedianHeap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MedianHeap>`_.

.. answer::

    Maintain **two heaps**:

    * A **Max-Heap** ``left`` storing the smaller half of the elements.
    * A **Min-Heap** ``right`` storing the larger half of the elements.

    **Invariants**:

    1. *Ordering invariant*: Every key in ``left`` is :math:`\le` every key in ``right`` (i.e., ``left.max() <= right.min()``).
    2. *Size balance invariant*: :math:`0 \le |\text{left}| - |\text{right}| \le 1` (or vice versa, according to the median convention).

    With these invariants, the median is always at the root of ``left`` in :math:`\Theta(1)` time, and after any insertion or median deletion, we rebalance the sizes of ``left`` and ``right`` by moving at most one root element between the two heaps in :math:`\mathcal{O}(\log N)` time.


Ternary Heap
""""""""""""

Implement a ternary heap where each node has up to three children rather than two.
Be careful here: we store the values starting at index 0 rather than index 1 as in the binary heap, because the formulas :math:`2k` and :math:`2k+1` do not apply to the ternary case.
What is the time complexity for the ``insert`` and ``delMax`` operations?

Implement the `TernaryHeap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_TernaryHeap>`_.

.. answer::

    * **0-indexed Ternary Heap index formulas**:

      * Parent of node :math:`k > 0`: :math:`\lfloor (k - 1) / 3 \rfloor`
      * Children of node :math:`k`: :math:`3k + 1`, :math:`3k + 2`, and :math:`3k + 3`

    * **Time complexity**:

      * The height of a ternary heap with :math:`N` nodes is :math:`\lfloor \log_3 N \rfloor`.
      * ``insert`` (``swim``): at most :math:`\log_3 N` comparisons (:math:`\mathcal{O}(\log_3 N) = \mathcal{O}(\log N)`).
      * ``delMax`` (``sink``): at each level we compare up to 3 children to find the largest child and swap with the parent, taking at most :math:`3 \log_3 N` comparisons (:math:`\mathcal{O}(\log_3 N) = \mathcal{O}(\log N)`).
