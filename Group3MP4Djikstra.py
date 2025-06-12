import heapq
import sys


# Function to construct the adjacency list from edge list
def construct_adjacency_list(edges, num_vertices):
    adjacency_list = [[] for _ in range(num_vertices)]
    for u, v, weight in edges:
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))  # Undirected graph
    return adjacency_list


# Dijkstra's Algorithm with step-by-step visualization
def dijkstra(num_vertices, edges, source):
    adjacency_list = construct_adjacency_list(edges, num_vertices)


    # Initialize all distances as infinite
    distances = [sys.maxsize] * num_vertices
    distances[source] = 0


    # Min-heap priority queue: (distance, vertex)
    priority_queue = [(0, source)]


    print(f"\nInitial distances: {distances}")
    print(f"Starting Dijkstra from source vertex {source}\n")


    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)


        print(f"> Visiting vertex {current_vertex} with current distance {current_distance}")


        # Check all neighbors of the current vertex
        for neighbor, weight in adjacency_list[current_vertex]:
            distance_through_u = current_distance + weight


            # If found a shorter path
            if distance_through_u < distances[neighbor]:
                print(f"  - Updating distance to vertex {neighbor}: {distances[neighbor]} → {distance_through_u}")
                distances[neighbor] = distance_through_u
                heapq.heappush(priority_queue, (distance_through_u, neighbor))
            else:
                print(f"  - Skipping vertex {neighbor}, current best: {distances[neighbor]}, via {current_vertex}: {distance_through_u}")


        print(f"  Current distance table: {distances}\n")


    return distances


# Main function to run the algorithm
if __name__ == "__main__":
    V = 5
    src = 0


    # Edge list: (u, v, weight)
    edges = [
        [0, 1, 4],
        [0, 2, 8],
        [1, 4, 6],
        [2, 3, 2],
        [3, 4, 10]
    ]


    shortest_distances = dijkstra(V, edges, src)


    print("\nFinal shortest distances from source vertex 0:")
    for vertex, distance in enumerate(shortest_distances):
        print(f"Vertex {vertex}: {distance}")