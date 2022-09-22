.. _part1_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W2.


Exercise 1.1.1
""""""""""""""

Define what an abstract data type (ADT) is. In java, is it better to describe an ADT by a
class or an interface? Why?

.. answer::

    Page 64 of the book. In java, we use an interface, because a class is either

    * useless because it is completely abstract (it might as well be replaced by an interface)
    * already imposes a method to implement the ADT.

    There are some cases where you want to use an abstract class rather than an interface.
    For example, to reuse code that we know to be common to all possible implementations.

    A practical example: an abstract class could implement ``isEmpty()`` from
    from ``size()`` (``return size() == 0``). But since java 8, we can also have a default implementation
    of methods in interfaces so that is not totally true.


Exercise 1.1.2
""""""""""""""

How to implement a *stack* by a simply linked list where the operations
and `pop` operations are done at **end of list**? Is this solution efficient? Argue.


.. answer::

    In practice, on the exam, you will need to implement it! Remind students that they need to do more
    that they need to do more than just understand the general idea. This is a good exercise to do yourself in IntelliJ.

Exercise 1.1.3
""""""""""""""

What are the possible implementations for a stack? By consulting the Java API documentation, describe
the implementation of a stack by the class `java.util.Stack`. Go to the source code of the implementation
`java.util.Stack` (crtl+B from IntelliJ).

Why do you think Java developers chose this implementation
(hint: argue about memory and garbage collection)?

.. answer::

    Stack étends Vector, qui est un tableau contigu redimensionable.

    Evidemment, cela permet d'éviter de créer plein de petits objets "noeuds" en mémoire,
    et donc d'utiliser moins le garbage collector et le heap.

    La complexité est donc un peu plus complexe que l'habituel ":math:`\mathcal{O}(1)` pour push/pop".
    La vérité est que c'est une complexité amortie!

    C'est un bon moment pour prendre le temps d'expliquer à tout les groupes en même temps,
    au tableau, comme fonctionne un tableau redimensionnable en temps amorti constant.

    Soit un tableau de taille 1, initialement vide. On double la taille du tableau
    à chaque fois qu'il est complet:

    * insérer un élément quand le tableau n'est pas plein est en :math:`\mathcal{O}(1)`
    * dans le cas contraire, il faut faire une copie du tableau dans un nouvel emplacement
      mémoire deux fois plus grand. Une opération en :math:`\mathcal{O}(n)` où :math:`n`
      est la taille courante du tableau.

    Si on fait le calcul, en ajoutant :math:`n=2^m` objets. On va avoir une opération de redimensionnement
    quand le tableau fait une taille :math:`1, 2, 4, 8, 16, ... n/2, n`. Ce sont des puissances de deux...
    On a que

    .. math::

        \sum_{i=0}^m 2^i = 2^{m+1}-1 = 2n-1

    Autrement dit, les opérations de resize sur :math:`n` insertions sont EN TOUT en :math:`\mathcal{O}(n)`.
    Rapporté par opération, ça fait :math:`\mathcal{O}(1)`. Magie.

    Note rigolote: Java recommande d'utiliser Deque à la place de Stack.
    "Qu'est-ce que ça change?" est une bonne question à poser aux étudiants.

Exercise 1.1.4 (Inginious)
""""""""""""""""""""""""""

How do you implement the abstract data type *stack* using two *queues*?
In particular, describe how the `push` and `pop` methods work in this case.

As an example, specify the state of each of the two queues after stacking the integers `1 2 3` from an initially empty
initially empty. Describe what happens next when the `pop` operation is performed.

What is the time complexity of these methods if we assume that each `queue` and `dequeue` operation
operations are executed in constant time?

Is this implementation of a stack efficient (for :math:`n` operations)
compared to the other implementations presented in the reference book?


Once you have imagined your solution on paper, you can solve the corresponding Inginious task `StackWithTwoQueues <https://inginious.info.ucl.ac.be/course/LINFO1121/fundamentals_StackWithTwoQueues>`_ .

.. answer::

    Il y a plusieurs possibilités. En voici deux:

    *   Méthode 1. On maintien l'ordre FIFO dans la file 1 en permanence.

        * ``push`` pousse dans la première file (:math:`\mathcal{O}(1)`)

          .. code-block:: java

            a.add(x);

        * ``pop`` "vide" la file 1 dans la file 2, renvoie le dernier élément, puis remet tout dans la première file (:math:`\mathcal{O}(n)`)

          .. code-block:: java

            if (a.size() == 0)
                throw new EmptyStackException();
            while (a.size() != 1)
                b.add(a.remove());
            int out = a.remove();
            while (b.size() != 0)
                a.add(b.remove());
            return out;
    *   Méthode 2. On maintien l'ordre LIFO dans la file 1 en permanence.

        * ``pop`` retire un élément de la file 1 (:math:`\mathcal{O}(1)`)

          .. code-block:: java

            return a.remove();

        * ``push`` ajoute l'élément à la file 2, vide la file 1 dans la file 2, et intervertit les files. (:math:`\mathcal{O}(n)`)

          .. code-block:: java

            b.add(x);
            while (a.size() != 0)
                b.add(a.remove());
            Queue<Integer> tmp = a;
            a = b;
            b = tmp;

    Il y a beaucoup d'autres manières de faire, mais elles sont toutes en :math:`\mathcal{O}(n)` sur au moins une des deux opérations.


Exercise 1.1.5
""""""""""""""


What do you think about these three different ways of iterating over the elements of a `java.util.LinkedList? Are they equivalent? Use a time-complecity argument.

.. code-block:: java

    LinkedList<Integer> list = new LinkedList<>();

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


    Les deux premières sont équivalentes (lors de la première, Java utilise en arrière-plan
    un itérateur... c'est un sucre syntaxique): :math:`\mathcal{O}(n)` pour visiter la liste.

    Malheureusement, ``list.get(i)`` est une opération en :math:`\mathcal{O}(n)` sur une liste,
    et donc la troisième boucle est en :math:`\mathcal{O}(n^2)`!

    Cela montre l'utilité d'un itérateur. Il permet de contenir de l'information sur "où on se trouve"
    dans la structure de données, et permet d'éviter de refaire plusieurs fois le même travail.


Exercise 1.1.6
"""""""""""""""


The :math:`\sim` (tilde) notation is used in the reference book for the analysis of the calculation times of
algorithms. How this notation differs or resembles the more classically used notations :math:`\mathcal{O}`
(big Oh), :math:`\mathcal{\Omega}` (big Omega) and :math:`\mathcal{\Theta}` (big Theta)?

Explain precisely the links and similarities between them.
What do you see as the advantage of using :math:`\sim` (tilde) notation rather than :math:`\mathcal{O}`
when possible?

.. answer::

    Voir le document sur les complexités: :ref:`part1complexity`.

Exercise 1.1.7
""""""""""""""

Explain how we can extract the characterization :math:`\sim` (tilde) from the implementation of an algorithm to
using the *Doubling ratio* test.

* How does this test work?

  .. answer::

    Si :math:`T(N)\sim aN^b\log N` alors :math:`T(2N)/T(N)\sim 2^b`.

    L'idée est donc de doubler la taille de l'entrée à chaque fois, d'en approximer la valeur de :math:`b`
    Et puis de donner une idée de l'ordre de grandeur.


* What are the limitations and advantages of this test?

  .. answer::

    L'avantage est la simplicité de l'approche, mais l'algorithme se révèle rapidement
    impraticable car les tailles d'input augmentent très vite.

    Par ailleurs, le facteur :math:`\log N` est souvent inexistant en pratique; ce n'est pas
    une méthode qui permet de prouver une complexité, seulement d'en avoir une idée générale.

Suppose we measure the following :math:`T(n)` execution times (in seconds) of a program as a function of the
input size :math:`n`:

============  ==== ==== ==== ==== ===== ===== =====
:math:`n`     1000 2000 4000 8000 16000 32000 64000
:math:`T(n)`  0    0    0.1  0.3  1.3   5.1   20.5
============  ==== ==== ==== ==== ===== ===== =====

* How can you best characterize the growth order of this function?

  .. answer::

    ===================  ================  ================  ==== ==== ===== ===== =====
    :math:`n`            1000              2000              4000 8000 16000 32000 64000
    :math:`T(n)`         0                 0                  0.1  0.3   1.3   5.1  20.5
    :math:`T(2n)/T(n)`   :math:`\simeq 1`  :math:`\simeq 1`     3  4.3   3.9   4.0
    ===================  ================  ================  ==== ==== ===== ===== =====

    On a donc :math:`2^b \sim 4.0`, :math:`b=2`. On serait donc théoriquement en :math:`\mathcal{O}(n^2\log n)`.
    En pratique, cette fonction est en :math:`\mathcal{O}


* What would be the running time for 128000?

  .. answer::

    :math:`T(128000)/T(64000)\sim 4 \rightarrow T(128000)\sim 4*T(64000)=82`.



Exercise 1.1.8
"""""""""""""""

* What do heap and stack mean when talking about the execution of a program in a programming language?
* What do the -Xmx, -Xms parameters mean that we can pass to the JVM for the execution of a bytecode?
* Can these parameters influence the execution speed of a Java program? Why?
* What is the JVM garbage collector

.. answer::

    A good opportunity to recall/introduce the notion of amortized constant time complexity.
    Depite the fact that operations using an array are amortized constant time, they are generally preferred
    because they generate less objects on the heap that eventually will be garbabe collected (Nodes, etc).
    Garbage collection can substantially slow down the execution.
    Extreme case: you do a series of consecutive push, pop, push, pop, etc...

Exercise 1.1.9
"""""""""""""""

* What is a good set of unit tests to verify the correctness of a data structure?
* Do you think about borderline cases?
* What could possibly go wrong with the implementation of this method implementation?

.. code-block:: java

     // return the floor of the average between a and b
     public static int average(int a, int b) {
        return (a + b) / 2;
     }

.. answer::

    a + b might cause a (silent) int overflow, for instance if a = b = Integer.MAXINT
    to avoid it, the implementation should be a + (b-a)/ 2 (assuming b is the largest number here)

* How can random data generation be useful for testing data structures?
* Why is it important to work with a fixed seed for testing?
* How a code coverage analysis tool can be useful (such as `Jacoco <http://eclemma.org/jacoco/>`_)
   to help you design tests.
* How to verify experimentally that the implementation of a data structure or an algorithm has
   the expected theoretical time complexity?
* How can you test the time complexity of your program?

.. answer::

    testing time is not always easy (possible using doubling ratio test), couting operations might be a good alternative
