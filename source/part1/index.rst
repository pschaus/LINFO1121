.. _part1:


*************************************************************************************************
Partie 1 | Types abstraits de données, Complexité, Collections Java; Piles, files et listes liées
*************************************************************************************************

Objectifs
=========

A l'issue de cette partie chaque étudiant sera capable de:

* faire la disctinction entre les notations :math:`\mathcal{\sim}`, :math:`\mathcal{O}`,
  :math:`\mathcal{\Theta}`, et :math:`\mathcal{\Omega}`, connaitre leurs propriétés et définitions;
* décrire avec précision les propriétés des types abstraits *pile* et *file*;
  ainsi que les divers types de listes chainées;
* faire la distinction entre un *type abstrait de données* et son implémentation;
* mettre en oeuvre et évaluer une implémentation d'une pile par une *liste simplement ou doublement chaînée*;
* utiliser des *tests unitaires* (avec JUnit) pour tester et prouver le bon fonctionnement d'un programme;
* utiliser les diverses collections présentes de base dans la language Java, en s'aidant de la documentation.

A lire
=======================================

Livre de référence:

* Chapitre 1, section 1: quelques rappels de Java et la programmation en général
* Chapitre 1, section 2: Abstraction de données
* Chapitre 1, section 3: Piles, files, sacs, listes chainées
* Chapitre 1, section 4: Analyses d'algorithmes

Ainsi que ce document résumant les différentes notations de :ref:`part1complexity`.

Slides (keynote)

* `Introduction <https://www.icloud.com/keynote/0jTHGv9VcBJNqr701X0LiSSeQ#part1-intro>`_ 
* `Séance Intermédiaire <https://www.icloud.com/keynote/037KCYIeXbULVFGRo7xLiY8fA#part1-exercices>`_ 
* `Restructuration <https://www.icloud.com/keynote/0C9qyvWomr8eHMmHUELTMbC7A#part1-bilan>`_ 



Exercices théoriques: première partie
=======================================

.. note::
   Vous devez faire ces exercices pour le mercredi de S2.

Exercice 1.1.1
""""""""""""""

Définissez ce qu'est un type abstrait de données (TAD [#adt]_). En java, est-il préférable de décrire un TAD par une
classe ou une interface ? Pourquoi ?

Exercice 1.1.2
""""""""""""""

Comment faire pour implémenter une *pile* par une liste simplement chaînée où les opérations
`push` et `pop` se font en **fin de liste** ? Cette solution est-elle efficace ? Argumentez.

Exercice 1.1.3
""""""""""""""

Quelles sont les implémentations possibles pour une pile? En consultant la documentation sur l'API de Java, décrivez
l'implémentation d'une pile par la classe `java.util.Stack`. Aller voir le code source de l'implémentation
`java.util.Stack` (crtl+B depuis IntelliJ).

Pourquoi pensez-vous que les développeurs de Java ont choisi cette implémentation
(hint: argumentez au niveau de la mémoire et du garbage collector)?

Exercice 1.1.4
""""""""""""""

Comment faire pour implémenter le type abstrait de données *Pile* à l'aide de deux *files* ?
Décrivez en particulier le fonctionnement des méthodes `push` et `pop` dans ce cas.

A titre d'exemple, précisez l'état de chacune des deux files après avoir empilé les entiers `1 2 3` à partir d'une pile
initialement vide. Décrivez ce qu'il se passe ensuite lorsque l'on effectue l'opération `pop`.

Quelle est la complexité temporelle de ces méthodes si l'on suppose que chaque opération `enqueue` et `dequeue`
s'exécute en temps constant?

Cette implémentation d'une pile est-elle efficace (pour :math:`n` opérations)
par rapport aux autres implémentations présentées dans le livre de référence ?

Exercice 1.1.5
""""""""""""""

* Qu'est-ce qu'un iterateur en Java (`java.util.Iterator`)?
* Pourquoi est-ce utile de définir une méthode `iterator()` sur les structures de données?
* Que pensez vous de permettre la modification d'une structure de donnée alors qu'on est en train d'itérer sur celle-ci?

Pour vous aider dans la réflexion, nous vous invitons à lire la spécification de l'API Java concernant la méthode
`remove()`.

Proposez une modification du code de l'iterateur de Stack qui lance une `java.util.ConcurrentModificationException`
si le client modifie la collection avec un `push()` ou `pop()` durant l'itération. Est-ce une bonne idée de laisser
l'implémentation de la méthode `remove()` vide si on ne désire pas permettre cette fonctionnalité?

Exercice 1.1.6
"""""""""""""""

La notation :math:`\sim` (tilde) est utilisée dans le livre de référence pour l'analyse des temps de calcul des
algorithmes. En quoi cette notation diffère ou ressemble aux notations plus classiquement utilisées :math:`\mathcal{O}`
(big Oh), :math:`\mathcal{\Omega}` (big Omega) et :math:`\mathcal{\Theta}` (big Theta)?

Expliquez précisément les liens et similitudes entre celles-ci.
Que voyez-vous comme avantage à utiliser la notation :math:`\sim` (tilde) plutôt que :math:`\mathcal{O}`
lorsque c'est possible?

Exercice 1.1.7
""""""""""""""

Expliquez comment nous pouvons extraire la caractérisation :math:`\sim` (tilde) de l'implémentation d'un algorithme à
l'aide du test *Doubling ratio*.

* Comment fonctionne ce test?
* Quelles sont les limites et avantages de ce test?

Supposont que nous mesurons les temps d'exécutions :math:`T(n)` suivants (en secondes) d'un programme en fonction de la
taille de l'entrée :math:`n`:

============  ==== ==== ==== ==== ===== ===== =====
:math:`n`     1000 2000 4000 8000 16000 32000 64000
:math:`T(n)`  0    0    0.1  0.3  1.3   5.1   20.5
============  ==== ==== ==== ==== ===== ===== =====

* Comment pouvez-vous caractériser au mieux l'ordre de croissance de cette fonction ?
* Que serait le temps d'exécution pour 128000?

Exercices théoriques supplémentaires
====================================

.. note::
    Ces exercices ne seront pas forcéments résolus en cours, ils restent néanmoins intéressants.
    Si vous avez des problèmes avec ceux-ci, posez votre question lors d'un TP.

Exercice 1.1b.1
"""""""""""""""

Que signifient les paramètres -Xmx, -Xms que l'on peut passer à la JVM pour l'exécution d'un bytecode?
Est-ce que ces paramètres peuvent influencer la vitesse d'exécution d'un programme Java? Pourquoi?

Exercice 1.1b.2
"""""""""""""""

* Qu'est-ce qu'un bon ensemble de tests unitaires pour vérifier l'exactitude d'une structure de données?
* Pensez-vous aux cas limites?
* Pensez-vous à la valeur maximale des entiers, doubles, etc?
* En quoi la génération de données aléatoire peut être utile pour tester les structures de données?
* Pourquoi est-ce important de travailler avec une semence (seed) fixée?
* En quoi un outil d'analyse de couverture de code peut être utile (tel que `Jacoco <http://eclemma.org/jacoco/>`_)
  pour vous aidez à concevoir des tests.
* Comment vérifier expérimentalement que l'implémentation d'une structure de données ou un algorithme a
  bien la complexité temporelle théorique attendue ?

Exercices sur Inginious
==========================================

.. note::
   Vous devez faire ces exercices pour le mercredi de S3.

1. `Ecriture de tests unitaires pour une stack <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/m1stacktests>`_
2. `Implementation d'une stack avec structure chainée <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/m1stack>`_ 
3. `Implementation d'une liste chainée circulaire et d'un iterateur <https://inginious.info.ucl.ac.be/course/LSINF1121-2016/Part1CircularLinkedList>`_

Exercices théorique: deuxième partie
=======================================

.. note::
   Vous devez faire ces exercices pour le mercredi de S3.

Exercice 1.2.1
""""""""""""""

Dans votre implémentation d'une liste chainée circulaire ci-dessous.
Quelle est la complexité de la méthode


* `public void enqueue(Item item)`?
* `public Item remove(int index)` ?
* d'une séquence d'operations qui consiste à *créer un iterateur et ensuite itérer sur les k-premiers elements* ?

.. code-block:: java


   import java.util.ConcurrentModificationException;
   import java.util.Iterator;
   import java.util.NoSuchElementException;

   public class CircularLinkedList<Item> implements Iterable<Item> {
    private long nOp = 0; // count the number of operations
    private int n;          // size of the stack
    private Node  last;   // trailer of the list

    // helper linked list class
    private class Node {
        private Item item;
        private Node next;
    }

    public CircularLinkedList() {
        last = new Node(); // dummy node
        last.next = last;
        n = 1;
    }

    public boolean isEmpty() { return n == 1; }

    public int size() { return n-1; }

    private long nOp() { return nOp; }

    /**
     * Append an item at the end of the list
     * @param item the item to append
     */
    public void enqueue(Item item) {
        // TODO STUDENT: Implement add method
    }

    /**
     * Removes the element at the specified position in this list.
     * Shifts any subsequent elements to the left (subtracts one from their indices).
     * Returns the element that was removed from the list.
     */
    public Item remove(int index) {
        // TODO STUDENT: Implement remove method
    }

    /**
     * Returns an iterator that iterates through the items in FIFO order.
     * @return an iterator that iterates through the items in FIFO order.
     */
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    /**
     * Implementation of an iterator that iterates through the items in FIFO order.
     *
     */
    private class ListIterator implements Iterator<Item> {
        // TODO STUDENT: Implement the ListIterator
    }

   }

Exercice 1.2.2
""""""""""""""
La notation post-fixe (ou `polonaise inverse <https://fr.wikipedia.org/wiki/Notation_polonaise_inverse>`_) est utilisée
pour représenter des expressions algébriques.
Nous ne considérons pour simplifier que des expressions post-fixes avec des entiers positifs
et les opérateurs `+` et `*`. Par exemple `2 3 1 * + 9 *` dont le résultat vaut 45
et le résultat de `4 20 + 3 5 1 * * +` est 39.

1. Ecrivez un algorithme en Java pour évaluer une expression post-fixe au départ d'une chaine de n-caractères.
2. Quelle structure de donnée utilisez vous ?
3. Quelle est la complexité de votre algorithme (temporelle et spatiale) ?

Pour rappel, voici comment on peut itérer sur les elements d'une chaine qui sont séparés par des espaces.

.. code-block:: java


    String in = "4 20 + 3 5 1 * * +";
    StringTokenizer tokenizer = new StringTokenizer(in);
    while (tokenizer.hasMoreTokens()) {
         String element = tokenizer.nextToken();
    }


Exercice 1.2.3
""""""""""""""

La `programmation fonctionnelle <https://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_ est un paradigme de programmation de plus en plus important.
Dans ce paradigme de programmation, les structures de données sont `immutables <https://en.wikipedia.org/wiki/Purely_functional_data_structure>`_ .
Nous nous intéressons ici à l'implémentation d'une liste immutable appelée *FList* permettant d'être utilisée dans un cadre fonctionnel.
Voici l'API d'une *FList*

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


Comme vous pouvez vous en rendre compte, aucune des méthodes ne permet de modifier l'état de la liste.
Voici un exemple de manipulation d'une telle liste.
Si vous n'êtes pas familiers avec les `interfaces fonctionnelles <https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html>`_  de Java8, 
nous vous demandons de vous familiariser d'abord avec celles-ci.



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


Voici une implémentation partielle de la `FList`


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


Nous vous demandons de 


* compléter cette implémentation, si possible utilisez autant que possible des méthodes récursives.
* déterminer la complexité de chacune des méthodes.


Ressources supplémentaires
==========================

.. toctree::
   :maxdepth: 1

   complexity

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. rubric:: Notes de bas de page

.. [#adt] *abstract data type* (ADT) en anglais

..
    Vieille questions

    - Comment faire en Java pour lire des données textuelles depuis un fichier et pour écrire des résultats
    dans un fichier ASCII ?
    Écrivez en Java une méthode générique*, c'est-à-dire aussi indépendante que possible de son utilisation
    dans un contexte particulier, de lecture depuis un fichier texte.  Faites de même pour l'écriture dans un fichier ASCII.

    - Comment faire en Java pour passer des arguments à un programme ? Soyez précis. Donnez un exemple

    Code example

    .. code-block:: java

        b = true , x = 4, c = 5
        b = false, x = 4, c = 2


    Link example `IsLessOrEqualTest.java <https://bitbucket.org/minicp/minicp/src/HEAD/src/test/java/minicp/engine/constraints/IsEqualTest.java?at=master>`_

    Image example

    .. image:: dfs.svg
        :scale: 50
        :width: 250
        :alt: DFS