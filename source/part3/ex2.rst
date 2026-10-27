.. _part3_ex2:

Exercises B
=======================================

.. note::
    You must complete these exercises by Wednesday of W7.


True/False: Binary Search, BSTs, and Red-Black Trees
""""""""""""""""""""""""""""""""""""""""""""""""""""

True or False?

Binary Search
-------------

* In the best case, the number of key comparisons for a binary search for a particular key in a sorted array of :math:`N` distinct keys is :math:`\sim \log N`.

  .. answer::

    **False.** In the best case, the searched key is located right at the first midpoint ``a[mid]``, requiring only :math:`\Theta(1)` (a single) key comparison! (:math:`\sim \log_2 N` is the worst-case and average-case number of comparisons).


Binary Search Trees
-------------------

Note: BST is understood here as the implementation from the textbook, i.e., a tree that is not necessarily balanced.
The 2-3 / red-black BST is also understood to be the one in the reference textbook.

We recommend that you first become familiar with the notions of `tree traversals <https://en.wikipedia.org/wiki/Tree_traversal>`_: inorder (infix), preorder (prefix), and postorder (postfix).

* Given the output of an inorder traversal of a BST containing :math:`N` distinct keys, is it possible to reconstruct the shape of the BST based on the result of the traversal? If so, write the pseudocode of an algorithm to do so; if not, give a counterexample that justifies your answer.

  .. answer::

    **False.** The inorder traversal of *any* valid BST containing a given set of :math:`N` keys simply outputs those keys in sorted ascending order, regardless of the tree's structure.
    *Counterexample*: The BST created by inserting ``10, 5, 15`` (rooted at ``10``) and the BST created by inserting ``5, 10, 15`` (a right-leaning chain rooted at ``5``) have different shapes but produce the exact same inorder traversal ``[5, 10, 15]``.

* Given the output of a preorder traversal of a BST containing :math:`N` distinct keys, is it possible to reconstruct the shape of the BST based on the result of the traversal? If so, write the pseudocode of an algorithm to do so; if not, give a counterexample that justifies your answer.

  .. answer::

    **True.** In a preorder traversal, the first element is always the root :math:`r`, followed by all keys in its left subtree (which are the keys :math:`< r`), followed by all keys in its right subtree (which are the keys :math:`> r`). Because the BST ordering property uniquely partitions the remaining elements around :math:`r`, the tree can be uniquely reconstructed in :math:`\Theta(N)` time using value bounds ``(min, max)``:

    .. code-block:: java

        private static Node readBSTFromPreorder(int[] input) {
            return readBSTFromPreorder(input, new int[]{0}, Integer.MIN_VALUE, Integer.MAX_VALUE);
        }

        private static Node readBSTFromPreorder(int[] input, int[] idx, int min, int max) {
            int i = idx[0];
            if (i < input.length && input[i] > min && input[i] < max) {
                int val = input[i];
                idx[0]++;
                Node left = readBSTFromPreorder(input, idx, min, val);
                Node right = readBSTFromPreorder(input, idx, val, max);
                return new Node(val, left, right);
            }
            return null;
        }

    *(Note: A postorder traversal also uniquely determines the BST by reading from right to left, whereas an inorder traversal does not.)*

* Given a binary search tree of :math:`N` distinct keys and a key :math:`x`, is it possible to find the smallest key strictly greater than :math:`x` in logarithmic time in the worst case?

  .. answer::

    **False.** A standard (unbalanced) BST can degenerate into a linked list of height :math:`N - 1` (for example, when keys are inserted in sorted order), so finding the higher key takes :math:`\Theta(N)` time in the worst case.

* The expected height of a BST resulting from inserting :math:`N` distinct keys in a random order into an initially empty tree is on average logarithmic.

  .. answer::

    **True.** When :math:`N` keys are inserted in uniformly random order, the expected depth of a search is :math:`\sim 2 \ln N \approx 1.39 \log_2 N` and the expected height of the tree is :math:`\Theta(\log N)` (while the best-case height is :math:`\lfloor \log_2 N \rfloor` and the worst-case height is :math:`N - 1`).

* Let :math:`x` be a node in a BST. The successor of :math:`x` (the node containing the next key in ascending order) is the leftmost node in the right subtree of :math:`x`.

  .. answer::

    **False in general.** This statement holds *only if* node :math:`x` has a non-empty right subtree! If ``x.right == null`` (for example, when :math:`x` is a leaf), its successor is instead the lowest ancestor of :math:`x` whose left subtree contains :math:`x`.


Red-Black Trees
---------------

For the statements related to red-black trees, we advise you to first translate them into statements about 2-3 trees,
as there is a one-to-one mapping between the two representations.
In most cases, it is easier to evaluate the validity of the statement for 2-3 trees.

* The maximum height of a 2-3 tree with :math:`N` keys is :math:`\sim \log_3 N`.

  .. answer::

    **False.** The **minimum** height of a 2-3 tree (when every node is a 3-node) is :math:`\sim \log_3 N`, whereas the **maximum** height (when every node is a 2-node) is :math:`\lfloor \log_2 N \rfloor` (see Proposition F, page 429).

* When inserting :math:`N` keys in ascending order into an initially empty red-black BST, the number of color changes for the last insertion is at most 3. The number of color changes is defined as the sum of the absolute differences between the number of red links after insertion and the number of red links before insertion.

  .. answer::

    **False.** If you insert keys such that the entire rightmost path of the corresponding 2-3 tree consists solely of 3-nodes, inserting one more larger key splits the bottom 3-node and propagates splits all the way up to the root, flipping the colors of :math:`\Theta(\log N)` links along the entire path.

* Does a red-black BST obtained after inserting :math:`N > 1` keys into an initially empty tree always have at least one red link? If not, give a counterexample.

  .. answer::

    **False.** When color flips propagate up to the root, a 3-node splits into three 2-nodes connected by black links. For example, after inserting keys ``2, 1, 3`` (or ``1, 2, 3``), the resulting red-black BST has root ``2`` with black left child ``1`` and black right child ``3``, containing **zero** red links.

* In a red-black BST of :math:`N` nodes, the black height (i.e., the number of black links on each path from the root to a null link) is at most :math:`\log_2 N`.

  .. answer::

    **True.** The black height of a Left-Leaning Red-Black BST equals the exact height of its corresponding 2-3 tree, which is at most :math:`\lfloor \log_2 N \rfloor`.


Sorting with a BST
""""""""""""""""""

Imagine a sorting algorithm using a BST. What would this algorithm look like?
What would be the complexity of your algorithm if the BST is replaced by a red-black BST?

.. answer::

    **Algorithm**:

    1. Insert all :math:`N` elements of the input array into an initially empty search tree.
    2. Perform an in-order traversal of the tree to output the elements in sorted order.

    **Time complexity**:

    * **With an unbalanced BST**: Building the tree takes :math:`\Theta(N^2)` in the worst case (e.g., if the input is already sorted) and :math:`\Theta(N \log N)` on average (equivalent to QuickSort's comparison tree). The in-order traversal takes :math:`\Theta(N)`. Total: :math:`\mathcal{O}(N^2)` worst case, :math:`\Theta(N \log N)` average case.
    * **With a Red-Black BST**: Each of the :math:`N` insertions is guaranteed to take :math:`\mathcal{O}(\log N)` time in the worst case, and the in-order traversal takes :math:`\Theta(N)`. Total: :math:`\Theta(N \log N)` worst-case time.


BST Deletion Complexity
"""""""""""""""""""""""

What is the time complexity of deleting the root key ``15`` from the BST depicted below using the textbook (Hibbard deletion) implementation?

.. code-block:: text

       15
         \
          x
         / \
        /   \
       /     \ 
      /n nodes\ 
     /         \
     -----------

.. answer::

    :math:`\Theta(1)` **time**.
    In the textbook implementation of ``delete(Node x, Key key)``, when the node to delete has ``x.left == null`` (at most one child), it immediately returns ``x.right`` without traversing the subtree rooted at ``x.right``!


Commutativity of BST Deletion
"""""""""""""""""""""""""""""

Is the delete operation (as implemented in the book) in a BST "commutative"?
That is, deleting :math:`x` and then directly :math:`y` from a BST
leaves the tree in the same state as if we had first deleted :math:`y` and then :math:`x`?
Give a counterexample or argue why this is indeed always the case.
To help you, consider the following tree and the deletion operations of 5 and 10.

.. code-block:: text

      10
     / \
    5   15
       /
      11

.. answer::

    **No, BST deletion is NOT commutative.**
    Using the given tree:

    * **Delete ``10`` then ``5``**: When deleting ``10``, it has two children (``5`` and ``15``), so Hibbard deletion replaces ``10`` with its successor ``11`` (the min of its right subtree). Next, deleting ``5`` removes the left child of ``11``, leaving ``11`` at the root with right child ``15``.
    * **Delete ``5`` then ``10``**: When deleting ``5`` first, ``10`` now only has a right child (``15``). Next, when deleting ``10``, since its left child is ``null``, ``10`` is simply replaced by its right child ``15``, leaving ``15`` at the root with left child ``11``!


BST Serialization
"""""""""""""""""

Data structure serialization refers to the process of converting a data structure (such as a list, tree, or graph) into a format that can be stored or transmitted and then reconstructed (deserialized) later.
Here, we are interested in reconstructing (deserializing) a BST that has been serialized using a preorder traversal.

Implement the reconstruction of a BST from the preorder traversal:
`Preorder reconstruction <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_PreorderToBST>`_


BirthdayMap
"""""""""""

An easy exercise to efficiently query persons by their birthday (exam 2023): `BirthdayMap <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_BirthdayMap>`_


Skyline
""""""""""

Design an efficient algorithm to compute the `Skyline <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_Skyline>`_ from a set of building shapes (rectangles) that can overlap.


Array BST, Put and Get
""""""""""""""""""""""

Special implementation of a binary search tree with ArrayLists (mid-term quiz 2022):
`ArrayBST put and get <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_ArrayBST>`_


Array BST, Delete
"""""""""""""""""

Implementation of the ``delete`` method in our array-based implementation of a BST (mid-term quiz 2023):
`ArrayBST with delete <https://inginious.info.ucl.ac.be/course/LINFO1121/searching_ArrayBST>`_
