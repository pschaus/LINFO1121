.. _part1_ex2:


Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W3.


Exercise 1.2.1 (INGInious: Circular Linked List)
""""""""""""""""""""""""""""""""""""""""""""""""

* What is the difference between an ``Iterable`` and an ``Iterator``?

  .. answer::

    An ``Iterable`` is an interface with the method ``iterator()`` producing an iterator.
    An ``Iterable`` is thus a class that can be iterated over (``Vector``, ``Stack``, ``ArrayList``, etc).
    But the real instrument for iteration is the iterator itself (with ``next``, ``hasNext``, etc).
    Any ``Iterable`` object can be used in enhanced for-loops (syntactic sugar): ``for (int a: myIterable)``




Implement a `Circular Linked List <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_CircularLinkedList>`_ and its iterator.

In your implementation, what is the time complexity of:

* `public void enqueue(Item item)`?
* `public Item remove(int index)`?
* a sequence of operations consisting of *creating an iterator and then iterating over the first k elements*?


Exercise 1.2.2 (INGInious: Implement a stack with an Array)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In your implementation, you will need to resize the array if the size of the stack reaches the maximum size.
Does Java have an efficient way to resize/refill an array? If yes, give an example of Java code to perform this operation.

.. answer::

    System.arraycopy


Implement the `Stack <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_Stack>`_ interface with an internal array-based implementation and with a linked list.

In your implementation, what is the time complexity of:

* `public void push(E item)`?
* a sequence of :math:`n` `push` operations?



Exercise 1.2.3
""""""""""""""

Postfix notation (or `Reverse Polish notation <https://en.wikipedia.org/wiki/Reverse_Polish_notation>`_) is used
to represent algebraic expressions.
For simplicity, we only consider postfix expressions with positive integers
and the `+` and `*` operators: for example, `2 3 1 * + 9 *`, which evaluates to 45,
and `4 20 + 3 5 1 * * +`, which evaluates to 39.

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


Exercise 1.2.4 (INGInious: Functional Lists)
""""""""""""""""""""""""""""""""""""""""""""

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


Here is a partial implementation of the `FList`


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




Exercise 1.2.5
""""""""""""""

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
         - Singly Linked List
         - /
         - :math:`\Theta(1)`
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
         - :math:`\Theta(1)`
         - /
       * - Queue
         - Singly Linked List
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
         - Resizing Array
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
         - Resizing Array
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
         - Singly Linked List
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
       * - List
         - Doubly Linked List
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
       * - List
         - Resizing Array
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` amortized
         - :math:`\Theta(n)`
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` amortized
         - :math:`\Theta(n)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`



Exercise 1.2.6
""""""""""""""

* Does Java provide classes for ``Stack``, ``Vector``, ``List``?
  If so, in which package? In your opinion, is it important to know this package well for the exam?
  Is ``List`` an interface or a class?
  How can you create an object of type ``List``? What about an object of type ``Queue``?

  .. answer::

    Most of the algorithms covered in this class are available in ``java.util`` (part of standard Java).
    You will save a lot of time and maximize your chances of success if you know the most common classes in ``java.util`` well.
    In past exams, we have seen students trying to instantiate an object from ``java.util.List``, failing to understand
    the difference between interfaces and implementations. The same goes for ``java.util.Queue``...
    Introduce the ``ArrayList`` class to them.



* What is the error in the following code where the student is trying to create an array of 5 lists and then insert the integer 4 into the 3rd list? Correct the code.

  .. code-block:: java

    List<Integer>[] myList = new List<Integer>[5];
    myList[2].add(4);

  .. answer::

      .. code-block:: java

        List<Integer>[] myList = new List<Integer>[5];
        for(int i = 0; i < myList.length; i++)
            myList[i] = new LinkedList<>();
        myList[2].add(4);

* What is the error in the following code where the student is trying to create an Iterable object? Correct the code.

  .. code-block:: java

    Iterable<Integer> myIterable = new Iterable<Integer>();

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

* What is the time complexity of this code, given a list of size :math:`n`? How can it be improved?

  .. code-block:: java

    void printList(List<Integer> l) {
        for (int i = 0; i < l.size(); i++) {
            int elem = l.get(i);
            System.out.println(elem);
        }
    }

  .. answer::

    C'est du :math:`\Theta(n^2)` avec certaines implémentations usuelles de listes.

    .. code-block:: java

        void printList(List<Integer> l) {
            for(Integer elem: l) {
                System.out.println(elem);
            }
        }

    ou

    .. code-block:: java

        void printList(List<Integer> l) {
            Iterator<Integer> itr = l.iterator();
            while(itr.hasNext()) {
                int elem = itr.next();
                System.out.println(elem);
            }
        }


