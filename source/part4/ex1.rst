.. _part4_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W7.


Symbol Table Implementations Comparison
"""""""""""""""""""""""""""""""""""""""

Name at least four different implementations of a symbol table (dictionary).
Specify the main properties of each implementation.
In which scenario(s) are they most appropriate?
What are the time complexities of their main operations?

.. answer::

    .. list-table:: Summary of Symbol Table (Dictionary) Implementations
       :header-rows: 1

       * - Structure
         - Java Map
         - Java Set
         - Insert (``put``)
         - Search (``get``)
         - Delete (``remove``)
         - Key Requirement & Notes
       * - Unordered Array / Linked List
         - —
         - —
         - :math:`\mathcal{O}(N)`
         - :math:`\mathcal{O}(N)`
         - :math:`\mathcal{O}(N)`
         - ``equals()``; only suitable for tiny tables
       * - Ordered Parallel Arrays (``BinarySearchST``)
         - —
         - —
         - :math:`\mathcal{O}(N)`
         - :math:`\mathcal{O}(\log N)`
         - :math:`\mathcal{O}(N)`
         - ``Comparable``; great for static / read-mostly tables
       * - Balanced Search Tree (Red-Black BST)
         - ``TreeMap``
         - ``TreeSet``
         - :math:`\mathcal{O}(\log N)`
         - :math:`\mathcal{O}(\log N)`
         - :math:`\mathcal{O}(\log N)`
         - ``Comparable`` / ``Comparator``; supports ordered operations (``floor``, ``ceiling``, range queries)
       * - Hash Table (Separate Chaining / Linear Probing)
         - ``HashMap``
         - ``HashSet``
         - :math:`\mathcal{O}(1)` amortized (expected)
         - :math:`\mathcal{O}(1)` (expected)
         - :math:`\mathcal{O}(1)` amortized (expected)
         - ``hashCode()`` & ``equals()``; fastest for general lookup, no key ordering (under uniform hashing)
       * - Linked Hash Table
         - ``LinkedHashMap``
         - ``LinkedHashSet``
         - :math:`\mathcal{O}(1)` amortized (expected)
         - :math:`\mathcal{O}(1)` (expected)
         - :math:`\mathcal{O}(1)` amortized (expected)
         - ``hashCode()`` & ``equals()``; preserves insertion order (or access order for LRU caches)


Two-Sum Using a Hash Table
""""""""""""""""""""""""""

Recall the following question from the sorting assignment: Given a set :math:`S` of size :math:`n` and a number :math:`x`, describe an efficient algorithm using a hash table to determine whether there exists a pair :math:`(a, b)` with :math:`a \in S, b \in S` such that :math:`a + b = x`. What is the time complexity of your algorithm? Is it better than your solution that used sorting?

.. answer::

    Since a hash table (such as ``HashSet<Integer>``) supports insertion and lookup in :math:`\mathcal{O}(1)` expected time (assuming a uniform hash function), we can iterate through each element :math:`a \in S`, check whether :math:`x - a` is already in the ``HashSet``, and insert :math:`a` into the set.

    This runs in :math:`\mathcal{O}(n)` expected time and :math:`\mathcal{O}(n)` extra space, which is asymptotically faster than the :math:`\mathcal{O}(n \log n)` sorting-based approach (at the cost of :math:`\mathcal{O}(n)` memory for the hash table).


Modular Arithmetic and String Hashing in Java
"""""""""""""""""""""""""""""""""""""""""""""

Show that :math:`(a + b) \% M` is equivalent to :math:`((a \% M) + b) \% M`. How can this property be useful when building a hash function for strings?
Explain how Java computes a hash function for strings.
What is the time complexity of computing the hash code of a string once, and computing it :math:`N` times?

.. answer::

    * **Modular equivalence**: Write :math:`a = qM + r` where :math:`r = a \% M`. Then :math:`(a + b) \% M = (qM + r + b) \% M = (r + b) \% M = ((a \% M) + b) \% M` since :math:`qM` is a multiple of :math:`M`.
      Combined with :math:`(a \cdot b) \% M = ((a \% M) \cdot b) \% M`, this allows evaluating a polynomial hash function :math:`\left(\sum_{i=0}^{n-1} s[i] \cdot R^{n-1-i}\right) \% M` using **Horner's method** by applying :math:`\% M` at every step of the loop, preventing integer overflow!
    * **Java's ``String.hashCode()``**: Evaluates :math:`\sum_{i=0}^{n-1} s[i] \cdot 31^{n-1-i}` using Horner's method (relying on 32-bit signed integer wrap-around modulo :math:`2^{32}`):

      .. code-block:: java

          int h = 0;
          for (int i = 0; i < length(); i++) {
              h = 31 * h + charAt(i);
          }

    * **Time complexity**:

      * Computing ``hashCode()`` the **first time** on a string of length :math:`n` takes :math:`\Theta(n)` time.
      * Because ``String`` is **immutable**, Java **caches** the computed hash value in a private field ``private int hash``. Therefore, calling ``hashCode()`` :math:`N` times on the same ``String`` instance takes :math:`\Theta(n + N)` time in total (:math:`\Theta(n)` for the first call and :math:`\Theta(1)` for each of the remaining :math:`N - 1` calls).


Sign Bit Masking in Hash Functions
""""""""""""""""""""""""""""""""""

Explain why the ``hash()`` method on page 461 of the book returns ``(x.hashCode() & 0x7FFFFFFF) % M`` and not simply ``x.hashCode() % M``?
What number does ``0x7FFFFFFF`` represent?
What is its binary representation?
Show the effect at the bit level on an example where ``x.hashCode()`` returns a negative number. Hint: use ``Integer.toBinaryString(int)`` to verify your answer.

.. answer::

    * ``0x7FFFFFFF`` is a 32-bit hexadecimal literal. Since ``7`` is ``0111`` in binary and ``F`` is ``1111``, ``0x7FFFFFFF`` has binary representation ``01111111_11111111_11111111_11111111`` (a ``0`` sign bit followed by 31 ``1``s), which equals :math:`2^{31} - 1 = 2{,}147{,}483{,}647` (``Integer.MAX_VALUE``).
    * **Why ``x.hashCode() % M`` is dangerous**: ``hashCode()`` returns any signed 32-bit ``int``, which can be negative. In Java, the remainder operator ``%`` with a negative dividend and positive divisor ``M`` returns a **negative** result in :math:`[-(M-1), 0]`, which would throw an ``ArrayIndexOutOfBoundsException`` when indexing the hash table array!
    * **Effect of ``& 0x7FFFFFFF``**: Applying a bitwise AND with ``0x7FFFFFFF`` clears the sign bit (bit 31) to ``0`` while leaving the remaining 31 bits unchanged, turning any 32-bit signed integer into a non-negative 31-bit integer before taking ``% M``.
      *(Note: why not ``Math.abs(x.hashCode()) % M``? Because ``Math.abs(Integer.MIN_VALUE)`` still returns ``Integer.MIN_VALUE = -2147483648`` due to two's complement overflow!)*


Java Map Hierarchy and Hashtable
""""""""""""""""""""""""""""""""

Java provides the class ``java.util.Hashtable`` as an implementation of the ``java.util.Map`` interface.
Which variant of hash table does it use?
Does Java provide other implementations of the ``Map`` interface?
Draw a diagram representing the interfaces and classes related to ``Map`` and specify the key characteristics of each.
What can be used as a key for a hash table in Java? Be specific.

.. answer::

    * **Variant used**: Both ``java.util.Hashtable`` and ``java.util.HashMap`` use **separate chaining** (in Java 8+, ``HashMap`` converts chains longer than 8 nodes into balanced Red-Black trees to guarantee :math:`\mathcal{O}(\log N)` worst-case lookup even under hash-flooding attacks).
    * **Differences and ``Map`` implementations**:

      * ``HashMap``: Unsynchronized, permits one ``null`` key and ``null`` values, :math:`\mathcal{O}(1)` expected operations. Preferred over legacy ``Hashtable`` (which is synchronized on every method call and forbids ``null`` keys/values).
      * ``LinkedHashMap``: Subclass of ``HashMap`` that threads a doubly linked list through all entries to maintain insertion order (or access order).
      * ``ConcurrentHashMap``: Thread-safe hash table using fine-grained lock striping / CAS operations instead of locking the entire table.
      * ``TreeMap`` (implements ``NavigableMap`` / ``SortedMap``): Red-Black tree implementation keeping keys sorted in :math:`\mathcal{O}(\log N)` time per operation.
    * **Requirements for keys in a hash table**: Any object class can be used as a key, provided it properly overrides ``equals(Object)`` and ``hashCode()`` to obey the contract (``a.equals(b)`` implies ``a.hashCode() == b.hashCode()``), and **keys must be immutable** (modifying fields that participate in ``hashCode()`` after inserting a key into a map makes the entry unreachable!).


Hash Collisions and Resolution Strategies
"""""""""""""""""""""""""""""""""""""""""

What is meant by a "collision" in a hash table?
Do collisions affect the time complexity of operations?
If so, which operation(s) and with what complexity? If not, explain why.

.. answer::

    A **collision** occurs when two distinct keys :math:`k_1 \neq k_2` map to the same array index :math:`\text{hash}(k_1) = \text{hash}(k_2)` in the hash table.

    **Impact on time complexity**:
    Yes, collisions directly affect the time complexity of **all** dictionary operations (``get``, ``put``, and ``delete``):

    * **Expected case (under uniform hashing and bounded load factor** :math:`\alpha = N/M` **)**: The expected number of probes per operation is :math:`\Theta(1 + \alpha) = \Theta(1)`.
    * **Worst case (all :math:`N` keys collide into the same bucket or cluster)**: Both **separate chaining** (with linked lists) and **linear probing** degrade to :math:`\Theta(N)` time for ``get``, ``put``, and ``delete`` because they must linearly scan all :math:`N` colliding keys.


Load Factor and Resizing Strategies
"""""""""""""""""""""""""""""""""""

What is the load factor of a hash table?
Is controlling the load factor necessary or optional for the proper operation of a hash table using linear probing or separate chaining?
What strategy is used by ``java.util.Hashtable`` to control the load factor?
How does it differ from the strategy used in ``LinearProbingHashST``?
What is the relationship between the load factor and collisions?

.. answer::

    * **Load factor**: :math:`\alpha = N / M`, where :math:`N` is the number of stored key-value pairs and :math:`M` is the size of the internal table array.
    * **Necessity of controlling** :math:`\alpha`:

      * In **separate chaining**, :math:`\alpha` is the average chain length (which can exceed 1). Controlling :math:`\alpha` is necessary to keep the average search time :math:`\Theta(1 + \alpha)` constant; without resizing, operations degrade to :math:`\Theta(N/M) = \Theta(N)`.
      * In **linear probing**, :math:`\alpha` **must strictly satisfies** :math:`\alpha < 1` (if :math:`N = M`, the table is completely full and an unsuccessful search loops infinitely!). Moreover, as :math:`\alpha \to 1`, primary clustering causes the expected probe length :math:`\sim \frac{1}{2}\left(1 + \frac{1}{(1-\alpha)^2}\right)` to blow up rapidly, so ``LinearProbingHashST`` resizes to keep :math:`\alpha \in [1/8, 1/2]`.
    * **``java.util.Hashtable`` / ``HashMap`` strategy**: Uses a default load factor threshold of ``0.75``. When :math:`N > 0.75 \cdot M`, ``Hashtable`` allocates a new array of size :math:`2M + 1` (keeping the table size odd) and rehashes all entries, whereas ``HashMap`` doubles :math:`M` (power of two) and mixes the upper 16 bits of the hash code into the lower 16 bits (``h ^ (h >>> 16)``).


Fail-Fast Iterator for LinearProbingHashST
""""""""""""""""""""""""""""""""""""""""""

Imagine a new ``iterator()`` method that returns an iterator over the keys of ``LinearProbingHashST``.
Your iterator must not allow modifications to the hash table while in use: a ``ConcurrentModificationException`` should be thrown if a modification occurs.
How would you implement this? Hint: Take inspiration from the ``java.util.Hashtable`` strategy.

.. answer::

    Maintain an integer counter ``private int modCount = 0;`` in ``LinearProbingHashST`` that is incremented every time the table is structurally modified (i.e., whenever a key is added in ``put`` or removed in ``delete``).

    When ``iterator()`` is called, the iterator instance records ``int expectedModCount = modCount;`` at construction time and scans the internal ``keys[]`` array to skip ``null`` slots:

    .. code-block:: java

        public Iterator<Key> iterator() {
            return new Iterator<Key>() {
                private final int expectedModCount = modCount;
                private int idx = 0;
                private int yielded = 0;

                public boolean hasNext() {
                    if (modCount != expectedModCount)
                        throw new ConcurrentModificationException();
                    return yielded < N;
                }

                public Key next() {
                    if (!hasNext())
                        throw new NoSuchElementException();
                    while (keys[idx] == null) {
                        idx++;
                    }
                    yielded++;
                    return keys[idx++];
                }
            };
        }


Lazy Deletion with Tombstones in Linear Probing
"""""""""""""""""""""""""""""""""""""""""""""""

Describe the implementation of the ``put(key)`` method in a hash table using linear probing where deleted entries are marked with a special sentinel value (tombstone) via the ``delete(key)`` method.
In other words, instead of rehashing and shifting subsequent entries so that it is as if the deleted entry was never inserted, ``delete(key)`` simply flags the entry with this special marker.
What are the advantages and disadvantages of this approach compared to the ``LinearProbingHashST`` implementation in the book?

.. answer::

    * **Implementation of ``put(key, val)`` with tombstones**:
      When probing from ``i = hash(key)``, we cannot stop at the first tombstone ``DELETED`` because the key ``key`` might already exist further along the cluster! Therefore, ``put(key, val)`` must:

      1. Remember the index ``firstTombstone`` of the first ``DELETED`` slot encountered along the probe sequence.
      2. Continue probing until either ``keys[i].equals(key)`` (in which case we update ``vals[i] = val`` in place) or ``keys[i] == null`` (end of cluster).
      3. If ``keys[i] == null``, insert the new pair at ``firstTombstone`` (if one was seen) or at ``i`` otherwise.

    * **Advantages**: ``delete(key)`` is simpler to implement and faster on the spot because it avoids rehashing the rest of the cluster.
    * **Disadvantages**: Over time, tombstones accumulate and link separate clusters together! Unsuccessful searches (``get`` for a missing key, or ``put`` for a new key) **cannot stop at tombstones** and must probe all the way until a true ``null`` slot. Even if the number of live keys :math:`N` is very small, the effective load factor for unsuccessful searches includes all tombstones, severely degrading ``get`` and ``put`` performance until a full table rehash cleans them out.


Incremental Rolling Hash — Rabin-Karp
"""""""""""""""""""""""""""""""""""""

Imagine a hash function for a string :math:`s` such that knowing its value for the substring :math:`s[i \ldots i+n-1]` allows computing the hash value of the substring :math:`s[i+1 \ldots i+n]` in constant time (incrementally).

.. answer::

    This is the **Rabin-Karp rolling hash** (page 775 of the textbook).
    Let :math:`x_i = \left(\sum_{k=0}^{n-1} s[i+k] \cdot R^{n-1-k}\right) \bmod Q` be the polynomial hash of substring :math:`s[i \dots i+n-1]`.
    Then the hash :math:`x_{i+1}` of the next window :math:`s[i+1 \dots i+n]` is obtained in :math:`\Theta(1)` time by subtracting the leading character term :math:`s[i] \cdot R^{n-1}`, multiplying by :math:`R`, and adding the new trailing character :math:`s[i+n]`:

    .. math::

        x_{i+1} = \Big(\big(x_i + Q - (s[i] \cdot R^{n-1}) \bmod Q\big) \cdot R + s[i+n]\Big) \bmod Q

    where :math:`R^{n-1} \bmod Q` is precomputed once before sliding the window.


Single and Multi-Pattern Substring Search — Rabin-Karp
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Explain how to search for a substring of length :math:`m` in a text of length :math:`n` in :math:`\mathcal{O}(n)` time using an incremental hash function.
How would you do this if you had :math:`k` patterns of length :math:`m` to search for in a text of length :math:`n`?
What is the time complexity of your method? Is it better than running the Rabin-Karp algorithm :math:`k` times?

.. answer::

    * **Single pattern of length** :math:`m`: Compute the hash of the pattern in :math:`\Theta(m)` time and the initial hash of :math:`\text{text}[0 \dots m-1]` in :math:`\Theta(m)` time. Then slide the window across the text for :math:`i = 0 \dots n - m`, updating the rolling hash in :math:`\Theta(1)` time per step and comparing it against the pattern hash. Total expected time: :math:`\mathcal{O}(n + m)`.
    * **Searching for** :math:`k` **patterns of length** :math:`m` **simultaneously**:

      1. Compute the hash of each of the :math:`k` patterns and store them in a ``HashSet`` (or ``HashMap<Long, List<String>>``) in :math:`\Theta(k \cdot m)` preprocessing time.
      2. Slide the window of length :math:`m` once over the text of length :math:`n`. At each position :math:`i`, update the rolling hash in :math:`\Theta(1)` time and check whether the current window hash is contained in the ``HashSet`` in :math:`\mathcal{O}(1)` expected time!
      3. **Complexity**: :math:`\mathcal{O}(k m + n)` expected time, which is significantly faster than running single-pattern Rabin-Karp :math:`k` separate times (:math:`\mathcal{O}(k m + k n)`).


MCQ on Hash Functions
"""""""""""""""""""""

`Multiple choice questions on hash function <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part4QcmHashing>`_


MCQ on Rabin-Karp
"""""""""""""""""

`Multiple choice questions on Rabin-Karp <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part4QcmRk>`_


Word Counter
""""""""""""

An easy tool to implement for counting word occurrences (exam 2022).
Word counting is a frequent task in natural language processing algorithms:
`Word Counter <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_WordCounter>`_


Incremental Hash
""""""""""""""""

Incremental computation of a hash function (exam 2018):
`Incremental Hash <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_IncrementalHash>`_


LRU Cache
""""""""""

A bounded-capacity cache that retains only the most recently used entries (exam 2022):
`LRUCache <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_LRUCache>`_


Multi-Pattern Rabin-Karp
""""""""""""""""""""""""

Implement a version of Rabin-Karp to search for `K patterns <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_RabinKarp>`_ simultaneously instead of just one.
