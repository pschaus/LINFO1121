.. _part4_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W7.



Exercise 4.1.1
""""""""""""""

Name at least four different implementations of a symbol table (dictionary).
Specify the main properties of each implementation.
In which scenario(s) are they most appropriate?
What are the time complexities of their main operations?

.. answer::

   Il *FAUT* insister sur l'existence dictionnaires qui ne sont pas tables de hachage.

   .. list-table:: Résumé des différentes implémentations
      :header-rows: 1

      * - Nom
        - Implémentation en dictionnaire
        - en ensemble
        - Insertion
        - Recherche
        - Suppression
        - Commentaire
      * - Double tableau, non trié
        -
        -
        - :math:`\mathcal{O}(1)` amorti
        - :math:`\mathcal{O}(n)`
        - :math:`\mathcal{O}(n)` (:math:`\mathcal{O}(1)` avec des listes)
        -
      * - Double tableau, trié
        -
        -
        - :math:`\mathcal{O}(n)` amorti
        - :math:`\mathcal{O}(\log n)`
        - :math:`\mathcal{O}(n)` (:math:`\mathcal{O}(1)` avec des listes)
        - nécessite un comparateur
      * - Hash tables
        - ``HashMap``
        - ``HashSet``
        - :math:`\mathcal{O}(1)` amorti
        - :math:`\mathcal{O}(1)` amorti
        - :math:`\mathcal{O}(1)` amorti
        - nécessite un hash
      * - Arbres de recherche
        - ``TreeMap``
        - ``TreeSet``
        - :math:`\mathcal{O}(\log n)`
        - :math:`\mathcal{O}(\log n)`
        - :math:`\mathcal{O}(\log n)`
        - nécessite un comparateur
      * - Linked Hash tables
        - ``LinkedHashMap``
        - ``LinkedHashSet``
        - :math:`\mathcal{O}(1)` amorti
        - :math:`\mathcal{O}(1)` amorti
        - :math:`\mathcal{O}(1)` amorti
        - ordre d'itération = ordre insertion


Exercise 4.1.2
""""""""""""""

Recall the following question from the sorting assignment: Given a set :math:`S` of size :math:`n` and a number :math:`x`, describe an efficient algorithm using a hash table to determine whether there exists a pair :math:`(a, b)` with :math:`a \in S, b \in S` such that :math:`a + b = x`. What is the time complexity of your algorithm? Is it better than your solution that used sorting?

.. answer::

   Une table de hachage étant en :math:`\mathcal{O}(1)` amorti en insertion/recherche (sous réserve d'un hachage correct)
   on peut simplement insérer tout les nombres dans la table, puis regarder pour chaque nombre :math:`i` si :math:`x-i`
   est présent dans l'ensemble. Complexité totale: :math:`\mathcal{O}(n)`.

Exercise 4.1.3
""""""""""""""

Show that :math:`(a + b) \% M` is equivalent to :math:`((a \% M) + b) \% M`. How can this property be useful when building a hash function for strings?
Explain how Java computes a hash function for strings.
What is the time complexity of computing the hash code of a string once, and computing it :math:`N` times?

.. answer::

   Le modulo est distributif, et l'appliquer deux fois est identique à l'appliquer une fois:

   .. math::

      ((a \% M) + b) \% M = (a \% M) \% M + b \% M = a \% M + b \% M

   Pour un string :math:`s_0,s_1,\ldots,s_n` java utilise la formule :math:`\sum_{i=0}^{n-1} 31^{n-i-1}s_i`.
   Mais l'implémentation utilise une boucle for (Horner method) similaire à celle de la page 460. La complexity est
   donc de :math:`\sim n`. Mais attention, Java met en cache le hashcode, il est donc calculé au plus 1 fois. La complexity
   pour :math:`N` appel à ``hashCode`` est donc :math:`n+N`.

Exercise 4.1.4
""""""""""""""

Explain why the ``hash()`` method on page 461 of the book returns ``(x.hashCode() & 0x7FFFFFFF) % M`` and not simply ``x.hashCode() % M``?
What number does ``0x7FFFFFFF`` represent?
What is its binary representation?
Show the effect at the bit level on an example where ``x.hashCode()`` returns a negative number. Hint: use ``Integer.toBinaryString(int)`` to verify your answer.

.. answer::

   0x7FFFFFFF est une représentation hexadecimale (car il commence par 0x). Un caractère hexa spécifie 4 bits. 0x7F FF FF FF spécifie donc la valeur de 32 bits.
   7=0111,F=1111. Donc  0x7FFFFFFF est le nombre binaire `0(suivi de 31 x 1)`. C'est l'entier maximum en Java, c'est à dire :math:`2^{31}-1=2147483647`.
   Rien ne garanti que la méthode hashCode retourne un entier positif. Or tout entier négatif a une representation binaire qui commence par \texttt{1 (suivi de 31 x (0 ou 1))}.
   Appliquer un :math:`\&` logique va donc mettre ce premier bit toujours à 0 afin d'éviter de calculer un index négatif qui résulterait en un OutOfBoundException dans un tableau.

   Question bonus: est-ce que `x \& 0x7FFFFFFF = abs(x)`? Non car on utilise une notation en complément de deux. Une bonne raison d'être attentif au cours de systèmes informatiques...

Exercise 4.1.5
""""""""""""""

Java provides the class ``java.util.Hashtable`` as an implementation of the ``java.util.Map`` interface.
Which variant of hash table does it use?
Does Java provide other implementations of the ``Map`` interface?
Draw a diagram representing the interfaces and classes related to ``Map`` and specify the key characteristics of each.
What can be used as a key for a hash table in Java? Be specific.

.. answer::

   Java utilise du separate-chaining. Sa structure pour le chaining est une liste doublement chaînée. Un object Entry est un noeud de la liste qui à une référence vers le predecesseur et le successeur.
   Différence entre HashMap et HashTable: HashMap accepte les clefs et valeurs nulles et celle-ci n'est pas synchronisée.
   Ensuite il y a aussi les SortedMap dont la TreeMap qui implémente les red-black tree et *ajoute des fonctionnalité relative à l'ordre (firstKey, ceil, floor, etc)*.

Exercise 4.1.6
""""""""""""""

What is meant by a "collision" in a hash table?
Do collisions affect the time complexity of operations?
If so, which operation(s) and with what complexity? If not, explain why.

.. answer::

   Une collision entre deux entrées veut dire qu'elle ont le même hash (après modulo). Clairement, cela force à utiliser une technique pour gérer ces cas.
   Il faut profiter de cette question pour demander aux étudiants quels sont les méthodes usuelles dans des hash tables pour gérer cela.
   Assurez-vous que tout le monde à bien compris le separate chaining et le linear probing (notamment la recherche et la suppression...)

Exercise 4.1.7
""""""""""""""

What is the load factor of a hash table?
Is controlling the load factor necessary or optional for the proper operation of a hash table using linear probing or separate chaining?
What strategy is used by ``java.util.Hashtable`` to control the load factor?
How does it differ from the strategy used in ``LinearProbingHashST``?
What is the relationship between the load factor and collisions?

.. answer::

   Il y a une valeur threshold = taille du tableau x facteur de charge limite.
   Le facteur de charge limite est par défaut de 0.75 mais le constructeur permet de le changer.
   Dès que le nombre d'element atteint cette limite threshold, on rehashe tout dans un nouveau tableau dont la capacité est multipliée par deux plus 1 (pourquoi?).

Exercise 4.1.8
""""""""""""""

Imagine a new ``iterator()`` method that returns an iterator over the keys of ``LinearProbingHashST``.
Your iterator must not allow modifications to the hash table while in use: a ``ConcurrentModificationException`` should be thrown if a modification occurs.
How would you implement this? Hint: Take inspiration from the ``java.util.Hashtable`` strategy.


Exercise 4.1.9
""""""""""""""

Describe the implementation of the ``put(key)`` method in a hash table using linear probing where deleted entries are marked with a special sentinel value (tombstone) via the ``delete(key)`` method.
In other words, instead of rehashing and shifting subsequent entries so that it is as if the deleted entry was never inserted, ``delete(key)`` simply flags the entry with this special marker.
What are the advantages and disadvantages of this approach compared to the ``LinearProbingHashST`` implementation in the book?

.. answer::

   L'inconvénient est que le get risque de prendre beaucoup plus de temps.
   si on fait un get et que la clef n'est pas là, on ne peut plus s'arrêter après le premier trou, il faudra a chaque fois tout parcourir.
   Le meilleur temps dans le cas où la clef n'est pas présente prendra donc :math:`\Theta(N)` au lieu de :math:`\mathcal{O}(1)`.
   Par contre le delete est plus rapide puisqu'il ne faut pas décaler vers la gauche les clefs.
   Il y d'autres problèmes que les étudiants pourraient soulever...

Exercise 4.1.10 (Rabin-Karp)
""""""""""""""""""""""""""""

Imagine a hash function for a string :math:`s` such that knowing its value for the substring :math:`s[i \ldots i+n-1]` allows computing the hash value of the substring :math:`s[i+1 \ldots i+n]` in constant time (incrementally).

.. answer::

   C'est l'idée de Rabin-Karp p 775 du livre. Soit :math:`x_i` le hash sur :math:`s[i,...,i+n-1]` alors :math:`x_{i+1}= (x_i-t_iR^{n-1})R+t_{i+n}`.

Exercise 4.1.11 (Rabin-Karp)
""""""""""""""""""""""""""""

Explain how to search for a substring of length :math:`m` in a text of length :math:`n` in :math:`\mathcal{O}(n)` time using an incremental hash function.
How would you do this if you had :math:`k` patterns of length :math:`m` to search for in a text of length :math:`n`?
What is the time complexity of your method? Is it better than running the Rabin-Karp algorithm :math:`k` times?

.. answer::

   Pour la première partie c'est Rabin-Karp, classique.
   Pour la deuxième question, le cout de hashage sera :math:`\mathcal{O}(km)` car il y a :math:`km` clef a mettre dans la table de hashage.
   Ensuite c'est :math:`\mathcal{O}(k)` pour tester les :math:`k` string.
   On peut imaginer de nombreuses optimisations.
   Imaginons qu'on cherche deux mots de longueur 5 et 10.
   On fait le RK classique pour la longueur 5. Ensuite si on trouve un match, on peut chercher à l'étendre pour matcher les 10 symboles.
   On peut aussi chercher les matchs du suffixe de longeur 5. Ensuite faire une double boucle pour voir si les matchs matches entre eux ;-)


Exercise 4.1.12 (INGInious: MCQ)
""""""""""""""""""""""""""""""""

`Multiple choice questions on hash function <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part4QcmHashing>`_


Exercise 4.1.13 (INGInious: MCQ)
""""""""""""""""""""""""""""""""

`Multiple choice questions on Rabin-Karp <https://inginious.info.ucl.ac.be/course/LINFO1121-QCM/Part4QcmRk>`_

Exercise 4.1.14 (INGInious)
"""""""""""""""""""""""""""

An easy tool to implement for counting word occurrences (exam 2022). 
Word counting is a frequent task in natural language processing algorithms.
`Word Counter <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_WordCounter>`_


Exercise 4.1.15 (INGInious)
"""""""""""""""""""""""""""

Incremental computation of a hash function (exam 2018).
`Incremental Hash <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_IncrementalHash>`_


Exercise 4.1.16 (INGInious)
"""""""""""""""""""""""""""

A bounded-capacity cache that retains only the most recently used entries (exam 2022).
`LRUCache <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_LRUCache>`_


Exercise 4.1.17 (INGInious)
"""""""""""""""""""""""""""

Implement a version of Rabin-Karp to search for `K patterns <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_RabinKarp>`_ simultaneously instead of just one.



