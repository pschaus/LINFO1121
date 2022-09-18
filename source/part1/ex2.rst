.. _part1_ex2:


Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W3.


Exercise 1.2.1 (Inginious)
""""""""""""""""""""""""""""

* What is the difference between an Iterable and an Iterator?

  .. answer::

    An ``Iterable`` is an interface with the method ``iterator()`` producing an iterator.
    An ``Iterable`` is thus a class that can be iterated over (``Vector``, ``Stack``, ``ArrayList``, etc).
    But the real instrument for iteration is the iterator itself (with ``next``, ``hasNext``, etc).
    Any ``Iterable`` object can be used in the for loops with syntactical sugar: ``for (int a: myIterable)``




Implement a `Circular Linked List <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_CircularLinkedList>`_ and its iterator.

In your implementation, what is the time complexity of:

* `public void enqueue(Item item)`?
* `public Item remove(int index)` ?
*  a sequence of operations which consists of *creating an iterator and then iterating over the first k-elements*?


Exercise 1.2.1 (Inginious)
""""""""""""""""""""""""""


In your implementation, you will need to resize the array if the size of the stack reaches the maximum size.
oes Java have an efficient way to resize/refill an array? If yes, give an example of Java code to perform this operation.

  .. answer::

    System.arraycopy


Implement the `Stack <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_Stack>`_ interface with an internal array-based implemenation and with a linked-list.

In your implementation, what is the time complexity of:

* `public void push(E item)`?
*  a sequence of n `push` operations



Exercise 1.2.2
""""""""""""""

Post-fix notation (or `Inverse Polish <https://en.wikipedia.org/wiki/Inverse_Polish_Notation>`_) is used
to represent algebraic expressions.
We consider for simplicity only post-fix expressions with positive integers
and the `+` and `*` operators. For example `2 3 1 * + 9 *` whose result is 45
and the result of `4 20 + 3 5 1 * * +` is 39.

1. Write an algorithm in Java to evaluate a post-fix expression from a string of n-characters.
2. What data structure do you use?
3. What is the complexity of your algorithm (temporal and spatial)?

As a reminder, here is how you can iterate over the elements of a string that are separated by spaces.

.. code-block:: java


    String in = "4 20 + 3 5 1 * * +";
    StringTokenizer tokenizer = new StringTokenizer(in);
    while (tokenizer.hasMoreTokens()) {
         String element = tokenizer.nextToken();
    }


Exercise 1.2.3
""""""""""""""

`Functional Programming <https://en.wikipedia.org/wiki/Functional_Programming>`_ is an increasingly important programming paradigm.
In this programming paradigm, data structures are `immutable <https://en.wikipedia.org/wiki/Purely_functional_data_structure>`_.
We are interested here in the implementation of an immutable list called *FList* allowing to be used in a functional framework.
Here is the API of a *FList*

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

        // return a list on which each element has been applied function f
        public final <B> FList<B> map(Function<A,B> f);

        // return a list on which only the elements that satisfies predicate are kept
        public final FList<A> filter(Predicate<A> f);

        // return an iterator on the element of the list
        public Iterator<A> iterator();

    }


As you can see, none of the methods allow you to modify the state of the list.
Here is an example of manipulation of such a list.
If you are unfamiliar with the `<https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html>`_ functional interfaces of Java8,
we ask that you familiarize yourself with these first.



.. code-block:: java


        FList<Integer> list = FList.nil();

        for (int i = 0; i < 10; i++) {
            list = list.cons(i);
        }

        list = list.map(i -> i+1);
        // will print 1,2,...,11
        for (Integer i: list) {
            System.out.println(i);
        }

        list = list.filter(i -> i%2 == 0);
        // will print 2,4,6,...,10
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


We ask you to


* complete this implementation, if possible use recursive methods as much as possible.
* determine the complexity of each method.



Exercise 1.2.4
""""""""""""""""""""""

Fill in the following table with the complexities of each operation?
If an operation is not possible (for example, going to the middle of a Stack is impossible because not provided for by the TAD, indicate it with a cross.
Specify each time if it is an amortized complexity or not.
SL = Simply Linked List, DL = Doubly Linked List, Arr = Array with redimentioning.



.. list-table:: Complexité
   :header-rows: 1

   * - TAD
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
   * - Liste
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


What is this ?



 .. answer::


    .. list-table:: Complexité
       :header-rows: 1

       * - TAD
         - Implémentation
         - Insertion (début)
         - Insertion (fin)
         - Insertion (pos :math:`i`)
         - Supprimer (début)
         - Supprimer (fin)
         - Supprimer (pos :math:`i`)
         - Voir (début)
         - Voir (fin)
         - Voir (pos :math:`i`)
       * - Stack
         - Liste chainée
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
         - Liste chainée
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
         - Tab. redim.
         - /
         - :math:`\Theta(1)` a
         - /
         - /
         - :math:`\Theta(1)` a
         - /
         - /
         - :math:`\Theta(1)`
         - /
       * - Queue
         - Tab. redim.
         - /
         - :math:`\Theta(1)` a
         - /
         - :math:`\Theta(1)` a
         - /
         - /
         - :math:`\Theta(1)`
         - /
         - /
       * - Liste
         - Simpl. Chainée
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(n)`
         - :math:`\Theta(i)`
       * - Liste
         - Doub. Chainée
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(i)`
       * - Liste
         - Tab. redim.
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` a
         - :math:`\Theta(n)`
         - :math:`\Theta(n)`
         - :math:`\Theta(1)` a
         - :math:`\Theta(n)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`
         - :math:`\Theta(1)`



Exercice 1.2.5
"""""""""""""""""

* Does Java provide a class for ``Stack``, ``Vector``, ``List``?
   If so in which package? In your opinion, is it interesting to know this package well for the exam?
   Is ``List`` an interface or a class?
   How to create an object of type ``List``? And an object of type ``Queue``?

  .. answer::

    Most the algorithms covered in this class are available in ``java.util`` (part of standard Java).
    You will spare a lot of time and maximize your chances to succeed if you know well
    ``java.util`` most common classes.
    We have seen at the exam students trying to instantiate object from ``java.util.List``, not understanding
    the differences between interfaces and implementation. The same goes for ``java.util.Queue``...
    Present them the ``ArrayList`` class.



* What is the error in the following code where the student is looking to create an array of 5 lists and then insert the integer 4 into the 3rd list? Correct the code.

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

* What is the time complexity of is this code, given the size of the list, :math:`n`? How to improve it?

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


