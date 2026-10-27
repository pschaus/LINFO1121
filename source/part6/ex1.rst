.. _part6_ex1:

Exercises A
=======================================

.. note::
    You must complete these exercises by Wednesday of W12.


Graph Representations and Elementary Complexities
"""""""""""""""""""""""""""""""""""""""""""""""""

Give several data structures that can be used to represent an undirected graph :math:`G`
with :math:`n` vertices (nodes) and :math:`m` edges.

What are the time complexities of the elementary operations ``Iterable<Integer> adj(int v)`` and ``addEdge(int v, int w)`` for each?

.. answer::

    .. list-table:: Graph Representations Comparison
       :header-rows: 1

       * - Representation
         - Typical Java Type
         - Space
         - ``adj(v)`` (iterate over neighbors)
         - ``addEdge(v, w)``
       * - Adjacency Matrix
         - ``boolean[n][n]``
         - :math:`\Theta(n^2)`
         - :math:`\Theta(n)`
         - :math:`\Theta(1)`
       * - Incidence Matrix
         - ``boolean[n][m]``
         - :math:`\Theta(n \cdot m)`
         - :math:`\Theta(m)`
         - :math:`\Theta(n)` (or :math:`\Theta(nm)` if resized)
       * - Adjacency Lists
         - ``Bag<Integer>[n]`` / ``List<Integer>[n]``
         - :math:`\Theta(n + m)`
         - :math:`\Theta(\text{deg}(v))`
         - :math:`\Theta(1)`
       * - Edge List (Incidence List)
         - ``List<Edge>``
         - :math:`\Theta(m)`
         - :math:`\Theta(m)`
         - :math:`\Theta(1)`

    *Practical tip*: For weighted or labeled graphs, an array of lists of ``Edge`` objects (``List<Edge>[n]``) or an array of hash maps (``Map<Integer, Integer>[n]`` mapping neighbor :math:`w` to edge weight) provides both :math:`\Theta(\text{deg}(v))` neighbor iteration and :math:`\mathcal{O}(1)` edge-weight lookup.


Bipartite Graph Detection with DFS
""""""""""""""""""""""""""""""""""

A graph is bipartite if its vertices can be partitioned into two disjoint sets such that no edge connects two vertices of the same set.

Propose an algorithm to test whether a graph is bipartite and, if so, find such a partition.
What is the time complexity of your algorithm? Hint: Use DFS.

.. answer::

    A graph is bipartite if and only if it is **2-colorable** (which is equivalent to having no odd-length cycles).
    We can test this using Depth-First Search (or BFS):

    1. Maintain a ``boolean[] marked`` array and a ``boolean[] color`` array of size :math:`V`.
    2. Loop over all vertices :math:`s = 0 \dots V - 1` (to handle disconnected components): if ``!marked[s]``, start a DFS from :math:`s`.
    3. When visiting vertex :math:`v`, for each neighbor :math:`w \in G.\text{adj}(v)`:

       * If ``!marked[w]``, set ``marked[w] = true``, assign it the **opposite color** ``color[w] = !color[v]``, and recursively call ``dfs(G, w)``.
       * If ``marked[w]`` and ``color[w] == color[v]``, an edge connects two vertices of the same color, so the graph is **not bipartite** (return ``false``).

    **Time complexity**: :math:`\mathcal{O}(V + E)` with adjacency lists, since every vertex and edge is examined a constant number of times.


Non-Disconnecting Vertex Removal
""""""""""""""""""""""""""""""""

Prove that every connected graph has a vertex whose removal (along with its incident edges) does not disconnect the graph.
Write an algorithm that finds such a vertex. Hint: Use DFS and vertex marking.

.. answer::

    **Proof and Algorithm**:
    Run a Depth-First Search (DFS) starting from any arbitrary vertex :math:`s` on the connected graph :math:`G`.
    The edges traversed by the DFS to discover new vertices form a **DFS spanning tree** :math:`T` of :math:`G`.
    Consider the **last vertex** :math:`v` discovered by the DFS (or any leaf of the DFS spanning tree :math:`T`, i.e., a vertex from which ``dfs(v)`` makes no recursive calls to unvisited neighbors).
    Since every other vertex in :math:`G` was reached from :math:`s` along tree edges of :math:`T` *without passing through* :math:`v`, removing :math:`v` and its incident edges leaves the spanning tree :math:`T \setminus \{v\}` connected, so :math:`G \setminus \{v\}` remains connected!
    Finding this vertex takes :math:`\mathcal{O}(V + E)` time via DFS.


Maze Shortest Path
""""""""""""""""""

Consider an unweighted, undirected graph :math:`G` whose edges represent valid moves for a robot in a maze between positions (nodes).
Given a starting position and a destination node, implement a method to find a path to the exit that minimizes the number of moves: `Maze <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Maze>`_.
What is the time complexity of your method? Does it depend on the graph representation (for example, adjacency lists vs. adjacency matrix)?

.. answer::

    Use **Breadth-First Search (BFS)** starting from the source node (which explores vertices in increasing order of distance using a FIFO ``Queue``):

    * With **adjacency lists**, BFS runs in :math:`\mathcal{O}(V + E)` time.
    * With an **adjacency matrix**, finding the neighbors of each visited vertex takes :math:`\Theta(V)` time, degrading BFS to :math:`\mathcal{O}(V^2)` time. Since maze/grid graphs are **sparse** (:math:`E \le 2V \ll V^2`), adjacency lists (or implicit grid neighbor lookups) are dramatically faster.


Cycle Detection in Course Prerequisites
"""""""""""""""""""""""""""""""""""""""

The EPL course syllabus lists prerequisites for each course.
You want to verify that all courses can be taken, i.e., that there is no circular dependency between courses.

What algorithm do you propose to perform this check?
What is the time complexity of your method?

.. answer::

    Model the courses as vertices of a **directed graph** (with a directed edge :math:`u \to v` if course :math:`u` is a prerequisite for course :math:`v`), and test whether the directed graph is a **DAG** (Directed Acyclic Graph) using **3-color DFS cycle detection**:

    Maintain a ``status`` array for each vertex with 3 states:

    * ``0`` (*Unvisited*): not yet reached by DFS.
    * ``1`` (*Visiting / On current recursion stack*): DFS has started on this vertex and has not yet finished exploring all its descendants.
    * ``2`` (*Visited / Completed*): DFS has finished exploring all descendants of this vertex.

    If, while exploring neighbors of a vertex :math:`u`, we encounter a neighbor :math:`w` with ``status[w] == 1`` (already on the active recursion stack), we have found a **back-edge**, which proves the existence of a directed cycle!

    .. code-block:: java

        List<Integer>[] graph = ...;
        int[] status = new int[graph.length]; // initialized to 0
        boolean hasCycle = false;

        void dfs(int u) {
            status[u] = 1; // currently on recursion stack
            for (int w : graph[u]) {
                if (status[w] == 0) {
                    dfs(w);
                } else if (status[w] == 1) {
                    hasCycle = true; // back-edge -> directed cycle!
                }
            }
            status[u] = 2; // completed
        }

    Running ``dfs`` from every unvisited vertex takes :math:`\Theta(V + E)` time.


Kahn's Algorithm for Topological Sorting
""""""""""""""""""""""""""""""""""""""""

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

    .. code-block:: java

        List<Integer>[] graph = ...; // adjacency list
        List<Integer> order = new ArrayList<>();

        int[] inDegree = new int[graph.length];
        for (int u = 0; u < graph.length; u++) {
            for (int v : graph[u]) {
                inDegree[v]++;
            }
        }

        Queue<Integer> sources = new ArrayDeque<>();
        for (int u = 0; u < graph.length; u++) {
            if (inDegree[u] == 0) {
                sources.add(u);
            }
        }

        boolean isUnique = true;
        while (!sources.isEmpty()) {
            if (sources.size() > 1) {
                isUnique = false; // multiple independent choices at this step
            }
            int u = sources.poll();
            order.add(u);
            for (int v : graph[u]) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    sources.add(v);
                }
            }
        }
        // Note: if order.size() < graph.length, the graph contains a cycle!

    * **Time complexity**: :math:`\Theta(V + E)`, as each vertex is enqueued/dequeued at most once and each directed edge is inspected twice (once to compute ``inDegree``, once when its source is dequeued).
    * **Uniqueness**: A DAG has a **unique** topological ordering if and only if the ``sources`` queue **never contains more than 1 vertex** at the start of any iteration (equivalently, the DAG contains a Hamiltonian path visiting all vertices).


Reconstructing an MST After Removing k Edges
""""""""""""""""""""""""""""""""""""""""""""

Let :math:`G = (V,E)` be an edge-weighted undirected graph for which a minimum spanning tree (MST) has already been computed.
Suppose :math:`k` edges are removed from this MST.
Write a method to reconstruct an MST from the remaining :math:`|V|-1-k` edges.
The final MST does not need to be identical to the original one, but it must contain the :math:`|V|-1-k` preserved edges.

On what fundamental property (or properties) of MSTs is your algorithm based?
What is the time complexity of your method?

.. answer::

    * **Using Kruskal's Algorithm**:
      Removing :math:`k` edges from an MST leaves a forest of :math:`k + 1` connected components with :math:`|V| - 1 - k` edges. This forest is a valid intermediate state of Kruskal's algorithm!

      1. Initialize a ``UF`` (Union-Find) structure of size :math:`|V|` and call ``union(u, v)`` for each of the :math:`|V| - 1 - k` preserved MST edges in :math:`\mathcal{O}(V \alpha(V))` time.
      2. Sort all edges of :math:`G` by weight (or reuse the sorted edge list if already available) and iterate through them in non-decreasing order of weight: whenever an edge :math:`(u, v)` connects two different components in ``UF``, add it to the MST and merge their components until :math:`k` edges have been added.
      3. **Complexity**: :math:`\mathcal{O}(E \log E)` (or :math:`\mathcal{O}(E \alpha(V))` if the edges of :math:`G` were already sorted).

    * **Underlying property**: The **Cut Property** (Proposition J, page 606) and the greedy nature of MST construction. Contracting each of the :math:`k + 1` preserved subtrees into a super-vertex and running Kruskal's or Prim's algorithm on the contracted graph of :math:`k + 1` vertices is guaranteed to yield a minimum-weight spanning tree containing the preserved edges.


Forcing an Edge into an MST
"""""""""""""""""""""""""""

Let :math:`G = (V,E)` be an edge-weighted undirected graph for which an MST has already been computed.
Suppose an edge :math:`e = (u, v) \in E` with weight :math:`w` is not part of this MST.
How can you compute a new MST that is constrained to include :math:`e` by adapting the original MST? Describe your algorithm.
What is the time complexity? Hint: Use DFS on the original MST.

.. answer::

    **Algorithm**:

    1. Since the original MST :math:`T` is a spanning tree, there is a unique simple path in :math:`T` between :math:`u` and :math:`v`. Adding edge :math:`e = (u, v)` to :math:`T` creates a unique cycle :math:`C` consisting of :math:`e` and this tree path.
    2. Run a **DFS on the MST** :math:`T` starting from :math:`u` to find the path to :math:`v`, and identify the **maximum-weight (heaviest) edge** :math:`e_{\max}` along that path in :math:`T`.
    3. Remove :math:`e_{\max}` from :math:`T` and insert :math:`e = (u, v)`. The resulting graph :math:`T' = (T \setminus \{e_{\max}\}) \cup \{e\}` is a spanning tree of weight :math:`w(T) + w(e) - w(e_{\max})`, which is the minimum-weight spanning tree constrained to contain :math:`e`.

    **Time complexity**: Since :math:`T` has :math:`|V| - 1` edges, running DFS on :math:`T` takes :math:`\mathcal{O}(V)` time!


Dijkstra's Algorithm with java.util.PriorityQueue
"""""""""""""""""""""""""""""""""""""""""""""""""

Could ``java.util.PriorityQueue`` be used to efficiently implement Dijkstra's algorithm?
If not, why not? What would the time complexity be if you used this priority queue?

.. answer::

    **Yes, it can be used efficiently using lazy deletion!**

    * **Difference from the textbook's ``IndexMinPQ``**: The textbook's Dijkstra implementation uses an indexed priority queue (``IndexMinPQ``) supporting ``decreaseKey(w, newDist)`` in :math:`\mathcal{O}(\log V)` time, so the queue contains at most :math:`V` vertices and runs in :math:`\mathcal{O}((V + E) \log V)` time.
    * **With ``java.util.PriorityQueue`` (no ``decreaseKey``)**:
      Whenever edge relaxation improves ``distTo[w]``, we simply **insert a new pair** ``(w, distTo[w])`` into the priority queue without removing the older, larger entry for ``w``. When polling ``(v, d)`` from the priority queue, if ``d > distTo[v]`` (or if ``v`` was already settled), we simply ignore and skip this outdated entry!
    * **Time complexity**: Each of the :math:`E` edges can trigger at most one insertion into the priority queue, so the priority queue has size at most :math:`E`. Thus, there are at most :math:`E` insertions and :math:`E` removals, each costing :math:`\mathcal{O}(\log E)`.
      For any simple graph, :math:`E \le V^2 \implies \log E \le 2 \log V = \mathcal{O}(\log V)`.
      Therefore, the overall time complexity is :math:`\mathcal{O}((V + E) \log E) = \mathcal{O}((V + E) \log V)`, the **exact same asymptotic time complexity** (at the cost of :math:`\mathcal{O}(E)` space in the priority queue instead of :math:`\mathcal{O}(V)`).


Why Dijkstra Fails on Negative Edge Weights
"""""""""""""""""""""""""""""""""""""""""""

Explain why Dijkstra's algorithm (``DijkstraSP``) does not support edges with negative weights.
Would the computed distances be incorrect, or would the time complexity guarantee no longer hold?
Provide an example graph illustrating the problem.

.. answer::

    Dijkstra's greedy invariant relies on the fact that when all edge weights are non-negative, **adding more edges to a path can never decrease its total weight**. Therefore, when the unsettled vertex :math:`v` with minimum ``distTo[v]`` is extracted from the priority queue, no future path through other unsettled vertices could possibly reach :math:`v` with a smaller distance.

    When negative edge weights are present:

    * **With a negative cycle**: Shortest paths are not even well-defined (:math:`-\infty`).

      .. image:: dijkneg1.png

    * **Even without any negative cycle**:

      .. image:: dijkneg2.png

      In the DAG above, starting from ``A``:

      1. Standard Dijkstra (which settles each vertex once) first settles ``A`` (:math:`d=0`), relaxes ``B`` (:math:`d=6`) and ``C`` (:math:`d=4`), and then permanently settles ``C`` with distance ``4`` before ever expanding ``B``! When ``B`` is finally expanded, the negative edge ``B -> C`` of weight ``-6`` reveals a shorter path ``A -> B -> C`` of total weight :math:`6 - 6 = 0 < 4`, so **the computed distance for ``C`` (and anything reachable from ``C``) is incorrect**.
      2. If you modify Dijkstra to re-insert already-settled vertices into the priority queue whenever their distance improves, it computes the right distances on graphs without negative cycles, but its worst-case time complexity **blows up to exponential time** :math:`\Omega(2^V)` on certain graphs!


Shifting Negative Edge Weights in Dijkstra
""""""""""""""""""""""""""""""""""""""""""

Let :math:`G` be a directed graph with potentially negative edge weights, but without any negative cycles.
Suppose we want to find the shortest path between a vertex :math:`u` and a vertex :math:`v`.
We only have access to an implementation of Dijkstra's algorithm that does not support negative weights.
A proposed heuristic is to add a constant to all edge weights equal to the absolute value of the most negative weight (making all weights non-negative), and then run Dijkstra's algorithm on this modified graph.
Is this method valid?
If so, prove it. If not, provide a counterexample.

.. answer::

    **No, this heuristic is INVALID!**
    Adding a positive constant :math:`c > 0` to every edge does **not** add the same amount to every path: a path with :math:`k` edges has its total weight increased by :math:`k \cdot c`, which penalizes paths with more edges!

    *Counterexample*: Consider the graph from the *Dijkstra and Negative Edge Weights* exercise above where we add :math:`c = 6` to every edge to make all weights non-negative:

    .. image:: dijkneg3.png

    * In the **original graph**, the shortest path from ``A`` to ``C`` is ``A -> B -> C`` (2 edges) with weight :math:`6 + (-6) = 0`, which is shorter than the direct edge ``A -> C`` (1 edge) of weight :math:`4`.
    * In the **shifted graph** (:math:`+6` per edge), ``A -> B -> C`` has weight :math:`(6+6) + (-6+6) = 12` (increased by :math:`2 \times 6 = 12`), whereas the direct edge ``A -> C`` has weight :math:`4 + 6 = 10` (increased by :math:`1 \times 6 = 6`). Dijkstra on the shifted graph chooses ``A -> C`` instead of the true shortest path ``A -> B -> C``!


Longest Path and Bellman-Ford with Negated Weights
""""""""""""""""""""""""""""""""""""""""""""""""""

Let :math:`G` be a directed graph with positive edge weights. We want to find the longest path between vertex :math:`u` and vertex :math:`v`.
Suppose we have an implementation of the Bellman-Ford algorithm (which supports negative weights).
Can we simply negate all edge weights and compute the shortest path using Bellman-Ford?
Is this method valid? If not, can you propose an algorithm to find the longest simple path?
Does your method apply to all graphs? If not, what specific class of graphs can it handle?

.. answer::

    * **Does negating edge weights work on general graphs?**
      Wait: if the original positive-weighted graph :math:`G` contains **any directed cycle**, negating all edge weights turns that cycle into a **negative-weight cycle**, so Bellman-Ford will fail (the longest walk is :math:`+\infty`, and finding the longest *simple* path in a general graph with cycles is **NP-hard**, so no polynomial-time algorithm is known).
    * **When does it work?**
      It works if and only if :math:`G` is a **Directed Acyclic Graph (DAG)**! Because a DAG has no cycles, negating its edge weights creates no negative cycles. Even better, in a **DAG**, we don't even need Bellman-Ford (:math:`\mathcal{O}(V \cdot E)`): we can compute the longest path in linear time :math:`\Theta(V + E)` by relaxing vertices in **topological order** (initializing ``distTo[s] = 0``, ``distTo[v] = -infinity`` and updating ``distTo[w] = Math.max(distTo[w], distTo[v] + e.weight())``).


Digraph Data Structure
""""""""""""""""""""""

Implement a `Digraph Data Structure <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Digraph>`_.


Depth-First Paths
"""""""""""""""""

Implement an algorithm for finding a path (its length does not matter) between a source node and a destination using
`Depth First Search <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_DepthFirstPaths>`_.


Connected Components
""""""""""""""""""""

Implement the computation of the number of connected components in a Graph:
`ConnectedComponents <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_ConnectedComponents>`_.


Covid Bubbles
"""""""""""""

A programming exercise on finding which contacts to prohibit in a network to satisfy Belgian COVID-19 bubble regulations:
`Covid bubbles <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_Bubbles>`_.


Multi-Source Shortest Paths
"""""""""""""""""""""""""""

A programming exercise on BFS to find the shortest path from multiple possible sources to a destination node:
`BFS multiple sources <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_BreadthFirstShortestPaths>`_.


Global Warming Shortest Path
""""""""""""""""""""""""""""

A programming exercise on shortest path in an implicit graph:
`Global Warming Path <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarmingPaths>`_.


Global Warming Islands with DFS
"""""""""""""""""""""""""""""""

Revisit the computation of the number of islands, this time using DFS rather than union-find:
`Global Warming Island <https://inginious.info.ucl.ac.be/course/LINFO1121/graphs_GlobalWarming>`_.
