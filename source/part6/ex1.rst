.. _part2_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W12.



Exercise 6.1.1
""""""""""""""

Give several data structures that can be used to represent an undirected :math:`G` graph
with :math:`n` nodes (vertex) and :math:`m` arcs (edges).

What are the complexities of the elementary operations ``Iterable<Integer> adj(int v)`` and ``addEdge(int v, int w)``?


.. answer::

    .. list-table:: Résumé des différentes implémentations
      :header-rows: 1

      * - Nom
        - Type usuel
        - ``ajd(v)``
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

A graph is bipartite if its nodes can be divided into two disjoint sets so that there is no arc
between two nodes of the same set.

Propose a method to test if a graph is bipartite and if so who would find such a partition.
What is the complexity of your algorithm? Hint: use a DFS.

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

Prove that any connected graph has a node whose removal (including incident arcs) would not disconnect the graph.
Write a method that finds such a node. Hint: use a DFS and node marking.

.. answer::

    Quand on visite le "dernier" noeud dans un DFS, c'est que l'on a atteind tout les autres noeuds d'abord
    via le noeud de départ, sans utiliser le dernier noeud.

    Celui-ci peut donc être retiré.

Exercise 6.1.4 (Inginious)
""""""""""""""""""""""""""""

Let be an undirected and weightless graph :math:`G` whose arcs represent the possible elementary moves of a robot in a maze from all possible positions (nodes). 
Given the current position and a node, implement method to find a path to the exit that minimizes the number of elementary moves: `Maze <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Maze>`_.
What is the complexity of your method? Does it depend on the implementation of the graph (for example if it is an adjacency matrix?)



.. answer::

    BFS. Bien demander d'expliquer l'algorithme. Noter la *seule* différence entre le BFS et le DFS: l'usage d'une ``Queue`` plutot que d'une ``Stack``.
    Avec une liste d'adjacence, l'algo est en :math:`\mathcal{O}(n+m)`. Avec une matrice d'incidence, c'est :math:`\mathcal{O}(n^2)`...

    Dans un graphe simplement connecté :math:`m` peut être aussi grand que :math:`\mathcal{O}(n^2)`.
    Du coup, est-ce grave?
    Oui car généralement les graphes sont très sparse et donc :math:`m << n^2`

Exercise 6.1.5
""""""""""""""

The EPL course syllabus lists the prerequisites for each course.
You want to make sure that all courses can be taken, i.e. that there is no cycle of dependency between courses.

What method do you propose to perform this test?
What would be the time complexity of your method?

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

Develop (write the code) a topological sorting algorithm for a directed graph that maintains an array of the size of the number of
nodes with each entry corresponding to the in-degree of each node.
Your algorithm also maintains a queue of *sources* (nodes with an in-degree of 0).
Initialize these two structures in a single pass on all edges.
Then perform the following operations until the source queue becomes empty:

* remove a source from the queue and mark it.
* decrement the in-degree of the adjacent destinations of the node marked in the previous step.
* if the in-degree of a node becomes 0, insert it in the source queue.

Is it possible to detect whether the topological sort is unique? 
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

Let :math:`G(V,E)` be an undirected graph with weights on which a minimum spanning tree has been computed.
Then :math:`k` arcs have been randomly removed from this MST.
Write a method to retrieve an MST from the partial MST.
The final MST does not have to be identical to the original, only the remaining :math:`V-1-k` arcs must
at least be present.

On what important property(ies) of MSTs is your algorithm based?
What is the complexity of your method?

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

Let :math:`G(V,E)` be an undirected graph with weight on which a minimum spanning tree has been computed.
The edge :math:`e \in E` of weight :math:`w` is not part of this MST.
Can you recompute an MST that would include :math:`e` by adapting the original MST? Describe your algorithm (code).
What is the time complexity? Hint: DFS on the original MST.


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

Could ``java.util.PriorityQueue`` be used to effectively implement Dijkstra?
If not, why not? What would be the complexity of using this priority queue?

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

Explain why DijkstraSP does not support arcs with negative weight?
Would the result be wrong or would the complexity no longer be guaranteed?
Show an example of input that illustrates the problem.

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

Let :math:`G` be a graph with potentially negative weights but there is no negative cycle.
I am looking for the shortest path between a :math:`u` node and a :math:`v` node.
I have at my disposal an implementation of Dijkstra which does not allow to manage negative weights.
So I just have to increase all the weights by the same amount corresponding to the absolute value of the smallest weight and apply Dijkstra to the
and to apply Dijkstra on this graph.
Is this method valid?
If yes, prove it.
If not, show a counter example.

.. answer::

    En partant du dernier exemple de la question précédente:

    .. image:: dijkneg3.png

    Est-ce que ça marche ici?

Exercise 6.1.12
"""""""""""""""

Let :math:`G` be a graph with positive weights. I am looking for the longest path between a :math:`u` node and a :math:`v` node.
I have at my disposal the Bellman-Ford implementation (which supports negative weights).
I just need to compute the shortest path on the same graph with the opposite weights.
Is this method valid? If not, can you propose a method to compute the longest path?
Does your method apply to all graphs? If not, what particular types of graphs can it handle?

.. answer::

    Ca marche ssi le graphe original est un DAG (et que donc il ne forme pas de cycle négatifs en faisant l'opposé des poids).



Exercise 6.1.13 (Inginious)
"""""""""""""""""""""""""""

Implement a
`Digraph Data Structure <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Digraph>`_



Exercise 6.1.14 (Inginious)
"""""""""""""""""""""""""""

Implement a
`Depth First Search <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_DepthFirstPaths>`_


Exercise 6.1.15 (Inginious)
"""""""""""""""""""""""""""

Implement the computation of the number of connected components in a Graph:
`ConnectedComponents <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_ConnectedComponents>`_



Exercise 6.1.16 (Inginious)
"""""""""""""""""""""""""""

A programming exercise on finding
the the relations to forbid in a contact network
to satisfy the belgian covid rules:
`Covid bubbles  <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Bubbles>`_


Exercise 6.1.17 (Inginious)
"""""""""""""""""""""""""""

A programming exercise on BFS from multiple sources:
`BFS multiple sources <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_BreadthFirstShortestPaths>`_



Exercise 6.1.18 (Inginious)
"""""""""""""""""""""""""""

A programming exercise on shortest path in an implicit graph:
`Global Warming Path <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarmingPaths>`_


Exercise 6.1.19 (Inginious)
"""""""""""""""""""""""""""

Revisit your computation of the number of islands but this time using DFS rather than union-find
`Global Warming Island <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarming>`_



