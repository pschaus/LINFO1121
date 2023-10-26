.. _part1complexity:


*************************************************************************************************
Complexity
*************************************************************************************************

Please note that all definitions here are for positive functions with one integer argument, but are almost identical
for multivariate functions from other sets.

Notation Big-Oh (:math:`\mathcal{O}`)
=====================================

.. math::

    f(n) \in \mathcal{O}(g(n)) \quad \Longleftrightarrow \quad
        \exists k \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ s.t. } \quad
        f(n) \leq k \cdot g(n) \quad
        \forall n \geq n_0

A function :math:`f(n)` is said to belong to :math:`\mathcal{O}(g(n))` if there is a constant :math:`k`,
such that :math:`k \cdot g(n)` is systematically greater than :math:`f(n)` for all :math:`n` large enough
(that is, there is a :math:`n_0` from which the rule is satisfied).

:math:`g(n)` therefore works as an upper bound on the function up to a constant.

Example
-------

Let :math:`f(n) = 2n^2+3n`. We have that :math:`f(n)\in \mathcal{O}(n^2)` (in other words, we choose :math:`g(n)=n^2`).
Indeed, with :math:`k=3`, the rule is respected from :math:`n=3`.

Similarly, the same function :math:`f(n) = 2n^2+3n` belongs to other sets:


* :math:`f(n) \in \mathcal{O}(n^3)`
* :math:`f(n) \in \mathcal{O}(n^4)`
* ...
* :math:`f(n) \in \mathcal{O}(2^n)`
* ...

because all these functions are upper bounds than :math:`n^2` when :math:`n` is large.

In the majority of cases, we will want to choose the smallest possible :math:`g(n)` function that respects the
property, since it will give us the most information.

Notation Big-Omega (:math:`\Omega`)
=============================================

The definition is similar to that of Big-Oh. In bold the differences:

.. math::

    f(n) \in \mathbf{\Omega}(g(n)) \quad \Longleftrightarrow \quad
        \exists k \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ s.t. } \quad
        \mathbf{k \cdot f(n) \geq g(n)} \quad
        \forall n \geq n_0

For large values of :math:`n`, :math:`f(n)` is always greater than :math:`g(n)` to a constant
close. Concretely, this means that the function :math:`g(n)` places a bound
lower on the complexity of :math:`f(n)`. In other words, :math:`g(n)` characterizes the
"best case" possible for the calculation of f(n) (this is an abuse of language: see below).

Example
-------

In the general case, Insert outputs :math:`\in \Omega(n)`.

Notation Big-Theta (:math:`\Theta`)
=============================================

.. math::

    f(n) \in \mathbf{\Theta}(g(n)) \quad \Longleftrightarrow \quad
        \exists k_0,k_1 \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ s.t. } \quad
        \mathbf{k_0 \cdot g(n) \leq f(n) \leq k_1 \cdot g(n)} \quad
        \forall n \geq n_0

In other words, for large values of :math:`n`, :math:`f(n)` behaves like :math:`g(n)` up to a multiplicative constant. 
:math:`g(n)` thus acts as both a lower and an upper bound.

One can easily see that (proof left as an exercise)

.. math::

    f(n) \in \mathbf{\Theta}(g(n)) \quad \Longleftrightarrow \quad f(n) \in \mathbf{\mathcal{O}}(g(n)) \quad\wedge\quad f(n) \in \mathbf{\Omega}(g(n))

Notes
---------

It is not possible to find a :math:`g(n)` function such as :math:`f(n) \in \Theta(g(n))` for any :math:`f(n) function )`.
For example, for Insertion sort, Since it is in :math:`\mathcal{O}(n^2)` but in :math:`\Omega(n)`, and that these two bounds are reached,
it is not possible to say that Insertion is in :math:`\Theta(g(n))`.

Example
-------

Merge sort is in :math:`\Theta(n\log_2 n)`.

Notation Tilde (:math:`\mathcal{\sim}`)
=======================================

The definition of tilde notation is based on different principles:

.. math::

    f(n) \sim g(n) \quad \quad \Longleftrightarrow \quad \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 1


This a priori more complicated definition simply allows us to see that
for large values of :math:`n`, :math:`f(n)` and :math:`g(n)` behave the same way:
the intuition is therefore somewhat the same as for :math:`\mathcal{O}`. Besides, we also have:

.. math::

    f(n) \sim g(n) \quad \quad \Longrightarrow \quad f(n) \in \mathcal{O}(g(n))

But the opposite relationship is not true. Indeed, if we take the example of an
algorithm with an execution time :math:`A` which needs to go through a list twice, we have:

.. math::

    A(n) \not\sim n \quad \text{since} \quad  \lim_{n\rightarrow\infty} \frac{A(n)}{n} = 2

This example shows us the main difference between :math:`\mathcal{O}` and :math:`\sim`: tilde keeps the
multiplicative factor.

There is another difference: tilde provides a *reached* bound. For example: according to the definition of :math:`\mathcal{O}`, we have that

* :math:`n \in \mathcal{O}(n)`
* :math:`n \in \mathcal{O}(n^2)`
* :math:`n \in \mathcal{O}(2^n)`

because :math:`n`, :math:`n^2` and :math:`2^n` all eventually become "bigger" than :math:`n`. Now, we have that


* :math:`n \sim n` (of course ...)
* :math:`n \not\sim n^2`
* :math:`n \not\sim 2^n`

because the limit of the latter two functions tends to 0, not 1!

There are other more subtle differences, which we will discuss in exercises.

Best case, worst case, average case
====================================

We too often hear that :math:`\mathcal{O}` is the *worst case* and :math:`\Omega` is the *best case*.
This is **false** in general, depending on how you define your function.

Let's say we're using a Quick Sort algorithm, which we'll see in Part 2 of the course.
If you define :math:`f(n)` as "the number of comparison operations to perform for an array of size n", then you have:

* :math:`f(n) \sim n^2` et :math:`f(n) \in \mathcal{O}(n^2)`
* :math:`f(n) \in \Omega(n\log_2 n)`

If you now define :math:`g(n)` as "the **average** (expectation) number of comparison operations to perform
for an array of size n, **when selecting arrays uniformly**", you get:

* :math:`g(n) \sim n\log_2 n` et :math:`g(n) \in \mathcal{O}(n\log_2 n)`
* :math:`g(n) \in \Omega(n\log_2 n)`
* et donc :math:`g(n) \in \Theta(n\log_2 n)`

By a (slight) abuse of language, we say that the "average case" of Quick Sort is in :math:`\Theta(n\log_2 n)`.
But the general case is not!

Amortized Comlexity
=================================

Another useful type of complexity is that which counts the average complexity for :math:`m` operations.
This complexity is called the *amortized complexity*.
For example, an `ArrayList <https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html>`_
in java is implemented with an array that doubles its size as soon as its capacity is reached.
The doubling of size operation is done in :math:`\mathcal{O}(n)` where :math:`n` is the current size of the array
Inserting :math:`n+1` operations with the *add(E e)* method when the array has a current size of :math:`n`
will cost on average :math:`\mathcal{O}(1)*n+\mathcal{O}(n)/(n+1)=\mathcal{O}(1)`.

Warning: the complexity of the method *add(E e)* in isolation is well :math:`\Omega(1)` and :math:`\mathcal{O}(n)`
where :math:`n` is the number of elements in the ArrayList.

Frequent complexities
===========================

+---------------------------------------+-------------------+-------------------------------------------------------+
| Classe                                | Nom               | Exemple                                               |
+=======================================+===================+=======================================================+
| :math:`\mathcal{O}(1)`                | Constante         | Find min in sorted array                              |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(\log_2{n})`        | Logarithmic       | Binary search                                         |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n)`                | Linear            | Iterate over elements in an array                     |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n\log_2{n})`       | Linearithmic      | Efficient sorting (e.g. merge sort)                   |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n^2)`              | Quadratic         | Inefficient sorting (e.g. insertion sort)             |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n^c)`              | Polynomial        | Magorith of algorithms in this course                 |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(c^n)`              | Exponential       | Knapsack Problem                                      |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n!)`               | Factorial         | Brute force Solving of the TSP (all permutations)     |
+---------------------------------------+-------------------+-------------------------------------------------------+
