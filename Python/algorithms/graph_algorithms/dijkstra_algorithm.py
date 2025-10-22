"""
Dijkstra's Algorithm - Shortest Path Algorithm
=============================================

Algorithm Description:
Dijkstra's algorithm finds the shortest paths from a source vertex to all other vertices 
in a weighted graph with non-negative edge weights. It uses a greedy approach with a 
priority queue to efficiently explore vertices in order of their distance from the source.

The algorithm maintains a set of vertices whose shortest distance from the source is known,
and repeatedly selects the unvisited vertex with minimum distance to explore its neighbors.

Time Complexity: O((V + E) log V) with binary heap, O(V²) with array
Space Complexity: O(V) for distance array and priority queue
Where V = number of vertices, E = number of edges

Applications:
- GPS Navigation systems (finding shortest routes)
- Network routing protocols (OSPF, IS-IS)
- Social networking (degrees of separation)
- Airline route planning
- Game AI pathfinding
"""

import heapq
from collections import defaultdict, deque
import math


class Graph:
    """
    Graph class to represent a weighted directed/undirected graph using adjacency list.
    """
    
    def __init__(self, directed=False):
        """
        Initialize the graph.
        
        Args:
            directed (bool): True for directed graph, False for undirected
        """
        self.graph = defaultdict(list)  # Adjacency list representation
        self.directed = directed
        self.vertices = set()
    
    def add_edge(self, u, v, weight):
        """
        Add an edge to the graph.
        
        Args:
            u: Source vertex
            v: Destination vertex
            weight (int/float): Weight of the edge (must be non-negative)
        
        Raises:
            ValueError: If weight is negative
        """
        if weight < 0:
            raise ValueError("Dijkstra's algorithm doesn't work with negative weights")
        
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        
        # For undirected graph, add reverse edge
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_vertices(self):
        """Return all vertices in the graph."""
        return list(self.vertices)
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex with their weights."""
        return self.graph[vertex]


def dijkstra(graph, start_vertex):
    """
    Dijkstra's algorithm implementation using binary heap (priority queue).
    
    Args:
        graph (Graph): The input graph
        start_vertex: Starting vertex for shortest path calculation
    
    Returns:
        tuple: (distances, previous_vertices) where:
               - distances: dict mapping vertex to shortest distance from start
               - previous_vertices: dict for reconstructing shortest paths
    
    Raises:
        ValueError: If start vertex is not in the graph
    """
    if start_vertex not in graph.vertices:
        raise ValueError(f"Start vertex {start_vertex} not found in graph")
    
    # Initialize distances and previous vertices
    distances = {vertex: math.inf for vertex in graph.vertices}
    previous = {vertex: None for vertex in graph.vertices}
    distances[start_vertex] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start_vertex)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Skip if already processed (due to duplicate entries in heap)
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
            
            # Calculate new distance through current vertex
            new_distance = current_distance + weight
            
            # If we found a shorter path, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (new_distance, neighbor))
    
    return distances, previous


def get_shortest_path(previous, start, end):
    """
    Reconstruct the shortest path from start to end vertex.
    
    Args:
        previous (dict): Previous vertices dictionary from Dijkstra's algorithm
        start: Start vertex
        end: End vertex
    
    Returns:
        list: Shortest path from start to end, or empty list if no path exists
    """
    if previous[end] is None and start != end:
        return []  # No path exists
    
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return path


def dijkstra_all_pairs(graph):
    """
    Find shortest paths between all pairs of vertices.
    
    Args:
        graph (Graph): The input graph
    
    Returns:
        dict: Nested dictionary where result[u][v] = shortest distance from u to v
    """
    all_distances = {}
    
    for vertex in graph.vertices:
        distances, _ = dijkstra(graph, vertex)
        all_distances[vertex] = distances
    
    return all_distances


def print_shortest_paths(graph, start_vertex):
    """
    Print shortest paths from start vertex to all other vertices.
    
    Args:
        graph (Graph): The input graph
        start_vertex: Starting vertex
    """
    distances, previous = dijkstra(graph, start_vertex)
    
    print(f"\nShortest paths from vertex '{start_vertex}':")
    print("=" * 50)
    
    for vertex in sorted(graph.vertices):
        if vertex == start_vertex:
            continue
        
        distance = distances[vertex]
        path = get_shortest_path(previous, start_vertex, vertex)
        
        if distance == math.inf:
            print(f"To {vertex}: No path exists")
        else:
            path_str = " -> ".join(map(str, path))
            print(f"To {vertex}: Distance = {distance}, Path = {path_str}")


# Test cases and examples
def create_sample_graph():
    """Create a sample graph for testing."""
    g = Graph(directed=False)
    
    # Add edges: (source, destination, weight)
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    return g


def create_directed_graph():
    """Create a sample directed graph for testing."""
    g = Graph(directed=True)
    
    edges = [
        (0, 1, 10), (0, 2, 3),
        (1, 2, 1), (1, 3, 2),
        (2, 1, 4), (2, 3, 8), (2, 4, 2),
        (3, 4, 7), (4, 3, 9)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    return g


def test_dijkstra():
    """Comprehensive test cases for Dijkstra's algorithm."""
    print("Testing Dijkstra's Algorithm")
    print("=" * 50)
    
    # Test 1: Undirected graph with letters
    print("\nTest 1: Undirected Graph")
    g1 = create_sample_graph()
    print_shortest_paths(g1, 'A')
    
    # Verify specific shortest paths
    distances, previous = dijkstra(g1, 'A')
    assert distances['D'] == 7, "Test 1 failed: A to D should be 7"
    assert distances['E'] == 9, "Test 1 failed: A to E should be 9"
    
    # Test 2: Directed graph with numbers
    print("\nTest 2: Directed Graph")
    g2 = create_directed_graph()
    print_shortest_paths(g2, 0)
    
    distances2, _ = dijkstra(g2, 0)
    assert distances2[4] == 5, "Test 2 failed: 0 to 4 should be 5"
    
    # Test 3: Single vertex
    print("\nTest 3: Single Vertex")
    g3 = Graph()
    g3.add_edge('X', 'X', 0)  # Self-loop
    distances3, _ = dijkstra(g3, 'X')
    print(f"Distance from X to X: {distances3['X']}")
    assert distances3['X'] == 0, "Test 3 failed"
    
    # Test 4: Disconnected graph
    print("\nTest 4: Disconnected Graph")
    g4 = Graph()
    g4.add_edge('A', 'B', 1)
    g4.add_edge('C', 'D', 2)
    distances4, _ = dijkstra(g4, 'A')
    print(f"Distance from A to C: {distances4['C']}")
    assert distances4['C'] == math.inf, "Test 4 failed: Should be infinity"
    
    print("\n" + "=" * 50)
    print("All tests passed! ✅")


def interactive_demo():
    """Interactive demonstration of Dijkstra's algorithm."""
    print("\nInteractive Dijkstra's Algorithm Demo")
    print("=" * 40)
    
    g = Graph()
    
    print("Build your graph by adding edges:")
    print("Enter edges in format: source destination weight")
    print("Type 'done' when finished, 'directed' to make graph directed")
    
    while True:
        user_input = input("Enter edge (or 'done'/'directed'): ").strip()
        
        if user_input.lower() == 'done':
            break
        elif user_input.lower() == 'directed':
            g.directed = True
            print("Graph is now directed")
            continue
        
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Please enter: source destination weight")
                continue
            
            source, dest, weight = parts[0], parts[1], float(parts[2])
            g.add_edge(source, dest, weight)
            print(f"Added edge: {source} -> {dest} (weight: {weight})")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input: {e}")
    
    if not g.vertices:
        print("No edges added. Demo finished.")
        return
    
    print(f"\nGraph vertices: {sorted(g.vertices)}")
    start = input("Enter start vertex: ").strip()
    
    if start not in g.vertices:
        print("Start vertex not found in graph.")
        return
    
    print_shortest_paths(g, start)


if __name__ == "__main__":
    # Run comprehensive tests
    test_dijkstra()
    
    # Demonstrate algorithm with sample graphs
    print("\n" + "=" * 60)
    print("DEMONSTRATION WITH SAMPLE GRAPHS")
    print("=" * 60)
    
    # Example 1: City road network
    print("\nExample: City Road Network")
    city_graph = Graph(directed=False)
    
    # Cities with distances in km
    roads = [
        ('NYC', 'Boston', 215), ('NYC', 'Philadelphia', 95),
        ('Boston', 'Philadelphia', 310), ('Philadelphia', 'Washington', 140),
        ('Boston', 'Washington', 440), ('NYC', 'Washington', 225)
    ]
    
    for city1, city2, distance in roads:
        city_graph.add_edge(city1, city2, distance)
    
    print("Finding shortest routes from New York City:")
    print_shortest_paths(city_graph, 'NYC')
    
    # Optional: Run interactive demo
    # Uncomment the line below to try the interactive version
    # interactive_demo()