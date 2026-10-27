.. _part4_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W8.


Hash of Long and Double
"""""""""""""""""""""""

Here is the formula used by Java to calculate the hash code
of a ``double`` (where ``bits`` is a 64-bit value represented as a ``long``):

.. code-block:: java

    return (int) (bits ^ (bits >>> 32));

* Why not simply use ``(int) bits`` (casting from ``long`` to ``int``)? Hint: The textbook suggests that a good hash function should use all bits in its calculation. Why?
* A ``double`` in Java is represented in 64 bits as :math:`(-1)^s \times m \times 2^{(e - 1023)}`. The first bit :math:`s` is the sign bit, the next 11 bits represent the exponent in binary, and the last 52 bits represent the mantissa (significand). Do a positive floating-point number and its opposite receive different hash codes?

.. answer::

    * **Why not ``(int) bits``?** Casting a 64-bit ``long`` directly to a 32-bit ``int`` simply discards the upper 32 bits (which for a ``double`` contain the sign bit, the entire 11-bit exponent, and the 20 most significant bits of the mantissa!). Many distinct ``double`` values (such as ``1.0``, ``2.0``, ``4.0``, ``-1.0``, whose lower 32 mantissa bits are all zeros) would collide with the exact same hash code ``0``. By XORing the upper 32 bits ``(bits >>> 32)`` with the lower 32 bits before casting, **all 64 bits** contribute to the 32-bit hash code.
    * **Positive vs. negative ``double``**: **Yes, they receive different hash codes.** A positive ``double`` has sign bit :math:`s = 0` at bit 63, whereas its opposite has :math:`s = 1` at bit 63 (and identical exponent and mantissa). When ``bits >>> 32`` shifts bit 63 down to bit 31 and XORs it with bit 31 of the lower half, the resulting 32-bit integers differ in their most significant bit (e.g., ``Double.hashCode(6.0) == 1075314688`` while ``Double.hashCode(-6.0) == -1072168960``).


Hash and Casting of Integers
""""""""""""""""""""""""""""

* Is the hash code of a 32-bit integer the same as the hash code of the same integer cast to a ``double``?

  .. answer::

    **False.** A 32-bit ``int`` (e.g., ``5``, binary ``0...0101``, whose ``Integer.hashCode(5)`` is ``5``) cast to a ``double`` (``5.0``) is encoded in IEEE 754 floating-point format as :math:`(-1)^0 \times 1.25 \times 2^{1025 - 1023}`, whose 64-bit pattern is ``0_10000000001_0100...0``. Applying ``(int) (bits ^ (bits >>> 32))`` to this IEEE 754 bit pattern produces ``1075052544``, which is completely different from ``5``.

* Is the hash code of a 32-bit integer the same as the hash code of the same integer cast to a ``long``? Hint: ``Long.toBinaryString(Double.doubleToRawLongBits(a))`` displays the bits used to represent a ``double``.

  .. answer::

    We must distinguish two cases when casting a 32-bit ``int`` :math:`x` to a 64-bit ``long`` (sign extension):

    * **Case 1: Non-negative integer (:math:`x \ge 0`) — True.**
      Sign-extending a non-negative ``int`` pads the upper 32 bits with ``0``s, so ``(bits >>> 32) == 0``. XORing the lower 32 bits with ``0`` leaves :math:`x` unchanged: ``Long.hashCode((long) x) == x == Integer.hashCode(x)``.
    * **Case 2: Negative integer (:math:`x < 0`) — False.**
      In two's complement, casting a negative 32-bit ``int`` to a 64-bit ``long`` fills the upper 32 bits with ``1``s (``0xFFFFFFFF``). Therefore, ``(bits >>> 32)`` is ``-1`` (all ``1``s), and XORing the lower 32 bits with all ``1``s flips every bit (computing the bitwise complement ``~x`` instead of ``x``)! For example, ``Integer.hashCode(-5) == -5``, whereas ``Long.hashCode(-5L) == ~(-5) == 4``.


String Hashing: Choice of M and R Constants
"""""""""""""""""""""""""""""""""""""""""""

The hash function for a given string as presented on page 460 of the book is as follows:

.. code-block:: java

    int hash = 0;
    for (int i = 0; i < s.length(); i++)
        hash = (R * hash + s.charAt(i)) % M;

In the book's implementation, :math:`M` (the size of the hash table) is a power of two.
The suggested value for :math:`R` is *a small prime such as 31 so that the bits of all characters play a role.*

* Suppose that :math:`R` is a multiple of :math:`M`. What would happen in the calculation?

  .. answer::

    If :math:`R = kM` for some integer :math:`k > 0`, then every term with :math:`n - 1 - i \ge 1` is a multiple of :math:`M` and vanishes modulo :math:`M`:

    .. math::

        \left( \sum_{i=0}^{n-1} (kM)^{n-1-i} s_i \right) \bmod M = s_{n-1} \bmod M

    **Only the very last character** :math:`s_{n-1}` of the string determines the hash value! All strings ending with the same character collide in the same bucket.

* Suppose that :math:`R` is an even number. What would happen?

  .. answer::

    Since :math:`M = 2^k` is a power of two and :math:`R = 2l` is even, we have :math:`R^j = 2^j l^j`, which is a multiple of :math:`M = 2^k` for all :math:`j \ge k`. Therefore:

    .. math::

        \left( \sum_{i=0}^{n-1} (2l)^{n-1-i} s_i \right) \bmod 2^k = \left( \sum_{i=\max(0, n-k)}^{n-1} (2l)^{n-1-i} s_i \right) \bmod 2^k

    Only the last :math:`k` characters of the string affect the hash value (and only some bits of those characters); all earlier characters are completely ignored!

In both cases, how many characters in the string will actually determine the hash code? What are the risks in terms of collisions? Can controlling the load factor solve this problem? Explain why using 31 is a good choice for array sizes that are powers of two. Would it also be a good choice for an array size that starts at 31 and is multiplied by two each time it is resized?

.. answer::

    Controlling the load factor (resizing) **cannot** fix a bad choice of :math:`R` and :math:`M`: if strings share the same suffix, they will still collide.
    :math:`R = 31` is a good choice when :math:`M = 2^k` because :math:`\gcd(31, 2^k) = 1` (they are **coprime**) and multiplication by :math:`31 = 2^5 - 1` can be optimized by the compiler as ``(h << 5) - h``. However, if :math:`M` is a multiple of :math:`31` (e.g., :math:`M = 31 \cdot 2^k`), then :math:`\gcd(R, M) = 31`, so ``hash % 31`` depends only on the last character ``s[n-1] % 31``! In general, :math:`R` and :math:`M` must always be **coprime** (:math:`\gcd(R, M) = 1`).

* In the book's implementation, :math:`M` (the size of the hash table) is a power of two, initialized to 16. Suppose that at some point :math:`M` is :math:`2^8 = 256`. Then two integer keys are added to a hash table implemented with separate chaining: :math:`2560` and :math:`3072` respectively (assume that these additions do not cause a resize). As you know, the hash code of an integer key (``int``) in Java is the integer itself.
  Will adding these two values cause a collision between them in the table? If so, why?

  .. answer::

    **Yes**, because both :math:`2560 = 10 \times 256` and :math:`3072 = 12 \times 256` are multiples of :math:`256`, so :math:`2560 \bmod 256 = 0` and :math:`3072 \bmod 256 = 0`.

  If so, can you suggest a third value that will also collide?

  .. answer::

    Any other multiple of :math:`256`, such as :math:`512` (or :math:`1024`).

  If there is a collision, can it disappear the next time the table is resized using the book's resizing strategy?

* What do you suggest to avoid this problem? What is the initialization and resizing policy for :math:`M` used in ``java.util.Hashtable`` / ``java.util.HashMap``? Does this solve the problem in our example?

  .. answer::

    With the book's strategy of doubling :math:`M` from :math:`256` to :math:`512`, both :math:`2560 = 5 \times 512` and :math:`3072 = 6 \times 512` remain multiples of :math:`512`, so **they still collide after resizing**!
    To avoid this:

    * Choose :math:`M` to be a **prime number** (or in ``java.util.Hashtable``, start at :math:`M = 11` and resize to :math:`2M + 1`, which changes the modulus to an odd number coprime to powers of two so :math:`2560` and :math:`3072` no longer collide).
    * Alternatively, ``java.util.HashMap`` keeps :math:`M = 2^k` for fast bitwise masking ``h & (M - 1)`` but first **scrambles** the hash code via ``h ^ (h >>> 16)`` so high-order bits also participate in the bucket index.


Design of a Hash Function for Vehicles
""""""""""""""""""""""""""""""""""""""

* What would you suggest as a hash function for vehicle identifiers that are strings of numbers and letters of the form: ``"9X9XX99X9XX999999"``, where each ``9`` represents a digit (0–9) and each ``X`` represents an uppercase letter (A–Z)?
* Does your hash function have the property that for a hypothetical array size :math:`N` of :math:`10^{11} \cdot 26^6` there will never be any collision?

.. answer::

    * **Standard polynomial hash**: Apply Horner's method across all 17 characters using prime radix :math:`R = 31` (or :math:`R = 37`).
    * **Perfect (collision-free) hash function for** :math:`N = 10^{11} \cdot 26^6`:
      The identifier consists of 6 uppercase letters (each in :math:`0 \dots 25`) and 11 decimal digits (each in :math:`0 \dots 9`).

      * Let :math:`X \in [0, 26^6 - 1]` be the integer formed by interpreting the 6 letters as a 6-digit number in base 26.
      * Let :math:`Y \in [0, 10^{11} - 1]` be the 11-digit decimal number formed by concatenating the 11 digits.
      * Then :math:`h(\text{id}) = X \cdot 10^{11} + Y` maps every valid vehicle identifier **bijectively** (one-to-one) to a unique integer in :math:`[0, 10^{11} \cdot 26^6 - 1]`, guaranteeing **zero collisions** in an array of size :math:`N = 10^{11} \cdot 26^6`.


Design of a Hash Function: Citizens
"""""""""""""""""""""""""""""""""""

Suppose we want to build a directory of Belgian citizens
where each citizen can be accessed by their 12-digit national identity card number.
We can consider this number as the unique key identifying each citizen
and use it directly as an index in a Java array.
Each array index would hold a reference to an instance of a class
whose fields contain the citizen's personal information.

What is the time complexity of the following operations?

* Searching for a citizen's information using their identity card number.
* Adding a new citizen.

Is this implementation of a dictionary not even better than a hash table?
Can a collision occur in this design? Justify your answer.

.. answer::

    * **Time complexity and collisions**: Both search and insertion take :math:`\Theta(1)` worst-case time via direct array indexing, and **no collision can ever occur** since each citizen has a unique 12-digit national number.
    * **Why this direct-address table is completely impractical**:
      A 12-digit number requires an array of size :math:`10^{12}` (:math:`1{,}000` billion slots). Even storing only an 8-byte object reference per slot would require :math:`8 \times 10^{12}\text{ bytes} = 8\text{ Terabytes}` of contiguous RAM (and Java arrays are indexed by 32-bit ``int``, so they cannot exceed :math:`2^{31} - 1 \approx 2.14 \times 10^9` elements anyway!).
      Since Belgium has only :math:`\approx 1.15 \times 10^7` citizens, the load factor would be :math:`\frac{1.15 \times 10^7}{10^{12}} \approx 0.00115\%`, wasting :math:`99.999\%` of the allocated memory. A hash table of size :math:`M \approx 2 \times 10^7` achieves :math:`\mathcal{O}(1)` expected lookup while using :math:`50{,}000\times` less memory!


Rabin-Karp Revisited
""""""""""""""""""""

Check that you have obtained a solution in :math:`\mathcal{O}(n)` and not :math:`\mathcal{O}(kn)` (not counting the initial hashing of the keywords to be searched, which is in :math:`\mathcal{O}(km)`) for last week's *Rabin-Karp* exercise.

.. answer::

    * The initial preprocessing of the :math:`k` patterns of length :math:`m` takes :math:`\Theta(k m)` time to compute their hashes and insert them into a ``HashSet<Long>`` (or ``HashMap``).
    * During the scan of the text of length :math:`n`: at each index :math:`i \in \{0, \dots, n - m\}`, we update the rolling hash of the current window in :math:`\Theta(1)` time, and instead of comparing it against all :math:`k` pattern hashes in :math:`\Theta(k)` time, we query the ``HashSet`` in :math:`\mathcal{O}(1)` **expected time**!
    * Thus, the text scan takes :math:`\mathcal{O}(n)` expected time (independent of :math:`k`!), giving a total expected time of :math:`\mathcal{O}(km + n)`.


Linear Probing
""""""""""""""

Implement a `linear probing hash table <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_LinearProbingHashST>`_.


Tries and Autocompletion
""""""""""""""""""""""""

Implement an efficient auto-completion algorithm using a trie data structure: `AutoCompleter <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_AutoCompleter>`_


Monkeys and Hash Tables
"""""""""""""""""""""""

This is problem 21 of the `Advent of Code 2022 <https://adventofcode.com>`_.
It can be efficiently solved using a hash table in combination with a linked tree data structure: `Monkeys <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_Monkeys>`_


Bitset
""""""""""

Implement an efficient alternative to a ``HashSet`` when you need to store a dense set of integers: `Bitset <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_Bitset>`_
