.. _part6_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W12.



Exercise 6.1.1
""""""""""""""

Give several data structures that can be used to represent an undirected graph :math:`G`
with :math:`n` vertices (nodes) and :math:`m` edges.

What are the time complexities of the elementary operations ``Iterable<Integer> adj(int v)`` and ``addEdge(int v, int w)`` for each?


.. answer::

    .. list-table:: Résumé des différentes implémentations
      :header-rows: 1

      * - Nom
        - Type usuel
        - ``adj(v)``
        - ``addEdge(v)``
      * - Matrice d'adjacence
        - ``boolean[n][n]``
        - :math:`\Theta(n)`
        - :math:`\Theta(1)`
      * - Matrice d'incidence
        - ``boolean[m][n]``
        - :math:`\Theta(m)`
        - :math:`\Theta(n+m)` ou :math:`\Theta(nm)`
      * - Liste d'adjacence
        - ``List<Integer>[n]``
        - :math:`\Theta(\text{degré du noeud})`
        - :math:`\Theta(1)`
      * - Liste d'incidence
        - ``List<Edge>``
        - :math:`\Theta(m)`
        - :math:`\Theta(1)`

    Faire remarquer que parfois, on veut stocker de l'information supplémentaire sur une edge, comme son poids.
    L'objet ``Edge`` de la liste d'incidence peut servir à ça. Une variante "liste d'incidence" ultra pratique est
    le double HashMap: ``HashMap<Node, HashMap<Node, Property>>``, modifiable à toutes les sauces.

    ``HashMap<Integer,Integer>[]`` est dans la même veine le must have pour les graphes avec noeuds indexés par des
    entiers, et avec des poids entiers.

Exercise 6.1.2
""""""""""""""

A graph is bipartite if its vertices can be partitioned into two disjoint sets such that no edge connects two vertices of the same set.

Propose an algorithm to test whether a graph is bipartite and, if so, find such a partition.
What is the time complexity of your algorithm? Hint: Use DFS.

.. answer::

    With a DFS:
    All nodes are white initially. We will color the nodes in red or blue.
    We start in red.
    Each time we cross a node:

    - if it is white, we set it to the current color
    - if it is the current color, we do nothing
    - if it is of the other color, the graph is not bipartite
    - then we change color (from red to blue or blue to red).
    - we visit the immediate neighbors, recursively.

    If when we have visited all the nodes we have not detected any error, it means that the graph is bipartite (! initial connectivity...)


Exercise 6.1.3
""""""""""""""

Prove that every connected graph has a vertex whose removal (along with its incident edges) does not disconnect the graph.
Write an algorithm that finds such a vertex. Hint: Use DFS and vertex marking.

.. answer::

    Quand on visite le "dernier" noeud dans un DFS, c'est que l'on a atteind tout les autres noeuds d'abord
    via le noeud de départ, sans utiliser le dernier noeud.

    Celui-ci peut donc être retiré.

Exercise 6.1.4 (INGInious: Maze)
""""""""""""""""""""""""""""""""

Consider an unweighted, undirected graph :math:`G` whose edges represent valid moves for a robot in a maze between positions (nodes). 
Given a starting position and a destination node, implement a method to find a path to the exit that minimizes the number of moves: `Maze <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Maze>`_.
What is the time complexity of your method? Does it depend on the graph representation (for example, adjacency lists vs. adjacency matrix)?



.. answer::

    BFS. Bien demander d'expliquer l'algorithme. Noter la *seule* différence entre le BFS et le DFS: l'usage d'une ``Queue`` plutot que d'une ``Stack``.
    Avec une liste d'adjacence, l'algo est en :math:`\mathcal{O}(n+m)`. Avec une matrice d'incidence, c'est :math:`\mathcal{O}(n^2)`...

    Dans un graphe simplement connecté :math:`m` peut être aussi grand que :math:`\mathcal{O}(n^2)`.
    Du coup, est-ce grave?
    Oui car généralement les graphes sont très sparse et donc :math:`m << n^2`

Exercise 6.1.5
""""""""""""""

The EPL course syllabus lists prerequisites for each course.
You want to verify that all courses can be taken, i.e., that there is no circular dependency between courses.

What algorithm do you propose to perform this check?
What is the time complexity of your method?

.. answer::

    Un DFS (correctement écrit) permet de détecter les cycles. L'idée est la suivante: on va
    marquer chaque noeud suivant 3 états. Non visité (pas encore atteind par le DFS), en cours de visite (tout ses
    voisins n'ont pas encore été visités, i.e. le DFS est en train de faire une récursion depuis ce noeud) et
    visité (le DFS a fini ses récursions sur ce noeud).

    Si on croise dans notre DFS un noeud X qui est déjà "en cours de visite", c'est qu'il existe un chemin
    entre le noeud courant Y et le noeud X, mais également entre le noeud X et le noeud Y vu qu'il
    est en cours de visite (et que donc la "stack trace" du DFS crée ce chemin). Autrement dit, il y a un cycle.

    Demandez aux étudiants d'écrire le code en récursif.

    .. code-block:: java

        List<Integer>[] graph = ...;
        int[] status = new int[graph.length];
        boolean hasCycle = false;
        Arrays.fill(status, 0); //0 == non-visité

        void visit(int node) {
            status[nei] = 1; //en visite
            for(Integer nei: graph[node]) {
                if(status[nei] == 0)
                    visit(nei);
                else if(status[nei] == 1)
                    hasCycle = true;
                //ignore if already visited
            }
            status[nei] = 2; //visité
        }

        visit(0);

    (NB: ce code a été écrit sans IDE et n'a pas été testé ;-))

    Comment adapter ce code si on veut extraire le cycle?

    Il suffit de "sauvegarder" par quel noeud chaque noeud a été atteint, puis de remonter
    la liste chainée résultat de Y vers X.

Exercise 6.1.6
""""""""""""""

Develop (write the code for) a topological sorting algorithm for a directed graph that maintains an array of size :math:`V` where each entry corresponds to the in-degree of a vertex.
Your algorithm should also maintain a queue of *sources* (vertices with an in-degree of 0).
Initialize these two structures in a single pass over all edges.
Then, repeat the following steps until the source queue is empty:

* Remove a source from the queue and add it to the topological order.
* Decrement the in-degree of each neighbor of that vertex.
* If the in-degree of a neighbor becomes 0, insert it into the source queue.

How can you detect whether the topological sort is unique? 
What is the time complexity of your algorithm?

.. answer::

    (code non testé, mais donne l'idée générale)

    .. code-block::

        List<Integer>[] graph = ...; //liste d'adjacence
        List<Integer> out = new LinkedList<>(); //output

        int[] inDegree = new int[graph.length];
        Arrays.fill(inDegree, 0);

        for(int i = 0; i < graph.length; i++)
            for(Integer j: graph[i])
                inDegree[j] += 1;

        Queue<Integer> todo = new LinkedList<>(); //ou n'importe quelle DS qui est O(1) insert/delete
        for(int i = 0; i < graph.length; i++)
            if(inDegree[i] == 0)
                todo.add(i);

        while (!todo.isEmpty()) {
            int now = todo.poll();
            out.add(now);
            for(Integer j: graph[now]) {
                inDegree[j]--;
                if(inDegree[j] == 0)
                    todo.add(j);
            }
        }

    Complexité: :math:`\mathcal{O}(n+m)`. On passe deux fois par chaque noeud et chaque arete.

    Un toposort n'est pas unique ssi il existe deux noeuds sur la même "profondeur", car ils peuvent être interchangés.
    On peut détecter ça en utilisant par exemple deux queues...

    .. code-block::

        // remplacer le code de la boucle while par ceci

        boolean hasMultipleOutputs = false;
        while (!todo.isEmpty()) {
            hasMultipleOutputs |= todo.size() != 1;
            Queue<Integer> nextTodo = new LinkedList<>();

            while (!todo.isEmpty()) {
                int now = todo.poll();
                out.add(now);
                for (Integer j : graph[now]) {
                    inDegree[j]--;
                    if (inDegree[j] == 0)
                        nextTodo.add(j);
                }
            }

            todo = nextTodo;
        }

Exercise 6.1.7
""""""""""""""

Let :math:`G = (V,E)` be an edge-weighted undirected graph for which a minimum spanning tree (MST) has already been computed.
Suppose :math:`k` edges are removed from this MST.
Write a method to reconstruct an MST from the remaining :math:`|V|-1-k` edges.
The final MST does not need to be identical to the original one, but it must contain the :math:`|V|-1-k` preserved edges.

On what fundamental property (or properties) of MSTs is your algorithm based?
What is the time complexity of your method?

.. answer::

    La majorité des étudiants constate qu'une "foret de morceaux d'arbres" telle qu'obtenue ici est en fait
    un état intermédiaire de l'algorithme de Kruskal.

    Une autre manière de faire, et qui est intéressante pour la comprehésension de étudiants, est d'utiliser Prim.

    On peut "compacter" chaque morceau d'arbre en un seul noeud, qui aurait comme aretes l'ensemble des aretes "sortant
    de l'arbre". On peut ensuite lancer Prim (ou n'importe quel algorithme!) et générer un nouvel arbre.
    Ensuite on peut "defusionner" les noeuds qui étaient auparavant des arbres, et magie!

    C'est forcément assez compliqué à implémenter, mais c'est algorithmiquement élégant et montre bien
    que tout les algorithmes trouvent toujours une solution optimale à partir de n'importe quelle solution partielle
    i.e. ils sont greedy.

Exercise 6.1.8
""""""""""""""

Let :math:`G = (V,E)` be an edge-weighted undirected graph for which an MST has already been computed.
Suppose an edge :math:`e \in E` with weight :math:`w` is not part of this MST.
How can you compute a new MST that is constrained to include :math:`e` by adapting the original MST? Describe your algorithm.
What is the time complexity? Hint: Use DFS on the original MST.


.. answer::

    Par définition d'un arbre, ajouter cette edge créerait un cycle. Pour que le résultat reste un arbre,
    il faut supprimer une arète de ce nouveau cycle (pas :math:`e`), et pour minimiser le résultat, il faut en fait
    supprimer l'arete la plus petite du cycle.

    C'est faisable par un DFS pour trouver le chemin (unique!) entre les deux noeuds dans l'arbre.

    Comment prouver que ce MST est bien minimal, sous contrainte de l'inclusion de :math:`e`?
    Il suffit de voir que si on démarrait avec les deux noeuds liés à :math:`e` fusionné, l'arbre obtenu
    ici est bien un MST.


Exercise 6.1.9
""""""""""""""

Could ``java.util.PriorityQueue`` be used to efficiently implement Dijkstra's algorithm?
If not, why not? What would the time complexity be if you used this priority queue?

.. answer::

    Dans le livre, l'implémentation de l'algorithme de Dijkstra est basée sur une file de priorité dans laquelle
    on peut changer la priorité d'un élément. ``java.util.PriorityQueue`` ne permet pas cela. Cela dit, ce n'est
    pas très grave.

    Lors de l'algorithme, chaque fois qu'on trouve un chemin plus court vers un noeud, on doit "mettre à jour"
    son poids dans la PQ. Une autre option est en fait de "re-ajouter" le noeud dans la queue avec son nouveau
    poids. Pour que cela marche, il faut ne considérer le noeud que la première fois qu'on le retire de la PQ.

    L'algorithme de dijkstra du livre est dans :math:`\mathcal{O}((V+E)\log V)`. L'algorithme proposé ici
    ne change pas le multiplicateur du logarithme, mais bien le logarithme, qui est la taille maximale de la PQ.

    Chaque noeud :math:`v` pouvant être maintenant ajouté au plus :math:`\text{degré}(v)` fois, et vu que :math:`\sum_v \text{degré}(v) = E`
    on obtient :math:`\mathcal{O}((V+E)\log E)`.

    Il se trouve qu'on peut simplifier tout (multi-)graphe en entrée du Dijkstra en utilisant la propriété
    que tout chemin "le plus court" passera forcément, s'il existe plusieurs edges entre une paire de noeuds,
    par l'edge de poids le plus faible. Sans perte de généralité, on a donc toujours un graphe simple.

    Hors dans un graphe simple, on a toujours que :math:`E < V^2`. Autrement dit:

    .. math::

        \mathcal{O}((V+E)\log E) \subseteq \mathcal{O}((V+E)\log (V^2)) = \mathcal{O}(2(V+E)\log V) = \mathcal{O}((V+E)\log V)

    On a donc la même complexité!

Exercise 6.1.10
"""""""""""""""

Explain why Dijkstra's algorithm (``DijkstraSP``) does not support edges with negative weights.
Would the computed distances be incorrect, or would the time complexity guarantee no longer hold?
Provide an example graph illustrating the problem.

.. answer::

    Avec des cycles négatifs:

    .. image:: dijkneg1.png

    Sans cycle négatifs:

    .. image:: dijkneg2.png

    Dans les deux cas ça ne marche pas. Avec cycle négatif == il n'existe pas de chemin le plus court.
    Sans cycle négatif, on arrive à C avec une taille de chemin de 4 mais la véritable valeur est 0.
    Si on laisse l'algo se "corriger" et recommencer à explorer de C, on peut créer des cas où la complexité
    devient exponentielle.

Exercise 6.1.11
"""""""""""""""

Let :math:`G` be a directed graph with potentially negative edge weights, but without any negative cycles.
Suppose we want to find the shortest path between a vertex :math:`u` and a vertex :math:`v`.
We only have access to an implementation of Dijkstra's algorithm that does not support negative weights.
A proposed heuristic is to add a constant to all edge weights equal to the absolute value of the most negative weight (making all weights non-negative), and then run Dijkstra's algorithm on this modified graph.
Is this method valid?
If so, prove it. If not, provide a counterexample.

.. answer::

    En partant du dernier exemple de la question précédente:

    .. image:: dijkneg3.png

    Est-ce que ça marche ici?

Exercise 6.1.12
"""""""""""""""

Let :math:`G` be a directed graph with positive edge weights. We want to find the longest path between vertex :math:`u` and vertex :math:`v`.
Suppose we have an implementation of the Bellman-Ford algorithm (which supports negative weights).
Can we simply negate all edge weights and compute the shortest path using Bellman-Ford?
Is this method valid? If not, can you propose an algorithm to find the longest simple path?
Does your method apply to all graphs? If not, what specific class of graphs can it handle?

.. answer::

    Ca marche ssi le graphe original est un DAG (et que donc il ne forme pas de cycle négatifs en faisant l'opposé des poids).



Exercise 6.1.13 (INGInious)
"""""""""""""""""""""""""""

Implement a
`Digraph Data Structure <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Digraph>`_



Exercise 6.1.14 (INGInious)
"""""""""""""""""""""""""""

Implement an algorithm for finding a path (its length does not matter) between a source node and a destination using
`Depth First Search <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_DepthFirstPaths>`_


Exercise 6.1.15 (INGInious)
"""""""""""""""""""""""""""

Implement the computation of the number of connected components in a Graph:
`ConnectedComponents <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_ConnectedComponents>`_



Exercise 6.1.16 (INGInious)
"""""""""""""""""""""""""""

A programming exercise on finding which contacts to prohibit in a network to satisfy Belgian COVID-19 bubble regulations:
`Covid bubbles <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Bubbles>`_


Exercise 6.1.17 (INGInious)
"""""""""""""""""""""""""""

A programming exercise on BFS to find the shortest path from multiple possible sources to a destination node:
`BFS multiple sources <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_BreadthFirstShortestPaths>`_



Exercise 6.1.18 (INGInious)
"""""""""""""""""""""""""""

A programming exercise on shortest path in an implicit graph:
`Global Warming Path <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarmingPaths>`_


Exercise 6.1.19 (INGInious)
"""""""""""""""""""""""""""

Revisit the computation of the number of islands, this time using DFS rather than union-find:
`Global Warming Island <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarming>`_



