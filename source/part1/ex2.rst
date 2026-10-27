.. _part1_ex2:


Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W3.


Circular Linked List
""""""""""""""""""""

* What is the difference between an ``Iterable`` and an ``Iterator``?

  .. answer::

    * ``Iterable<T>`` is an interface with a single required method ``Iterator<T> iterator()`` that produces a new ``Iterator``. It represents a collection that *can be iterated over* (e.g., ``ArrayList``, ``LinkedList``, ``Stack``) and allows the object to be used in Java's enhanced ``for (T item : collection)`` loop.
    * ``Iterator<T>`` is the stateful object that actually performs the traversal over a collection, maintaining the current position and providing ``hasNext()`` and ``next()``. Multiple independent ``Iterator`` instances can traverse the same ``Iterable`` simultaneously.

Implement a `Circular Linked List <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_CircularLinkedList>`_ and its iterator.

In your implementation, what is the time complexity of:

* ``public void enqueue(Item item)``?
* ``public Item remove(int index)``?
* a sequence of operations consisting of *creating an iterator and then iterating over the first k elements*?

.. answer::

    * ``enqueue(Item item)``: :math:`\Theta(1)` using the ``last`` pointer (since ``last.next`` points to the first node, inserting after ``last`` and updating ``last`` takes constant time).
    * ``remove(int index)``: :math:`\Theta(\text{index})` (or :math:`\mathcal{O}(n)` in the worst case), as we must traverse ``index`` links from the first node to reach the node preceding the target index.
    * Creating an iterator and iterating over the first :math:`k` elements: :math:`\Theta(k)` (:math:`\Theta(1)` to initialize the iterator at ``last.next``, and :math:`\Theta(1)` per call to ``next()``).


Implement a Stack with an Array
"""""""""""""""""""""""""""""""

In your implementation, you will need to resize the array if the size of the stack reaches the maximum size.
Does Java have an efficient way to resize/refill an array? If yes, give an example of Java code to perform this operation.

.. answer::

    Yes, ``System.arraycopy`` (or ``Arrays.copyOf``, which calls ``System.arraycopy`` internally) copies a contiguous block of memory natively and efficiently:

    .. code-block:: java

        E[] newArray = (E[]) new Object[array.length * 2];
        System.arraycopy(array, 0, newArray, 0, size);
        array = newArray;

Implement the `Stack <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_Stack>`_ interface with an internal array-based implementation and with a linked list.

In your implementation, what is the time complexity of:

* ``public void push(E item)``?
* a sequence of :math:`n` ``push`` operations?

.. answer::

    * A single call to ``push(E item)`` takes :math:`\mathcal{O}(n)` time in the worst case (when the array is full and must be resized) and :math:`\Theta(1)` **amortized** time.
    * A sequence of :math:`n` ``push`` operations starting from an empty stack takes :math:`\Theta(n)` time in total.


Reverse Polish Notation Evaluation
""""""""""""""""""""""""""""""""""

Postfix notation (or `Reverse Polish notation <https://en.wikipedia.org/wiki/Reverse_Polish_notation>`_) is used
to represent algebraic expressions.
For simplicity, we only consider postfix expressions with positive integers
and the ``+`` and ``*`` operators: for example, ``2 3 1 * + 9 *``, which evaluates to 45,
and ``4 20 + 3 5 1 * * +``, which evaluates to 39.

1. Write an algorithm in Java to evaluate a postfix expression from a string of :math:`n` characters.
2. What data structure do you use?
3. What is the time and space complexity of your algorithm?

As a reminder, here is how you can iterate over the elements of a string that are separated by spaces:

.. code-block:: java

    String in = "4 20 + 3 5 1 * * +";
    StringTokenizer tokenizer = new StringTokenizer(in);
    while (tokenizer.hasMoreTokens()) {
         String element = tokenizer.nextToken();
    }

.. answer::

    1. **Java implementation**:

       .. code-block:: java

           public static int evaluatePostfix(String in) {
               Deque<Integer> stack = new ArrayDeque<>();
               StringTokenizer tokenizer = new StringTokenizer(in);
               while (tokenizer.hasMoreTokens()) {
                   String token = tokenizer.nextToken();
                   if (token.equals("+")) {
                       int b = stack.pop();
                       int a = stack.pop();
                       stack.push(a + b);
                   } else if (token.equals("*")) {
                       int b = stack.pop();
                       int a = stack.pop();
                       stack.push(a * b);
                   } else {
                       stack.push(Integer.parseInt(token));
                   }
               }
               return stack.pop();
           }

    2. **Data structure**: A **Stack** (LIFO). Each operand is pushed onto the stack, and each binary operator pops the top two operands, applies the operation, and pushes the result back onto the stack.
    3. **Complexity**: Each token is processed once and triggers a constant number of :math:`\mathcal{O}(1)` stack operations, so the **time complexity is** :math:`\Theta(n)` and the **space complexity is** :math:`\mathcal{O}(n)` in the worst case (proportional to the maximum number of operands on the stack).


Functional Lists
""""""""""""""""

`Functional Programming <https://en.wikipedia.org/wiki/Functional_Programming>`_ is an increasingly important programming paradigm.
In this programming paradigm, data structures are `immutable <https://en.wikipedia.org/wiki/Purely_functional_data_structure>`_.
We are interested here in implementing an immutable list called *FList* designed for use in a functional framework.
Here is the API of *FList*:

.. code-block:: java

    public abstract class FList<A> implements Iterable<A> {

        // creates an empty list
        public static <A> FList<A> nil();

        // prepend a to the list and return the new list
        public final FList<A> cons(final A a);

        public final boolean isNotEmpty();

        public final boolean isEmpty();

        public final int length();

        // return the head element of the list
        public abstract A head();

        // return the tail of the list
        public abstract FList<A> tail();

        // return a list where function f has been applied to each element
        public final <B> FList<B> map(Function<A,B> f);

        // return a list containing only the elements that satisfy the predicate
        public final FList<A> filter(Predicate<A> f);

        // return an iterator over the elements of the list
        public Iterator<A> iterator();

    }

As you can see, none of the methods allow you to modify the state of the list.
Here is an example of manipulating such a list.
If you are unfamiliar with Java 8 `functional interfaces <https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html>`_,
we recommend familiarizing yourself with them first.

.. code-block:: java

        FList<Integer> list = FList.nil();

        for (int i = 0; i < 10; i++) {
            list = list.cons(i);
        }
        // list = 9,8,7,...,0
        
        list = list.map(i -> i+1);
        // will print 10,9,...,1
        for (Integer i: list) {
            System.out.println(i);
        }

        list = list.filter(i -> i%2 == 0);
        // will print 10,...,6,4,2
        for (Integer i: list) {
            System.out.println(i);
        }

Here is a partial implementation of the ``FList``:

.. code-block:: java

        import java.util.Iterator;
        import java.util.NoSuchElementException;
        import java.util.function.Function;
        import java.util.function.Predicate;

        public abstract class FList<A> implements Iterable<A> {

            public final boolean isNotEmpty() {
                return this instanceof Cons;
            }

            public final boolean isEmpty() {
                return this instanceof Nil;
            }

            public final int length() {
                // TODO
            }

            public abstract A head();

            public abstract FList<A> tail();

            public static <A> FList<A> nil() {
                return (Nil<A>) Nil.INSTANCE;
            }

            public final FList<A> cons(final A a) {
                return new Cons(a, this);
            }

            public final <B> FList<B> map(Function<A,B> f) {
                // TODO
            }

            public final FList<A> filter(Predicate<A> f) {
                // TODO
            }

            public Iterator<A> iterator() {
                return new Iterator<A>() {
                    // complete this class

                    public boolean hasNext() {
                      // TODO
                    }

                    public A next() {
                      // TODO
                    }

                    public void remove() {
                        throw new UnsupportedOperationException();
                    }
                };
            }

            private static final class Nil<A> extends FList<A> {
                public static final Nil<Object> INSTANCE = new Nil();
                // TODO
            }

            private static final class Cons<A> extends FList<A> {
                // TODO
            }

        }

We ask you to:

* complete this implementation (prefer recursive methods where appropriate).
* determine the time complexity of each method.

The INGInious task is the following: `FList <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_FList>`_.

.. answer::

    * ``nil()``, ``cons(a)``, ``isEmpty()``, ``isNotEmpty()``, ``head()``, ``tail()``: :math:`\Theta(1)` time. Note that ``tail()`` simply returns the reference to the rest of the immutable list without copying anything.
    * ``length()``: :math:`\Theta(n)` if computed recursively (``isEmpty() ? 0 : 1 + tail().length()``), or :math:`\Theta(1)` if cached as a ``final int size`` field inside ``Cons`` upon construction.
    * ``map(f)``: ``isEmpty() ? nil() : tail().map(f).cons(f.apply(head()))`` — runs in :math:`\Theta(n)` time and allocates :math:`n` new ``Cons`` nodes.
    * ``filter(p)``: ``if (isEmpty()) return nil(); FList<A> rest = tail().filter(p); return p.test(head()) ? rest.cons(head()) : rest;`` — runs in :math:`\Theta(n)` time.


Complexity of List, Stack, and Queue Implementations
""""""""""""""""""""""""""""""""""""""""""""""""""""

Fill in the following table with the time complexity of each operation.
If an operation is not supported (for example, accessing the middle of a Stack is not supported by the ADT), indicate it with a cross.
Specify in each case whether it is an amortized complexity.
SL = Singly Linked List, DL = Doubly Linked List, Arr = Resizing Array.

.. list-table:: Complexity
   :header-rows: 1

   * - ADT
     - Implementation
     - Insertion (head)
     - Insertion (end)
     - Insertion (pos :math:`i`)
     - Remove (head)
     - Remove (end)
     - Remove (pos :math:`i`)
     - Get (head)
     - Get (end)
     - Get (pos :math:`i`)
   * - Stack
     - SL
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - Queue
     - SL
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - Stack
     - Arr
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - Queue
     - Arr
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - List
     - SL
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - List
     - DL
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - List
     - Arr
     -
     -
     -
     -
     -
     -
     -
     -
     -


.. answer::

    .. list-table:: Complexity Summary
       :header-rows: 1

       * - ADT
         - Implementation
         - Insertion (head)
         - Insertion (end)
         - Insertion (pos :math:`i`)
         - Remove (head)
         - Remove (end)
         - Remove (pos :math:`i`)
         - Get (head)
         - Get (end)
         - Get (pos :math:`i`)
       * - Stack
         - Singly Linked List (top at head)
         - :math:`\Theta(1)`
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
       * - Queue
         - Singly Linked List (with tail ptr)
         - /
         - :math:`\Theta(1)`
         - /
         - :math:`\Theta(1)`
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
       * - Stack
         - Resizing Array (top at end)
         - /
         - :math:`\Theta(1)` amortized
         - /
         - /
         - :math:`\Theta(1)` amortized
         - /
         - /
         - :math:`\Theta(1)`
         - /
       * - Queue
         - Resizing Circular Array
         - /
         - :math:`\Theta(1)` amortized
         - /
         - :math:`\Theta(1)` amortized
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
       * - List
         - Singly Linked List (with tail ptr)
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
       * - List
         - Doubly Linked List
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(\min(i, n-i))`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(\min(i, n-i))`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(\min(i, n-i))`
       * - List
         - Resizing Array
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` amortized
         - :math:`\Theta(n - i)`
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` amortized
         - :math:`\Theta(n - i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`


Java Collections and Common Implementation Pitfalls
"""""""""""""""""""""""""""""""""""""""""""""""""""

* Does Java provide classes for ``Stack``, ``Vector``, ``List``?
  If so, in which package? In your opinion, is it important to know this package well for the exam?
  Is ``List`` an interface or a class?
  How can you create an object of type ``List``? What about an object of type ``Queue``?

  .. answer::

    All standard collection interfaces and implementations are in the ``java.util`` package. Knowing ``java.util`` well is essential for the exam!
    Both ``List`` and ``Queue`` are **interfaces**, not concrete classes, so you cannot instantiate them directly with ``new List<>()`` or ``new Queue<>()``. Instead, you instantiate a concrete implementation such as:

    .. code-block:: java

        List<Integer> list = new ArrayList<>();      // or new LinkedList<>()
        Queue<Integer> queue = new LinkedList<>();   // or new ArrayDeque<>()

* What is the error in the following code where the student is trying to create an array of 5 lists and then insert the integer 4 into the 3rd list? Correct the code.

  .. code-block:: java

    List<Integer>[] myList = new List<Integer>[5];
    myList[2].add(4);

  .. answer::

    There are two errors:

    1. Java does not allow direct generic array creation (``new List<Integer>[5]`` causes a compile-time error); you must cast a raw array ``(List<Integer>[]) new List[5]``.
    2. All array entries are initially ``null``, so calling ``myList[2].add(4)`` throws a ``NullPointerException`` unless each list is instantiated first:

    .. code-block:: java

        List<Integer>[] myList = (List<Integer>[]) new List[5];
        for (int i = 0; i < myList.length; i++) {
            myList[i] = new LinkedList<>();
        }
        myList[2].add(4);

* What is the error in the following code where the student is trying to create an ``Iterable`` object? Correct the code.

  .. code-block:: java

    Iterable<Integer> myIterable = new Iterable<Integer>();

  .. answer::

    ``Iterable`` is an **interface**, so it cannot be instantiated directly without implementing its ``iterator()`` method. You should instantiate a concrete class implementing ``Iterable`` (such as ``ArrayList`` or ``LinkedList``):

    .. code-block:: java

        Iterable<Integer> myIterable = new ArrayList<>();

* What is the error in the following code where the student is trying to define a constructor?

  .. code-block:: java

    public class ADT {
      private int n = 4;
      private ADT myAdt;
      public ADT(int n) {
        n = n;
        myAdt = new ADT(4);
      }
    }

  .. answer::

    There are two bugs:

    1. **Variable shadowing**: ``n = n;`` assigns the parameter ``n`` to itself instead of updating the instance field. It should be ``this.n = n;``.
    2. **Infinite recursion**: ``myAdt = new ADT(4);`` inside the constructor unconditionally calls the constructor again, causing a ``StackOverflowError`` at runtime.

* What is the time complexity of this code, given a list of size :math:`n`? How can it be improved?

  .. code-block:: java

    void printList(List<Integer> l) {
        for (int i = 0; i < l.size(); i++) {
            int elem = l.get(i);
            System.out.println(elem);
        }
    }

  .. answer::

    If ``l`` is a ``LinkedList``, ``l.get(i)`` takes :math:`\Theta(i)` time, making the loop run in :math:`\Theta(n^2)` time!
    To guarantee :math:`\Theta(n)` time regardless of the ``List`` implementation, use an ``Iterator`` or a ``for``-each loop:

    .. code-block:: java

        void printList(List<Integer> l) {
            for (Integer elem : l) {
                System.out.println(elem);
            }
        }
