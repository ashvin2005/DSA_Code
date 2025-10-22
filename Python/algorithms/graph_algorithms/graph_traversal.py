"""
Graph Traversal Algorithms - DFS and BFS
=======================================

Algorithm Description:
Graph traversal algorithms are used to visit all vertices in a graph systematically.
Two fundamental traversal algorithms are:

1. Depth-First Search (DFS):
   - Explores as far as possible along each branch before backtracking
   - Uses a stack (or recursion) to keep track of vertices to visit
   - Time Complexity: O(V + E) where V = vertices, E = edges
   - Space Complexity: O(V) for the stack and visited set

2. Breadth-First Search (BFS):
   - Explores all neighbors at the present depth before moving to next level
   - Uses a queue to keep track of vertices to visit
   - Time Complexity: O(V + E)
   - Space Complexity: O(V) for the queue and visited set

Applications:
DFS Applications:
- Detecting cycles in a graph
- Topological sorting
- Finding strongly connected components
- Solving maze problems
- Path finding

BFS Applications:
- Shortest path in unweighted graphs
- Level-order traversal
- Finding connected components
- Social networking (degrees of separation)
- Web crawlers
"""

from collections import deque, defaultdict
from typing import List, Set, Dict, Any


class Graph:
    """
    Graph representation using adjacency list.
    """
    
    def __init__(self, directed=False):
        """
        Initialize a graph.
        
        Args:
            directed (bool): True for directed graph, False for undirected
        """
        self.graph = defaultdict(list)
        self.directed = directed
        self.vertices = set()
    
    def add_edge(self, u, v):
        """
        Add an edge to the graph.
        
        Args:
            u: Source vertex
            v: Destination vertex
        """
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        
        # For undirected graph, add reverse edge
        if not self.directed:
            self.graph[v].append(u)
    
    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self.vertices.add(v)
        if v not in self.graph:
            self.graph[v] = []
    
    def get_vertices(self):
        """Return all vertices in the graph."""
        return list(self.vertices)
    
    def get_neighbors(self, v):
        """Get neighbors of a vertex."""
        return self.graph[v]
    
    def __str__(self):
        """String representation of the graph."""
        result = []
        for vertex in sorted(self.vertices):
            neighbors = ", ".join(map(str, self.graph[vertex]))
            result.append(f"{vertex} -> [{neighbors}]")
        return "\n".join(result)


def dfs_recursive(graph, start, visited=None):
    """
    Perform Depth-First Search recursively.
    
    Args:
        graph (Graph): The graph to traverse
        start: Starting vertex
        visited (set): Set of visited vertices
    
    Returns:
        list: Vertices in DFS order
    """
    if visited is None:
        visited = set()
    
    result = []
    
    if start not in visited:
        visited.add(start)
        result.append(start)
        
        for neighbor in graph.get_neighbors(start):
            if neighbor not in visited:
                result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Perform Depth-First Search iteratively using a stack.
    
    Args:
        graph (Graph): The graph to traverse
        start: Starting vertex
    
    Returns:
        list: Vertices in DFS order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors in reverse order so they're processed in original order
            neighbors = graph.get_neighbors(vertex)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def dfs_all_paths(graph, start, end, path=None):
    """
    Find all paths between start and end vertices using DFS.
    
    Args:
        graph (Graph): The graph to search
        start: Starting vertex
        end: Destination vertex
        path (list): Current path being explored
    
    Returns:
        list: List of all paths from start to end
    """
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get_neighbors(start):
        if neighbor not in path:  # Avoid cycles
            new_paths = dfs_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths


def bfs(graph, start):
    """
    Perform Breadth-First Search.
    
    Args:
        graph (Graph): The graph to traverse
        start: Starting vertex
    
    Returns:
        list: Vertices in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between two vertices using BFS.
    
    Args:
        graph (Graph): The graph to search
        start: Starting vertex
        end: Destination vertex
    
    Returns:
        list: Shortest path from start to end, or None if no path exists
    """
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found


def bfs_level_order(graph, start):
    """
    Perform level-order BFS, returning vertices grouped by distance from start.
    
    Args:
        graph (Graph): The graph to traverse
        start: Starting vertex
    
    Returns:
        dict: Dictionary mapping distance to list of vertices at that distance
    """
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    levels = defaultdict(list)
    
    while queue:
        vertex, level = queue.popleft()
        levels[level].append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    return dict(levels)


def has_cycle_directed(graph):
    """
    Detect cycle in a directed graph using DFS.
    
    Args:
        graph (Graph): Directed graph to check
    
    Returns:
        bool: True if cycle exists, False otherwise
    """
    visited = set()
    rec_stack = set()
    
    def dfs_cycle(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle(vertex):
                return True
    
    return False


def has_cycle_undirected(graph):
    """
    Detect cycle in an undirected graph using DFS.
    
    Args:
        graph (Graph): Undirected graph to check
    
    Returns:
        bool: True if cycle exists, False otherwise
    """
    visited = set()
    
    def dfs_cycle(vertex, parent):
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle(vertex, None):
                return True
    
    return False


def connected_components(graph):
    """
    Find all connected components in an undirected graph using DFS.
    
    Args:
        graph (Graph): Undirected graph
    
    Returns:
        list: List of connected components (each is a list of vertices)
    """
    visited = set()
    components = []
    
    def dfs_component(vertex, component):
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_component(neighbor, component)
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            component = []
            dfs_component(vertex, component)
            components.append(component)
    
    return components


def topological_sort(graph):
    """
    Perform topological sorting on a directed acyclic graph (DAG) using DFS.
    
    Args:
        graph (Graph): Directed acyclic graph
    
    Returns:
        list: Vertices in topological order, or None if graph has a cycle
    """
    if has_cycle_directed(graph):
        return None
    
    visited = set()
    stack = []
    
    def dfs_topo(vertex):
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_topo(neighbor)
        
        stack.append(vertex)
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            dfs_topo(vertex)
    
    return stack[::-1]


def is_bipartite(graph):
    """
    Check if a graph is bipartite using BFS coloring.
    
    Args:
        graph (Graph): Graph to check
    
    Returns:
        tuple: (is_bipartite, coloring) where coloring maps vertices to colors (0 or 1)
    """
    color = {}
    
    for start in graph.get_vertices():
        if start in color:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return False, {}
    
    return True, color


def test_graph_traversal():
    """Comprehensive test cases for graph traversal algorithms."""
    print("Testing Graph Traversal Algorithms")
    print("=" * 50)
    
    # Test 1: DFS on undirected graph
    print("\nTest 1: DFS on Undirected Graph")
    g1 = Graph(directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    for u, v in edges:
        g1.add_edge(u, v)
    
    print("Graph:")
    print(g1)
    
    dfs_result = dfs_recursive(g1, 0)
    print(f"\nDFS Recursive from 0: {dfs_result}")
    
    dfs_iter = dfs_iterative(g1, 0)
    print(f"DFS Iterative from 0: {dfs_iter}")
    
    assert len(dfs_result) == 6, "DFS should visit all 6 vertices"
    print("DFS tests passed ✅")
    
    # Test 2: BFS
    print("\nTest 2: BFS on Undirected Graph")
    bfs_result = bfs(g1, 0)
    print(f"BFS from 0: {bfs_result}")
    assert len(bfs_result) == 6, "BFS should visit all 6 vertices"
    print("BFS tests passed ✅")
    
    # Test 3: Shortest path
    print("\nTest 3: Shortest Path")
    path = bfs_shortest_path(g1, 0, 4)
    print(f"Shortest path from 0 to 4: {path}")
    assert path == [0, 1, 4], "Shortest path should be [0, 1, 4]"
    print("Shortest path tests passed ✅")
    
    # Test 4: All paths
    print("\nTest 4: All Paths")
    all_paths = dfs_all_paths(g1, 0, 5)
    print(f"All paths from 0 to 5:")
    for path in all_paths:
        print(f"  {path}")
    assert len(all_paths) > 0, "Should find at least one path"
    print("All paths tests passed ✅")
    
    # Test 5: Level order
    print("\nTest 5: Level Order BFS")
    levels = bfs_level_order(g1, 0)
    print("Vertices by distance from 0:")
    for level, vertices in sorted(levels.items()):
        print(f"  Distance {level}: {vertices}")
    print("Level order tests passed ✅")
    
    # Test 6: Cycle detection (directed)
    print("\nTest 6: Cycle Detection (Directed Graph)")
    g2 = Graph(directed=True)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)  # Creates cycle
    assert has_cycle_directed(g2) == True, "Should detect cycle"
    print("Directed graph has cycle ✅")
    
    g3 = Graph(directed=True)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    assert has_cycle_directed(g3) == False, "Should not detect cycle"
    print("Directed graph without cycle ✅")
    
    # Test 7: Connected components
    print("\nTest 7: Connected Components")
    g4 = Graph(directed=False)
    g4.add_edge(0, 1)
    g4.add_edge(1, 2)
    g4.add_edge(3, 4)  # Separate component
    components = connected_components(g4)
    print(f"Connected components: {components}")
    assert len(components) == 2, "Should find 2 components"
    print("Connected components tests passed ✅")
    
    # Test 8: Topological sort
    print("\nTest 8: Topological Sort")
    g5 = Graph(directed=True)
    g5.add_edge('A', 'B')
    g5.add_edge('A', 'C')
    g5.add_edge('B', 'D')
    g5.add_edge('C', 'D')
    topo = topological_sort(g5)
    print(f"Topological order: {topo}")
    assert topo is not None, "Should return valid topological order"
    print("Topological sort tests passed ✅")
    
    # Test 9: Bipartite check
    print("\nTest 9: Bipartite Graph Check")
    g6 = Graph(directed=False)
    g6.add_edge(0, 1)
    g6.add_edge(1, 2)
    g6.add_edge(2, 3)
    is_bip, coloring = is_bipartite(g6)
    print(f"Graph is bipartite: {is_bip}")
    print(f"Coloring: {coloring}")
    assert is_bip == True, "Should be bipartite"
    print("Bipartite tests passed ✅")
    
    print("\n" + "=" * 50)
    print("All tests passed! 🎉")


if __name__ == "__main__":
    # Run comprehensive tests
    test_graph_traversal()
    
    # Demonstrate usage
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Graph Traversal Applications")
    print("=" * 60)
    
    # Demo: Social network
    print("\n1. Social Network (Friend Connections):")
    social = Graph(directed=False)
    connections = [
        ('Alice', 'Bob'), ('Alice', 'Charlie'),
        ('Bob', 'David'), ('Charlie', 'David'),
        ('David', 'Eve')
    ]
    
    for u, v in connections:
        social.add_edge(u, v)
    
    print("Network connections:")
    print(social)
    
    print("\nBFS from Alice (degrees of separation):")
    bfs_order = bfs(social, 'Alice')
    print(f"  {' -> '.join(bfs_order)}")
    
    print("\nShortest path from Alice to Eve:")
    path = bfs_shortest_path(social, 'Alice', 'Eve')
    print(f"  {' -> '.join(path)}")
    
    # Demo: Course prerequisites
    print("\n2. Course Prerequisites (Topological Sort):")
    courses = Graph(directed=True)
    prereqs = [
        ('Intro CS', 'Data Structures'),
        ('Data Structures', 'Algorithms'),
        ('Intro CS', 'Programming'),
        ('Programming', 'Algorithms')
    ]
    
    for prereq, course in prereqs:
        courses.add_edge(prereq, course)
    
    order = topological_sort(courses)
    print(f"Course order: {' -> '.join(order)}")