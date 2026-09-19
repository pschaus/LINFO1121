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

A function :math:`f(n)` is said to belong to :math:`\mathcal{O}(g(n))` if there is a constant :math:`k`
such that :math:`k \cdot g(n)` is systematically greater than or equal to :math:`f(n)` for all :math:`n` large enough
(that is, there is an :math:`n_0` from which the rule is satisfied).

:math:`g(n)` therefore acts as an upper bound on the function up to a constant factor.

Example
-------

Let :math:`f(n) = 2n^2+3n`. We have that :math:`f(n)\in \mathcal{O}(n^2)` (in other words, we choose :math:`g(n)=n^2`).
Indeed, with :math:`k=3`, the rule is respected for all :math:`n \geq 3`.

Similarly, the same function :math:`f(n) = 2n^2+3n` belongs to other sets:


* :math:`f(n) \in \mathcal{O}(n^3)`
* :math:`f(n) \in \mathcal{O}(n^4)`
* ...
* :math:`f(n) \in \mathcal{O}(2^n)`
* ...

because all these functions grow at least as fast as :math:`n^2` when :math:`n` is large.

In the majority of cases, we want to choose the smallest possible :math:`g(n)` function that satisfies the
property, since it gives us the most information.

Notation Big-Omega (:math:`\Omega`)
=============================================

The definition is similar to that of Big-Oh. The differences are shown in bold:

.. math::

    f(n) \in \mathbf{\Omega}(g(n)) \quad \Longleftrightarrow \quad
        \exists k \in \mathbb{R^+}, n_0 \in \mathbb{N} \quad \text{ s.t. } \quad
        \mathbf{k \cdot f(n) \geq g(n)} \quad
        \forall n \geq n_0

For large values of :math:`n`, :math:`f(n)` is always greater than :math:`g(n)` up to a constant
factor. Concretely, this means that the function :math:`g(n)` places a lower
bound on the complexity of :math:`f(n)`. In other words, :math:`g(n)` characterizes the
"best case" possible for the calculation of :math:`f(n)` (this is an abuse of language: see below).

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
-----

It is not always possible to find a function :math:`g(n)` such that :math:`f(n) \in \Theta(g(n))` for an arbitrary function :math:`f(n)`.
For example, for insertion sort, since its worst case is in :math:`\mathcal{O}(n^2)` while its best case is in :math:`\Omega(n)`, and both bounds are tight,
it is not possible to say that insertion sort is in :math:`\Theta(g(n))` in general.

Example
-------

Merge sort is in :math:`\Theta(n\log_2 n)`.

Notation Tilde (:math:`\mathcal{\sim}`)
=======================================

The definition of tilde notation is based on different principles:

.. math::

    f(n) \sim g(n) \quad \quad \Longleftrightarrow \quad \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 1


This seemingly more complicated definition simply allows us to see that
for large values of :math:`n`, :math:`f(n)` and :math:`g(n)` behave the same way:
the intuition is therefore somewhat the same as for :math:`\mathcal{O}`. Besides, we also have:

.. math::

    f(n) \sim g(n) \quad \quad \Longrightarrow \quad f(n) \in \mathcal{O}(g(n))

But the converse is not true. Indeed, if we take the example of an
algorithm with an execution time :math:`A` which needs to go through a list twice, we have:

.. math::

    A(n) \not\sim n \quad \text{since} \quad  \lim_{n\rightarrow\infty} \frac{A(n)}{n} = 2

This example shows us the main difference between :math:`\mathcal{O}` and :math:`\sim`: tilde keeps the
multiplicative factor.

There is another difference: tilde provides a *tight* (achieved) bound. For example, according to the definition of :math:`\mathcal{O}`, we have:

* :math:`n \in \mathcal{O}(n)`
* :math:`n \in \mathcal{O}(n^2)`
* :math:`n \in \mathcal{O}(2^n)`

because :math:`n`, :math:`n^2`, and :math:`2^n` all eventually upper-bound :math:`n`. However, we have:

* :math:`n \sim n` (of course)
* :math:`n \not\sim n^2`
* :math:`n \not\sim 2^n`

because the limit of the ratio for the latter two functions tends to 0, not 1!

There are other more subtle differences, which we will discuss in the exercises.

Best case, worst case, average case
====================================

We too often hear that :math:`\mathcal{O}` is the *worst case* and :math:`\Omega` is the *best case*.
This is **false** in general, depending on how you define your function.

Let's say we are analyzing the QuickSort algorithm, which we will see in Part 2 of the course.
If you define :math:`f(n)` as "the number of comparison operations performed on an array of size :math:`n`", then you have:

* :math:`f(n) \sim n^2` and :math:`f(n) \in \mathcal{O}(n^2)`
* :math:`f(n) \in \Omega(n\log_2 n)`

If you now define :math:`g(n)` as "the **expected** number of comparison operations performed
on an array of size :math:`n`, **assuming arrays are selected uniformly at random**", you get:

* :math:`g(n) \sim n\log_2 n` and :math:`g(n) \in \mathcal{O}(n\log_2 n)`
* :math:`g(n) \in \Omega(n\log_2 n)`
* and therefore :math:`g(n) \in \Theta(n\log_2 n)`

By a (slight) abuse of language, we say that the "average case" of QuickSort is in :math:`\Theta(n\log_2 n)`.
However, the general case is not!

Amortized Complexity
====================

Another useful measure of complexity is that which counts the average cost per operation over a sequence of :math:`m` operations.
This is called *amortized complexity*.
For example, an `ArrayList <https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html>`_
in Java is implemented with an array that doubles its capacity as soon as it is full.
The resizing operation takes :math:`\mathcal{O}(n)` where :math:`n` is the current size of the array.
Performing :math:`n+1` operations with the *add(E e)* method starting from an empty array
will cost on average :math:`(\mathcal{O}(1)\cdot n + \mathcal{O}(n))/(n+1) = \mathcal{O}(1)`.

Warning: the worst-case complexity of an individual call to *add(E e)* is indeed :math:`\mathcal{O}(n)`, while its best case is :math:`\Omega(1)`.

Frequent complexities
=====================

+---------------------------------------+-------------------+-------------------------------------------------------+
| Class                                 | Name              | Example                                               |
+=======================================+===================+=======================================================+
| :math:`\mathcal{O}(1)`                | Constant          | Find min in sorted array                              |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(\log_2{n})`        | Logarithmic       | Binary search                                         |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n)`                | Linear            | Iterate over elements in an array                     |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n\log_2{n})`       | Linearithmic      | Efficient sorting (e.g. merge sort)                   |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n^2)`              | Quadratic         | Inefficient sorting (e.g. insertion sort)             |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n^c)`              | Polynomial        | Majority of algorithms in this course                 |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(c^n)`              | Exponential       | Knapsack Problem                                      |
+---------------------------------------+-------------------+-------------------------------------------------------+
| :math:`\mathcal{O}(n!)`               | Factorial         | Brute-force solving of the TSP (all permutations)     |
+---------------------------------------+-------------------+-------------------------------------------------------+
