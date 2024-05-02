# Implement depth first search and Breadth first Search algorithm, Use an undirected graph and 
# develop a recursive algorithm for searching all the vertices of a graph or tree data tructure.


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

start_node = 'A'
visited = set()
queue = []

def bfs(graph, queue, visited):
    if not queue:
        return visited
    current_node = queue.pop(0)
    print(current_node, end=" ")    
    visited.append(current_node)

    for neighbor in graph[current_node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    return bfs(graph, queue, visited)

def dfs(graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour)

print("BFS: ", end ='')
bfs(graph, [start_node], [])
# BFS: A B C D E F

print()
print("DFS:", end = " ")
dfs(graph, start_node)
#DFS: A B D E F C 

# -------------------------------- BFS WITH COMMENTS ------------------------------------- #
# # Time complexity: O(V + E), where V is no. of vertices & E is no. of edges
# def bfs(graph, queue, visited):
#     if not queue:  # Checking if the queue is empty. O(1)
#         return visited
#     current_node = queue.pop(0)  # Removing the first element from the queue.
#     print(current_node, end=" ")   # Printing the current node. 
#     visited.append(current_node)   # Appending the current node to the visited list.

#     for neighbor in graph[current_node]:  # Iterating over the neighbors of the current node.
#         if neighbor not in visited and neighbor not in queue:  # Checking if the neighbor is not visited and not in the queue.
#             queue.append(neighbor)  # Adding the neighbor to the queue.

#     return bfs(graph, queue, visited)  # Recursively calling bfs.

# ------------------------------------------DFS WITH COMMENTS ------------------------------------ #
# # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# def dfs(graph, node):
#     if node not in visited:  # Checking if the node is not visited. O(1)
#         print(node, end=" ")  # Printing the current node. O(1)
#         visited.add(node)  # Adding the current node to the visited set. O(1)

#         for neighbour in graph[node]:  # Iterating over the neighbors of the current node. O(E)
#             dfs(graph, neighbour)  # Recursive call to dfs. O(V + E)
