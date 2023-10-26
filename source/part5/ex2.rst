.. _part5_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W11.


Exercise 5.2.1
""""""""""""""

In the Huffman coding compression technique, it is useful to
to include in the compressed file a header containing the information necessary to decode of the file. 
In your implementation, the header is probably a serialized version
of the tree (result of a prefix parse) as proposed in the book.
Do you think it would be more or less interesting from a memory point of view to store for each symbol its binary encoding
rather than the serialized tree?

Exercise 5.2.2
""""""""""""""

Can we gain even more compression ratio if we reapply Huffman's compression algorithm
Huffman's compression algorithm on a file already compressed once?
What happens in this case?
Does this open the door to a recursive and optimal compression algorithm?

.. answer::

    Huffman is able to compress better when the number of symbols is not large (less than the whole asci set) and/or when they are large differences in the number of occurences.
    It works well for text input because this is exactly what we have in natural languages.
    After a first compression, you loose this nice property of natural languages because the input does not correspond to a text anymore.
    Also you need to consider the preorder encoding table as an input). Conclusion: no guarentee it will be usefull because it is not a natural language, the counters should be much more uniform and also you need to add again a new encoding table (preorder traversal of the tree).

Exercise 5.2.3
""""""""""""""

What is, approximately, the compression ratio obtained if we apply the Huffman compression algorithm
on a file with a single string consisting of the character 'a' repeated a million times (:math:``approx 2^{20}``), followed by the character ``b`` present only once?

Does the resulting compression ratio vary with the length of the file (for example, if the ``a`` character is repeated two million times)?

What is the minimum number of bits needed to represent this file in compressed form?

Can we use another compression scheme, compressing more than Huffman compression in this particular case?

Can Huffman compression algorithm be used for other input than text files (say for instance a picture)? 
What would the algorithm count in this case?



.. answer::

    Assume the file is encoded in extended ASCI (256 symbols) thus one byte required for each letter.
    The prefix in the encoding is negligible given the size of the text. The compression rate is thus 1/8 (since huffman will need 0 and 1 for encoding 'a' 'b').
    This compression rate would not change whatever the number of 'a' followed buy a 'b'.
    If we know that the form of the file is given by the regular expression :math:`[a*b]`, then only one number is needed for the number of 'a'. Thus one int.

    Yep, another technique could be "character" followed by the number of consecutive occurences". For instance "aaabbbbbbbccaaa" would become "a3b7c2a3".

    Yes, Huffman can count anything with the form of fixed size number of bits (colors for images, etc).



Exercise 5.2.4 (Linked Heap, Inginious)
"""""""""""""""""""""""""""""""""""""""


Imagine a heap implementation of a priority queue using a chained structure to represent the essentially complete binary tree corresponding to the heap.
How many links are needed in each node?
Write the code for the methods *insert*, *delMax*. What is the complexity? Is it useful to give the size *max N* in the constructor?
How do you add a new node in the heap or remove the next node? Can this be done from the current heap size?


Implement the min priority queue using a linked structure for representing the heap: `MinPQLinked <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MinPQLinked>`_


.. answer::

    You need to have access to the parent and the two children for each node => 3 links/node.
    No you don't need a "maxN" value but you need to be able to add a new node on the last layer or remove the last one of the last layer efficiently. This can be done using the current size :math:`n` in :math:`O(log(n))`.
    The hight :math:`h = \lfloor log_2 (n+1) \rfloor`. The node index of the last node on the last layer is :math:`n-(2^h-1)`. You can consider this node index as a binary number. Each bit tells you if you should follow the left/right link from the root down to the leaf you are looking for in the tree (to retrieve where to add or delete the node at the last layer).

Exercise 5.2.5 (Inginious)
"""""""""""""""""""""""""""

Propose a data structure that would support the following operations in logarithmic time: *insert*, *remove maximum*, *remove minimum*;
and the following operations in constant time: *find maximum and minimum*.
For this, we propose to study the following property called min-max heap.
The even levels are: 0 (root), 2, 4, etc.
These even levels are also called the :math:`min` levels.
The odd levels are 1, 3, 5, etc.
Odd levels are also called :math:`max` levels.
For any :math:`x` element in the min-max heap we have the following property:

* If :math:`x` is at a :math:`min` level, all descendants of :math:`x` are greater than :math:`x`.
* If :math:`x` is at a level :math:`max`, all descendants of :math:`x` are lower than :math:`x`.


Questions related to this min-max heap:

* Which is the smallest element of the heap?

  .. answer::

    c'est celui de la racine.

* Which is the largest element of the heap?

  .. answer::

    Le maximum entre les deux éléments du niveau 1

* Draw a min-max heap that contains the following elements: 10,8,71,31,41,46,51,31,21,11,16,13.

  .. answer::

    .. image:: minmaxheap.png

* Describe the insertion operation in a min-max heap? Give the pseudo-code.

  .. answer::

    Attention, il faut aller voir au niveau :math:`i-2` pour voir s'il ne faut pas swapper.




Implement the `MinMax Heap <https://inginious.info.ucl.ac.be/course/LINFO1121/sorting_MinMaxHeap>`_



Exercise 5.2.6
""""""""""""""

Imagine a data structure that supports

1. *insertion* in logarithmic time
2. the *find median* operation in constant time
3. *deleting the median* in logarithmic time.

.. answer::

    Il faut utiliser deux heap, chacune contenant la moitié des éléments.
    La première heap est une max-heap et contient les :math:`n/2` plus petits éléments.
    La deuxième heap est une min-heap et contient les :math:`n/2` plus grands éléments.
    Assez facile de maintenir cette propriété lors de l'insertion d'un élément et le retrait de la médiane.
