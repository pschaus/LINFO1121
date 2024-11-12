.. _part4_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W8.


Exercise 4.2.1 (Hash of Long and Double)
"""""""""""""""""""""""""""""""""""""""""""""

Here is the formula used by Java to calculate a hash function
on doubles (bits is a 64 bit array represented as a long):


.. code-block:: java

    return (int) bits ^ (bits >>> 32);



* Why not just use ``(int) bits`` (casting from long to int)? Hint: The reference book suggests that a good hash function should use all bits for its calculation. Why?
* A double in Java is represented in 64 bits as :math:`(-1)^s \times m \times 2^{(e - 1023)}`. The first bit :math:`s` is the sign, the next 11 bits represent the exponent in binary form and the last 52 bits represent the mantissa (decimal part) in binary form.  Do a positive decimal number and its opposite get different hash functions?

.. answer::

   Oui un décimal positif et son opposé n'obtiennent pas les mêmes fonction de hachage. Exemple hashCode(6.0)=1075314688, alors que hashCode(-6L)=-1072168960. Vous pouvez leur dire de tester directement dans Java :-)
   On pourrait penser que le xor suivi du casting ne prenne pas en compte les 32 premiers bits (dont le bit de poids fort).
   Mais grâce (bits ``>>>`` 32), tous les bits auront bien un impact sur la fonction de hachage. Propritété évidemment souhaitable pour éviter les collisions et obtenir une mapping le plus réparti possible sur les int. (il faut que deux double/long "adjacent" (+1, -1, *2, ...) soient "éloignés" les un des autres quand ils sont hashés).

Exercise 4.2.2 (Hash and casting of integers)
"""""""""""""""""""""""""""""""""""""""""""""""


* Is the hash function of a 32-bit integer the same as the hash function of the same integer that would be double-cast?

  .. answer::

   Pour le double c'est faux. ((double)5) est représenté comme :math:`(-1)^0\cdot 1.25 \cdot 2^2` c'est à dire:
   0-10000000001-0100000000000000000000000000000000000000000000000000.
   Ce nombre de 64 bit est sans grand rapport avec :math:`0^{61}101`, or la formule est la même. Le hashcode sera donc différent.

* Is the hash function of a 32-bit integer the same as the hash function of the same integer that would be cast as a long?  Hint: `Long.toBinaryString( Double.doubleToRawLongBits(a))` displays the array of bits used to represent a double.

  .. answer::

   On distingue 2 cas:

   * *cas 1* Si l'entier est positif : **c'est vrai**.
     Le hash d'un entier sur 32 bits est l'entier lui-même.
     Si on caste par exemple l'entier 5 en Long on obtient en représentation binaire :math:`(61x0)101` (il y a juste 32 zeros mis devant).
     La formule de hash sur un long est la même sur sur les doubles. (bits ``>>>`` 32) va donner un masque de 32x0. Le xor va donc laisser l'entier initial intact.
   * *cas.2* si l'entier est négatif: **c'est faux** car pour l'entier  de 32 bits casté en Long aura une représentation différente.
     :math:`5 = (61\times 0)101`, :math:`-5 = (61\times 1) 011 ` en utilisant le complément à 2 de :math:`5`.

Exercise 4.2.3 (Hash of String: the choice of M and R constants)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


The hash function for a given string as presented in the book p460 is as follows:

.. code-block:: java

    int hash = 0;
    for (int i = 0; i < s.length(); i++)
        hash = (R * hash + s.charAt(i)) % M;


In the book's implementation, :math:`M` (the size of the hash table) is a power of two.
The suggested value for :math:`R` is *a small prime such that 31 so that the bits of all characters play a role.*

* Suppose that :math:`R` is a multiple of :math:`M`. What would happen in the calculation?

  .. answer::

   Supposons par exemple :math:`R=kM` pour un entier :math:`k>0`, on a donc comme indice calculé dans le tableau pour le string :math:`s`:

   .. math::

      \left ( \sum_{i=0}^{n-1} (kM)^{n-i-1}s_i \right ) \% M = \sum_{i=0}^{n-1} \left ((kM)^{n-i-1} s_i \right ) \% M = s_{n-1} \% M.

   C'est vraiment très triste car on voit bien que seul le dernier caractère est pris en compte pour calculer la fonction de hachage. Il faut donc faire très attention à l'interaction entre :math:`M` et :math:`R`.

* Suppose that :math:`R` is an even number. What would happen?

  .. answer::

   M s'écrit comme une puissance de deux, disons :math:`2^k`. R est pair, on l'écrit par exemple :math:`2l`. Notre calcul d'indice s'écrit donc comme suit:

   .. math::

      \sum_{i=0}^{n-1} \left ((2l)^{n-i-1} s_i \right ) \% 2^k = s_{n-1} \% M.

   Encore une fois, on voit bien que tous les premiers termes vont donner zero. Plus précisément ceux tels que :math:`n-i-1 \ge k`.

   Donc tous les caractères (et donc tous les bits) ne seront pas pris en compte. Pas bien!

In both cases, how many entries in the string will actually determine the hash code? What are the risks in terms of collision? Can load factor control solve the problem? Explain why using 31 is a good choice for array sizes that are powers of two? Would it also be a good choice for an array size that starts at 31 and is multiplied by two each time it needs to resize?

* In the book implementation, :math:`M` (the size of the hash table) is a power of two, initialized to 16. Suppose that at some point :math:`M` is :math:`2^8=256`. Then two integer keys are added to a hash table implemented with separate chaining: respectively :math:`2560` and :math:`3072` (it is assumed that these additions do not cause any resizing of the table). As you know, the hash code of an integer key (int) is the number itself.
  Will adding these two values cause a collision between them in the table? If so why?

  .. answer::

   Oui car dans les deux cas, le :math:`\%256` donne 0.

  If so can you suggest a third value that will also collide?

  .. answer::

   512

  If there is a collision, can it disappear the next time the table is resized as in the book implementation?


* What do you suggest to avoid this problem? What is the :math:`M` initialization and resizing policy used in ``java.util.HashMap``? Does this solve the problem on our example?

  .. answer::

   Par défaut, le tableau interne dans HashTable est 11. Son redimensionnement garde la taille impaire :math:`(currentSize \times 2+1)`.
   Dans ce cas-ci, on n'a pas de problème. L'avantage de la stratégie de Java est qu'une collision peut disparaître au prochain dimensionnement.
   Alors que pour la stratégie du livre pas nécessairement. En effet, lorsqu'on passe à :math:`M=512`, les deux collisions sont toujours là.

Exercise 4.2.4 (Design of Hash function for Vehicules)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

* What would you suggest as a hash function for identifying vehicles that are strings of numbers and letters of the form: "9X9XX99X9XX999999" where a 9 represents a number and an "X" represents a letter from A to Z.
* Does your hash function have the property that for a hypothetical array size N of :math:`10^{11} \cdot 26^6` there is never a collision?

.. answer::

   Il y a 6 lettres et 11 chiffres.
   Soit :math:`X` la valeur du string des lettres concaténées si on le considère comme un nombre en base 26 (A=0, B=1, ...). La valeur max de ce nombre est :math:`26^6-1`.
   Soit :math:`Y` le nombre obtenu par concaténation des chiffres. La valeur max de ce nombre est :math:`10^{11}-1`.
   Un fonction de hash pour :math:`XY` est :math:`X \cdot 10^{11} + Y`.
   Le maximum de ce nombre est bien :math:`10^{11} \cdot 26^6` et il existe bien une correspondance 1 à 1 (une bijection, donc) entre la fonction de hash et les strings des véhicules.

Exercise 4.2.5 (Design of Hash function: Citizens)
"""""""""""""""""""""""""""""""""""""""""""""""""""

Let's imagine that we want to build a directory of Belgian citizens
and we want to be able to access each citizen by his identity card number
(12 digits).
We can then consider this number as the unique key identifying
each citizen and use this key as an index in an array in Java.
To each index would correspond a reference to an instance of the class
class whose fields constitute the information that we want to store for each citizen.
What is the time complexity of the following operations?

* search for the information relative to a citizen from his identity card number.
  identity card number.
* add a new citizen.

Isn't this implementation of a dictionary even better than a hash table?
Can we have a collision problem in this case? Justify.

.. answer::

   Tout est en :math:`\mathcal{O}(1)`. La magie s'interrompt cependant quand on constate que la taille du dictionnaire
   en mémoire (avec des object ``Citoyen`` de taille :math:`x`) est de :math:`10^12\cdot x`. Avec :math:`x` = 1 ko,
   on obtient 1 Peta-octet de données.

   Il y a 11 millions de citoyen à mettre dans le dico. Le facteur de remplissage serait

   .. math::

      \frac{11\cdot 10^6}{10^12} = 11\cdot 10^{-6}

   Ca ne semble pas être une utilisation très raisonnable de l'espace...

Exercise 4.2.6 Rabin-Karp, the return of revenge
""""""""""""""""""""""""""""""""""""""""""""""""""""

Check that you have obtained a solution in :math:`\mathcal{O}(n)`, and not :math:`\mathcal{O}(kn)` (not counting the initial hashing of the keywords to be searched, which is in :math:`\mathcal{O}(km)`), and
not counting the initial hashing of the keywords to be searched which is in :math:`\mathcal{O}(km)`),
for last week's Exercise 4.1.11.

.. answer::

    La partie :math:`\mathcal{O}(km)` vient du hashing initial des :math:`k` mots-clés de taille :math:`m`, on
    ne peut pas y couper.

    Contrairement, en mettant dans une table de hachage (HashMap ici) les [hash -> mots-clés], on sait savoir en
    O(1) si le hash d'un des mots-clés matche, plutôt que d'aller comparer les hash en :math:`\mathcal{O}(k)`.

    On a donc pour chaque lettre du string principal (de taille :math:`n`) une opération d'update de hash en :math:`\mathcal{O}(1)`
    (update incrémental du hash) suivi d'un check de présence du hash dans la table de hashage en :math:`\mathcal{O}(1)`,
    suivi eventuellement d'un check de collision en :math:`\mathcal{O}(m)` qui peut être négligé.

    On est donc bien en :math:`\mathcal{O}(n)` si on considère qu'il n'y a pas trop de collisions, la même complexité
    qu'avec un seul mot-clé! Magique, non?


Exercise 4.2.7 (Inginious: Linear Probing)
""""""""""""""""""""""""""""""""""""""""""""

Implement a `Linear Probing Hashtable <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_LinearProbingHashST>`_


Exercise 4.2.8 (Inginious: Tries and Autocompletion)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Implement an efficient auto-completionalgorithm using a trie data structure: `AutoCompletor <https://inginious.info.ucl.ac.be/course/LINFO1121/strings_AutoCompleter>`_



Exercise 4.2.9 (Inginious: An funny exercise using HashTables)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This is the question 21 of the `advent of code 2022 <https://adventofcode.com>`_.
It can be efficently solved using a hashtables in combination with a linked tree data-structure.
 `Monkeys <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_Monkeys>`_




