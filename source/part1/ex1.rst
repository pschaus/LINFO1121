.. _part1_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W2.


Abstract Data Types: Interface vs. Class
""""""""""""""""""""""""""""""""""""""""

Define what an abstract data type (ADT) is. In Java, is it better to describe an ADT by a
class or an interface? Why?

.. answer::

    An **Abstract Data Type (ADT)** is a data type defined solely by its behavior (the set of operations it supports and their semantics) from the point of view of a user, independent of any concrete implementation (see page 64 of the textbook).

    In Java, it is better to specify an ADT using an **interface** because a class either:

    * is completely abstract (in which case an interface is more flexible since a class can implement multiple interfaces but only extend a single class), or
    * already commits to a specific internal representation and implementation of the ADT.

    An **abstract class** can still be useful as a skeletal implementation between the interface and concrete subclasses to share common code (for example, implementing ``isEmpty()`` in terms of ``size()`` as ``return size() == 0;``). However, since Java 8, interfaces can also provide ``default`` method implementations, making interfaces the standard choice for defining ADTs.


Stack at the End of a Singly Linked List
""""""""""""""""""""""""""""""""""""""""

How would you implement a *stack* using a singly linked list where the ``push`` and ``pop`` operations are done at the **end of the list**? Is this solution efficient? Justify your answer.

.. answer::

    In a singly linked list, each node only stores a reference to its ``next`` node:

    * **Without a tail pointer**: both ``push`` and ``pop`` must traverse the entire list from ``head`` to reach the last node, taking :math:`\Theta(n)` time.
    * **With a tail pointer**: ``push`` at the end can be done in :math:`\Theta(1)` time by appending a new node after ``tail`` and updating ``tail``. However, ``pop`` must remove the last node and update ``tail`` to point to the **second-to-last** node (and set its ``next`` reference to ``null``). Because links are unidirectional, finding the predecessor of ``tail`` still requires traversing the list from ``head`` in :math:`\Theta(n)` time.

    Therefore, this solution is **inefficient** (:math:`\Theta(n)` per ``pop``). To achieve :math:`\Theta(1)` worst-case time for both ``push`` and ``pop`` with a singly linked list, operations must be performed at the **head** (front) of the list, or a doubly linked list must be used.


Stack Implementations and java.util.Stack
"""""""""""""""""""""""""""""""""""""""""

What are the possible implementations for a stack? By consulting the Java API documentation, describe
the implementation of a stack by the class ``java.util.Stack``. Go to the source code of the implementation
``java.util.Stack`` (Ctrl+B from IntelliJ).

Why do you think Java developers chose this implementation
(hint: argue about memory and garbage collection)?

.. answer::

    A stack can be implemented using either a **linked list** (singly linked list operating at the head) or a **resizing array**.

    In the standard library, ``java.util.Stack`` extends ``java.util.Vector``, which uses a **contiguous resizing array**.

    **Why a resizing array is preferred in practice:**

    * **Memory and Garbage Collection**: A linked list allocates a separate ``Node`` object on the heap for every ``push`` and makes it eligible for garbage collection on every ``pop``. Under frequent ``push``/``pop`` workloads, this creates significant memory overhead (object headers + two references per node) and heavy pressure on the garbage collector. A resizing array stores references contiguously in a single array block and has much better CPU cache locality.
    * **Amortized constant time**: Although resizing the array by doubling its capacity takes :math:`\mathcal{O}(n)` time when full, this happens only when the size reaches a power of two (:math:`1, 2, 4, 8, \dots, n = 2^m`). Over :math:`n` insertions, the total number of element copies is:

      .. math::

          \sum_{i=0}^m 2^i = 2^{m+1} - 1 = 2n - 1 \in \mathcal{O}(n)

      Dividing by :math:`n` operations gives an **amortized cost of** :math:`\mathcal{O}(1)` per operation.

    *Note:* The Java documentation recommends using ``ArrayDeque`` (implementing the ``Deque`` interface) instead of the legacy ``Stack`` class, because ``Stack`` inherits synchronized methods from ``Vector`` (adding unnecessary synchronization overhead in single-threaded code) and exposes indexed ``Vector`` methods that break the strict LIFO abstraction.


Implement a Stack with Two Queues
"""""""""""""""""""""""""""""""""

How do you implement the abstract data type *stack* using two *queues*?
In particular, describe how the ``push`` and ``pop`` methods work in this case.

As an example, specify the state of each of the two queues after pushing the integers ``1 2 3`` onto an initially empty stack.
Describe what happens next when the ``pop`` operation is performed.

What is the time complexity of these methods if we assume that each ``enqueue`` and ``dequeue``
operation is executed in constant time?

Is this implementation of a stack efficient (for :math:`n` operations)
compared to the other implementations presented in the reference book?

Once you have imagined your solution on paper, you can solve the corresponding INGInious task `StackWithTwoQueues <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_StackWithTwoQueues>`_.

.. answer::

    There are two main approaches using two FIFO queues ``a`` and ``b``:

    * **Method 1 (Fast push, costly pop)**: Maintain elements in FIFO order in queue ``a``.

      * ``push(x)`` (:math:`\mathcal{O}(1)`): simply enqueue ``x`` into ``a``.

        .. code-block:: java

            a.add(x);

      * **Example trace**: After ``push(1)``, ``push(2)``, ``push(3)``, queue ``a`` contains ``[1, 2, 3]`` (front is ``1``) and queue ``b`` is ``[]``.
      * ``pop()`` (:math:`\mathcal{O}(n)`): dequeue the first :math:`n-1` elements from ``a`` and enqueue them into ``b`` (``b`` becomes ``[1, 2]``). The remaining element ``3`` in ``a`` is dequeued and returned. Finally, swap the references of ``a`` and ``b`` (or move elements back to ``a``).

        .. code-block:: java

            if (a.isEmpty()) throw new EmptyStackException();
            while (a.size() > 1) {
                b.add(a.remove());
            }
            int out = a.remove();
            Queue<Integer> tmp = a;
            a = b;
            b = tmp;
            return out;

    * **Method 2 (Costly push, fast pop)**: Maintain elements in LIFO (reverse) order in queue ``a`` so the most recently pushed element is always at the front of ``a``.

      * ``push(x)`` (:math:`\mathcal{O}(n)`): enqueue ``x`` into empty queue ``b``, dequeue all elements from ``a`` into ``b``, then swap ``a`` and ``b``. After pushing ``1, 2, 3``, queue ``a`` contains ``[3, 2, 1]`` (front is ``3``) and ``b`` is ``[]``.

        .. code-block:: java

            b.add(x);
            while (!a.isEmpty()) {
                b.add(a.remove());
            }
            Queue<Integer> tmp = a;
            a = b;
            b = tmp;

      * ``pop()`` (:math:`\mathcal{O}(1)`): simply dequeue the front element from ``a`` (``return a.remove();``).

    **Efficiency**: In both methods, at least one of ``push`` or ``pop`` takes :math:`\Theta(n)` time, so a sequence of :math:`n` operations can take :math:`\Theta(n^2)` time. This is much less efficient than a standard array-based or linked-list stack, which executes :math:`n` operations in :math:`\Theta(n)` time (:math:`\Theta(1)` per operation).


Iterating Over a LinkedList vs. ArrayList
"""""""""""""""""""""""""""""""""""""""""

What do you think about these three different ways of iterating over the elements of a ``java.util.LinkedList``? Are they equivalent? Use a time-complexity argument.
Does replacing ``new LinkedList<>()`` with ``new ArrayList<>()`` on the first line change the performance of these loops?

.. code-block:: java

    List<Integer> list = new LinkedList<>();

    // assume I insert n elements in the list here

    for (Integer val: list) {
        System.out.println(val);
    }

    Iterator<Integer> itr = list.iterator();
    while (itr.hasNext()) {
        Integer val = itr.next();
        System.out.println(val);
    }

    for (int i = 0; i < list.size(); i++) {
        Integer val = list.get(i);
        System.out.println(val);
    }

.. answer::

    * **With ``LinkedList``**:

      * The **first two loops are equivalent** (the enhanced ``for``-each loop is syntactic sugar that compiles down to using an ``Iterator``). The iterator maintains a pointer to the current node in the list, advancing in :math:`\mathcal{O}(1)` per step, so the total time complexity is :math:`\Theta(n)`.
      * The **third loop takes** :math:`\Theta(n^2)` **time**! On a ``LinkedList``, ``list.get(i)`` must traverse :math:`i` links from the beginning (or end) of the list, costing :math:`\Theta(i)` time. Summing over :math:`i = 0 \dots n-1` yields :math:`\Theta(n^2)`.
      * This highlights the primary purpose of an **Iterator**: it preserves traversal state inside the data structure so each element is visited in :math:`\mathcal{O}(1)` time without repeating work.

    * **With ``ArrayList``**:

      * All three loops run in :math:`\Theta(n)` time because ``ArrayList`` is backed by a contiguous array where ``list.get(i)`` provides :math:`\Theta(1)` random access.


Asymptotic Notations: Tilde vs. Big-Oh, Omega, Theta
""""""""""""""""""""""""""""""""""""""""""""""""""""

The :math:`\sim` (tilde) notation is used in the reference book for the analysis of the running times of
algorithms. How does this notation differ from or resemble the more commonly used notations :math:`\mathcal{O}`
(big Oh), :math:`\mathcal{\Omega}` (big Omega), and :math:`\mathcal{\Theta}` (big Theta)?

Explain precisely the links and similarities between them.
What do you see as the advantage of using the :math:`\sim` (tilde) notation rather than :math:`\mathcal{O}`
when possible?

.. answer::

    See the detailed summary document on complexity notations: :ref:`part1complexity`.

    In short:

    * :math:`f(n) \in \mathcal{O}(g(n))` gives an **asymptotic upper bound** up to a constant factor.
    * :math:`f(n) \in \Omega(g(n))` gives an **asymptotic lower bound** up to a constant factor.
    * :math:`f(n) \in \Theta(g(n))` gives a **tight asymptotic bound** (both upper and lower) up to constant factors.
    * :math:`f(n) \sim g(n)` means :math:`\lim_{n \to \infty} \frac{f(n)}{g(n)} = 1`. Thus, :math:`f(n) \sim g(n) \implies f(n) \in \Theta(g(n)) \implies f(n) \in \mathcal{O}(g(n))`, but the converse is false (for instance, :math:`2n^2 \in \Theta(n^2)` but :math:`2n^2 \not\sim n^2`).

    **Advantage of tilde notation**: Unlike :math:`\mathcal{O}` and :math:`\Theta`, the :math:`\sim` notation **preserves the leading multiplicative constant** while dropping lower-order terms. This allows comparing the concrete efficiency of two algorithms with the same asymptotic growth rate (e.g., :math:`\sim \frac{1}{2}n^2` vs. :math:`\sim n^2` comparisons) and making quantitative running-time predictions.


The Doubling Ratio Test
"""""""""""""""""""""""

Explain how we can extract the :math:`\sim` (tilde) characterization from the implementation of an algorithm
using the *doubling ratio* test.

* How does this test work?

  .. answer::

    If the running time follows a power law :math:`T(n) \sim a \cdot n^b` (or :math:`a \cdot n^b \log n`), then doubling the input size yields the ratio:

    .. math::

        \frac{T(2n)}{T(n)} \sim \frac{a (2n)^b}{a n^b} = 2^b

    By repeatedly doubling the input size :math:`n` and measuring :math:`T(2n)/T(n)`, the ratio converges to :math:`2^b`, from which we can deduce the exponent :math:`b = \log_2 \left(\lim_{n\to\infty} \frac{T(2n)}{T(n)}\right)` and estimate the order of growth.

* What are the limitations and advantages of this test?

  .. answer::

    * **Advantages**: Very simple to implement experimentally as a black-box test without needing to analyze every line of source code; directly predicts real execution times for larger inputs.
    * **Limitations**:

      1. It cannot reliably distinguish logarithmic factors (since :math:`\frac{a(2n)^b \log(2n)}{a n^b \log n} = 2^b \left(1 + \frac{1}{\log n}\right) \to 2^b`).
      2. It becomes impractical when :math:`T(n)` grows very fast (exponential) or requires too much memory for large :math:`n`.
      3. It is an empirical observation on specific inputs (which might not hit the worst case) and not a mathematical proof, and can be noisy for small :math:`n` due to JVM warm-up, caching, or garbage collection.

Suppose we measure the following :math:`T(n)` execution times (in seconds) of a program as a function of the
input size :math:`n`:

============  ==== ==== ==== ==== ===== ===== =====
:math:`n`     1000 2000 4000 8000 16000 32000 64000
:math:`T(n)`  0    0    0.1  0.3  1.3   5.1   20.5
============  ==== ==== ==== ==== ===== ===== =====

* How can you best characterize the growth order of this function?

  .. answer::

    Computing the successive doubling ratios :math:`T(2n)/T(n)`:

    ===================  ==== ==== ==== ==== ===== ===== =====
    :math:`n`            1000 2000 4000 8000 16000 32000 64000
    :math:`T(n)`         0    0    0.1  0.3  1.3   5.1   20.5
    :math:`T(2n)/T(n)`   —    —    —    3.0  4.3   3.9   4.0
    ===================  ==== ==== ==== ==== ===== ===== =====

    Since :math:`T(2n)/T(n) \approx 4 = 2^2`, we have :math:`b = 2`. The order of growth is **quadratic**: :math:`T(n) \sim c \cdot n^2` (or :math:`\Theta(n^2)`, up to a potential logarithmic factor).

* What would be the running time for 128000?

  .. answer::

    Since :math:`T(128000) / T(64000) \approx 4`, we estimate:

    .. math::

        T(128000) \approx 4 \times T(64000) = 4 \times 20.5 = 82.0\text{ seconds.}


JVM Memory: Stack, Heap, and Garbage Collector
""""""""""""""""""""""""""""""""""""""""""""""

* What do heap and stack represent when talking about the execution of a program?
* What do the ``-Xmx`` and ``-Xms`` parameters mean when running Java bytecode on the JVM?
* Can these parameters influence the execution speed of a Java program? Why?
* What is the JVM garbage collector?

.. answer::

    * **Call Stack vs. Heap**:

      * The **Stack** stores method call frames, local primitive variables, and object references. Memory on the stack is automatically allocated and freed in LIFO order as methods are called and return.
      * The **Heap** is a shared memory region where all dynamically allocated Java objects (created via ``new``) reside.
    * **JVM flags ``-Xms`` and ``-Xmx``**:

      * ``-Xms`` specifies the **initial** heap memory size allocated by the JVM at startup.
      * ``-Xmx`` specifies the **maximum** heap memory size the JVM is allowed to use (exceeding it throws an ``OutOfMemoryError``).
    * **Influence on execution speed**: Yes. If ``-Xms`` is too small, the JVM must repeatedly request additional memory from the OS and resize the heap. If ``-Xmx`` is tight relative to the program's live data, the garbage collector must run much more frequently, causing significant CPU overhead and pause times.
    * **JVM Garbage Collector (GC)**: An automatic memory management process that periodically identifies objects on the heap that are no longer reachable from any active references and reclaims their memory. Data structures that allocate many small wrapper objects (such as ``Node`` instances in linked lists) create much more GC work than array-based data structures.


Unit Testing, Edge Cases, and Complexity Verification
"""""""""""""""""""""""""""""""""""""""""""""""""""""

* What is a good set of unit tests to verify the correctness of a data structure?
* Do you think about edge cases?
* What could possibly go wrong with this method implementation?

.. code-block:: java

     // return the floor of the average between a and b
     public static int average(int a, int b) {
        return (a + b) / 2;
     }

.. answer::

    ``a + b`` can cause a silent 32-bit signed **integer overflow** if ``a`` and ``b`` are large positive integers (for instance, if ``a = b = Integer.MAX_VALUE``, ``a + b`` overflows to ``-2``).
    To avoid overflow, compute ``a + (b - a) / 2`` (for positive integers) or use the unsigned right-shift operator ``(a + b) >>> 1`` (for non-negative integers).

* How can random data generation be useful for testing data structures?
* Why is it important to work with a fixed seed for testing?
* How can a code coverage analysis tool (such as `JaCoCo <http://eclemma.org/jacoco/>`_)
  help you design tests?
* How can you verify experimentally that the implementation of a data structure or an algorithm has
  the expected theoretical time complexity?
* How can you test the time complexity of your program?

.. answer::

    * **Edge cases**: A good test suite must cover empty structures, single-element structures, duplicate elements, boundary values (``0``, ``Integer.MAX_VALUE``, ``Integer.MIN_VALUE``), resizing boundaries, and invalid operations (e.g., popping from an empty stack throwing the expected exception).
    * **Random data generation & fixed seed**: Randomized tests (fuzzing) can compare your data structure against a trusted reference implementation over thousands of random operations. Using a **fixed random seed** (e.g., ``new Random(42)``) ensures that tests are **deterministic and reproducible**: if a test fails, you can replay the exact same sequence of operations to debug it.
    * **Code coverage (JaCoCo)**: Highlights which lines and conditional branches of your code were never executed by any test, helping you craft tests for uncovered edge cases (Note: 100% coverage does not guarantee the absence of bugs, but low coverage guarantees untested code).
    * **Experimental complexity verification**: You can either measure wall-clock execution time across doubling input sizes (the **doubling ratio test**) or instrument the code to **count elementary operations** (such as comparisons or array accesses), which is deterministic and immune to OS background noise.


SegmentedList and Iterators
"""""""""""""""""""""""""""

You are asked to implement an ADT called a ``SegmentedList`` and the iterator method of this ADT: `SegmentedList <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_SegmentedList>`_.
